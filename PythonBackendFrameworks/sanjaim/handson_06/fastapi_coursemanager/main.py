from typing import Optional

from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from database import engine, get_db, Base
from models import Course
from schemas import CourseCreate, CourseUpdate, CourseResponse

app = FastAPI(title='Course Management API', version='1.0')


@app.on_event('startup')
async def on_startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


@app.get('/')
def root():
    return {'message': 'API running'}


@app.post('/api/courses/')
async def create_course(course: CourseCreate, db: AsyncSession = Depends(get_db)):
    new_course = Course(**course.model_dump())
    db.add(new_course)
    await db.commit()
    await db.refresh(new_course)
    return CourseResponse.model_validate(new_course)


@app.get('/api/courses/{course_id}')
async def get_course(course_id: int, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Course).where(Course.id == course_id))
    course = result.scalar_one_or_none()
    if not course:
        raise HTTPException(status_code=404, detail='Course not found')
    return CourseResponse.model_validate(course)


@app.get('/api/courses/')
async def list_courses(
    skip: int = 0,
    limit: int = 10,
    department_id: Optional[int] = None,
    db: AsyncSession = Depends(get_db)
):
    query = select(Course)
    if department_id is not None:
        query = query.where(Course.department_id == department_id)
    query = query.offset(skip).limit(limit)

    result = await db.execute(query)
    courses = result.scalars().all()
    return [CourseResponse.model_validate(course) for course in courses]


@app.put('/api/courses/{course_id}')
async def update_course(course_id: int, course_update: CourseUpdate, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Course).where(Course.id == course_id))
    course = result.scalar_one_or_none()
    if not course:
        raise HTTPException(status_code=404, detail='Course not found')

    for field, value in course_update.model_dump(exclude_unset=True).items():
        setattr(course, field, value)

    await db.commit()
    await db.refresh(course)
    return CourseResponse.model_validate(course)


@app.delete('/api/courses/{course_id}')
async def delete_course(course_id: int, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Course).where(Course.id == course_id))
    course = result.scalar_one_or_none()
    if not course:
        raise HTTPException(status_code=404, detail='Course not found')

    await db.delete(course)
    await db.commit()
    return {'message': 'deleted'}
