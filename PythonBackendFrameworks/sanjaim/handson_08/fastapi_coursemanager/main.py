from typing import Optional, List

from fastapi import FastAPI, Depends, HTTPException, BackgroundTasks, Request, Response, status
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from sqlalchemy import select, or_
from sqlalchemy.ext.asyncio import AsyncSession

from database import engine, get_db, Base
from models import Course, Student, Enrollment
from schemas import (
    CourseCreate, CourseUpdate, CourseResponse,
    StudentCreate, StudentUpdate, StudentResponse,
    EnrollmentCreate, EnrollmentResponse,
)

app = FastAPI(
    title='Course Management API',
    description='REST API for managing departments, courses, students and enrollments.',
    version='1.0.0',
    contact={'name': 'Sanjai M', 'email': 'sanjaim899@gmail.com'},
)


@app.on_event('startup')
async def on_startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


def send_confirmation_email(student_email: str):
    print(f'Sending confirmation to {student_email}')


def build_error_payload(code: str, message: str, field: Optional[str] = None):
    return {'error': {'code': code, 'message': message, 'field': field}}


def raise_api_error(status_code: int, code: str, message: str, field: Optional[str] = None):
    raise HTTPException(status_code=status_code, detail=build_error_payload(code, message, field))


def raise_not_found(resource: str, resource_id: Optional[int] = None, field: Optional[str] = None):
    if resource_id is not None:
        message = f'{resource} with id {resource_id} does not exist'
    else:
        message = f'{resource} does not exist'
    raise_api_error(status.HTTP_404_NOT_FOUND, 'NOT_FOUND', message, field)


@app.exception_handler(HTTPException)
async def http_exception_handler(request: Request, exc: HTTPException):
    detail = exc.detail
    if isinstance(detail, dict) and 'error' in detail:
        payload = detail
    elif isinstance(detail, dict):
        payload = build_error_payload(detail.get('code', 'HTTP_ERROR'), detail.get('message', 'Request failed'), detail.get('field'))
    else:
        payload = build_error_payload('HTTP_ERROR', str(detail))
    return JSONResponse(status_code=exc.status_code, content=payload)


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    return JSONResponse(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, content=build_error_payload('VALIDATION_ERROR', 'Request validation failed', None))


@app.exception_handler(Exception)
async def unhandled_exception_handler(request: Request, exc: Exception):
    return JSONResponse(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, content=build_error_payload('INTERNAL_SERVER_ERROR', 'Internal server error', None))


@app.get('/')
def root():
    return {'message': 'API running'}


# Courses
# Versioning ->  URL versioning uses explicit paths such as /api/v1/courses/, while
# header-based versioning keeps the URL stable and sends version info in headers such as
# Accept: application/vnd.api+json;version=1.

@app.post(
    '/api/v1/courses/',
    response_model=CourseResponse,
    status_code=status.HTTP_201_CREATED,
    tags=['Courses'],
    summary='Create a new course',
    response_description='The created course',
)
async def create_course(course: CourseCreate, response: Response, db: AsyncSession = Depends(get_db)):
    new_course = Course(**course.model_dump())
    db.add(new_course)
    await db.commit()
    await db.refresh(new_course)
    response.headers['Location'] = f'/api/courses/{new_course.id}/'
    return new_course


@app.get('/api/v1/courses/', response_model=List[CourseResponse], tags=['Courses'])
async def list_courses(
    skip: int = 0,
    limit: int = 10,
    department_id: Optional[int] = None,
    search: Optional[str] = None,
    db: AsyncSession = Depends(get_db)
):
    query = select(Course)
    if department_id is not None:
        query = query.where(Course.department_id == department_id)
    if search:
        search_term = f'%{search}%'
        query = query.where(
            or_(
                Course.name.ilike(search_term),
                Course.code.ilike(search_term),
            )
        )
    query = query.offset(skip).limit(limit)

    result = await db.execute(query)
    return result.scalars().all()


@app.get('/api/v1/courses/{course_id}', response_model=CourseResponse, tags=['Courses'])
async def get_course(course_id: int, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Course).where(Course.id == course_id))
    course = result.scalar_one_or_none()
    if not course:
        raise_not_found('Course', course_id)
    return course


@app.put('/api/v1/courses/{course_id}', response_model=CourseResponse, tags=['Courses'])
async def update_course(course_id: int, course_update: CourseCreate, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Course).where(Course.id == course_id))
    course = result.scalar_one_or_none()
    if not course:
        raise_not_found('Course', course_id)

    for field, value in course_update.model_dump().items():
        setattr(course, field, value)

    await db.commit()
    await db.refresh(course)
    return course


@app.patch('/api/v1/courses/{course_id}/', response_model=CourseResponse, tags=['Courses'])
async def patch_course(course_id: int, course_update: CourseUpdate, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Course).where(Course.id == course_id))
    course = result.scalar_one_or_none()
    if not course:
        raise_not_found('Course', course_id)

    for field, value in course_update.model_dump(exclude_unset=True).items():
        setattr(course, field, value)

    await db.commit()
    await db.refresh(course)
    return course


@app.delete('/api/v1/courses/{course_id}', status_code=status.HTTP_204_NO_CONTENT, tags=['Courses'])
async def delete_course(course_id: int, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Course).where(Course.id == course_id))
    course = result.scalar_one_or_none()
    if not course:
        raise_not_found('Course', course_id)

    await db.delete(course)
    await db.commit()


@app.get('/api/v1/courses/{course_id}/students/', response_model=List[StudentResponse], tags=['Courses'])
async def get_course_students(course_id: int, db: AsyncSession = Depends(get_db)):
    course_result = await db.execute(select(Course).where(Course.id == course_id))
    if not course_result.scalar_one_or_none():
        raise_not_found('Course', course_id)

    result = await db.execute(
        select(Student).join(Enrollment, Enrollment.student_id == Student.id).where(Enrollment.course_id == course_id)
    )
    return result.scalars().all()




@app.post('/api/students/', response_model=StudentResponse, status_code=status.HTTP_201_CREATED, tags=['Students'])
async def create_student(student: StudentCreate, response: Response, db: AsyncSession = Depends(get_db)):
    new_student = Student(**student.model_dump())
    db.add(new_student)
    await db.commit()
    await db.refresh(new_student)
    response.headers['Location'] = f'/api/students/{new_student.id}/'
    return new_student


@app.get('/api/students/', response_model=List[StudentResponse], tags=['Students'])
async def list_students(db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Student))
    return result.scalars().all()


@app.get('/api/students/{student_id}', response_model=StudentResponse, tags=['Students'])
async def get_student(student_id: int, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Student).where(Student.id == student_id))
    student = result.scalar_one_or_none()
    if not student:
        raise_not_found('Student', student_id)
    return student


@app.put('/api/students/{student_id}', response_model=StudentResponse, tags=['Students'])
async def update_student(student_id: int, student_update: StudentUpdate, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Student).where(Student.id == student_id))
    student = result.scalar_one_or_none()
    if not student:
        raise_not_found('Student', student_id)

    for field, value in student_update.model_dump(exclude_unset=True).items():
        setattr(student, field, value)

    await db.commit()
    await db.refresh(student)
    return student


@app.delete('/api/students/{student_id}', status_code=status.HTTP_204_NO_CONTENT, tags=['Students'])
async def delete_student(student_id: int, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Student).where(Student.id == student_id))
    student = result.scalar_one_or_none()
    if not student:
        raise_not_found('Student', student_id)

    await db.delete(student)
    await db.commit()


# Enrollments

@app.post('/api/enrollments/', response_model=EnrollmentResponse, status_code=status.HTTP_201_CREATED, tags=['Enrollments'])
async def create_enrollment(
    enrollment: EnrollmentCreate,
    background_tasks: BackgroundTasks,
    response: Response,
    db: AsyncSession = Depends(get_db)
):
    student_result = await db.execute(select(Student).where(Student.id == enrollment.student_id))
    student = student_result.scalar_one_or_none()
    if not student:
        raise_not_found('Student', enrollment.student_id)

    course_result = await db.execute(select(Course).where(Course.id == enrollment.course_id))
    if not course_result.scalar_one_or_none():
        raise_not_found('Course', enrollment.course_id)

    new_enrollment = Enrollment(**enrollment.model_dump())
    db.add(new_enrollment)
    await db.commit()
    await db.refresh(new_enrollment)

    response.headers['Location'] = f'/api/enrollments/{new_enrollment.id}/'
    background_tasks.add_task(send_confirmation_email, student.email)
    return new_enrollment


@app.get('/api/enrollments/', response_model=List[EnrollmentResponse], tags=['Enrollments'])
async def list_enrollments(db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Enrollment))
    return result.scalars().all()


@app.get('/api/enrollments/{enrollment_id}', response_model=EnrollmentResponse, tags=['Enrollments'])
async def get_enrollment(enrollment_id: int, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Enrollment).where(Enrollment.id == enrollment_id))
    enrollment = result.scalar_one_or_none()
    if not enrollment:
        raise_not_found('Enrollment', enrollment_id)
    return enrollment


@app.delete('/api/enrollments/{enrollment_id}', status_code=status.HTTP_204_NO_CONTENT, tags=['Enrollments'])
async def delete_enrollment(enrollment_id: int, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Enrollment).where(Enrollment.id == enrollment_id))
    enrollment = result.scalar_one_or_none()
    if not enrollment:
        raise_not_found('Enrollment', enrollment_id)

    await db.delete(enrollment)
    await db.commit()
