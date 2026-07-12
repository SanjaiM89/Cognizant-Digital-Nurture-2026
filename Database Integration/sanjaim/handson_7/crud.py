'''
90. Compare the two outputs and document the difference in a comment block at the top of crud.py
-> without using joinedload we will be using session.query(Enrollment).all() that will fetch all enrollments, now in the fo loop accessing
enrollment.student and enrollment.course will trigger another two additional queries per enrollment. This creates a N+1 problem. It is not using any
join queries
-> Using Joinedload
 joinedload(Enrollment.student), joinedload(Enrollment.course) will modify the sql queries to use left outer join this fetches all enrollments and the
 realted student and course details in one query
'''


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, joinedload
from models import Base, Department, Student, Professor, Course, Enrollment
from datetime import date

engine = create_engine('mysql+pymysql://sanjai:abcdef@localhost:3306/college_db', echo=True)
Session = sessionmaker(bind=engine)
session = Session()

try:
    dept_cs = Department(head_of_dept="dept_head1", budget=50000.00, dept_name="CSE")
    dept_it = Department(head_of_dept="dept_head2", budget=35000.00, dept_name="IT")
    dept_eee = Department(head_of_dept="dept_head3", budget=40000.00, dept_name="EEE")

    session.add_all([dept_cs, dept_it, dept_eee])
    session.commit()
    print("Inserted three departments")

    student1 = Student(
        first_name="student", last_name="one",
        email="studentone@gmail.com",
        date_of_birth=date(2005, 1, 1),
        department_id=dept_cs.department_id,
        enrollment_year=2026
    )
    student2 = Student(
        first_name="student", last_name="two",
        email="studenttwo@gmail.com",
        date_of_birth=date(2005, 1, 2),
        department_id=dept_cs.department_id,
        enrollment_year=2026
    )
    student3 = Student(
        first_name="student", last_name="three",
        email="studentthree@gmail.com",
        date_of_birth=date(2005, 1, 3),
        department_id=dept_it.department_id,
        enrollment_year=2026
    )
    student4 = Student(
        first_name="student", last_name="four",
        email="studentfour@gmail.com",
        date_of_birth=date(2005, 1, 4),
        department_id=dept_eee.department_id,
        enrollment_year=2026
    )
    student5 = Student(
        first_name="student", last_name="five",
        email="studentfive@gmail.com",
        date_of_birth=date(2005, 1, 5),
        department_id=dept_cs.department_id,
        enrollment_year=2026
    )
    
    session.add_all([student1, student2, student3, student4, student5])
    session.commit()
    print("Inserted 5 student details")

    course1 = Course(
        course_name="TOC",
        course_code="CS200",
        credits=3,
        department_id=dept_cs.department_id,
        max_seats=60
        )
    course2 = Course(
        course_name="Resource Management",
        course_code="CS201",
        credits=3,
        department_id=dept_cs.department_id,
        max_seats=60
    )
    course3 = Course(
        course_name="Machine Learning",
        course_code="CS202",
        credits=3,
        department_id=dept_it.department_id,
        max_seats=60
    )
    
    session.add_all([course1, course2, course3])
    session.commit()
    print("Inserted three courses")

    enrollment1 = Enrollment(
        student_id=student1.student_id,
        course_id=course1.course_id,
        enrollment_date=date(2026, 1, 15),
        grade="A"
    )
    enrollment2 = Enrollment(
        student_id=student1.student_id,
        course_id=course2.course_id,
        enrollment_date=date(2026, 1, 15),
        grade="B+"
    )
    enrollment3 = Enrollment(
        student_id=student2.student_id,
        course_id=course3.course_id,
        enrollment_date=date(2026, 1, 16),
        grade="A"
    )
    enrollment4 = Enrollment(
        student_id=student3.student_id,
        course_id=course2.course_id,
        enrollment_date=date(2026, 1, 17),
        grade="B"
    )

    session.add_all([enrollment1, enrollment2, enrollment3, enrollment4])
    session.commit()
    print("Inserted Four enrollments")

    print("83. READ: Query all students in department 'Computer Science' using session.query(Student).join(Department).filter(Department.dept_name == 'Computer Science').")
    cs_students = session.query(Student).join(Department).filter(
        Department.head_of_dept == "Dr. Alan Turing"
    ).all()
    for student in cs_students:
        print(f"   - {student.first_name} {student.last_name}")

    print("84. READ: Query all enrollments and print each student's name alongside course name. Enable echo=True on the engine to count SQL queries issued")
    enrollments = session.query(Enrollment).options(
        joinedload(Enrollment.student),
        joinedload(Enrollment.course)
    ).all()

    for enrollment in enrollments:
        student_name = f"{enrollment.student.first_name} {enrollment.student.last_name}"
        course_name = enrollment.course.course_name
        print(f"   - {student_name} → {course_name} (Grade: {enrollment.grade})")

    print("85. UPDATE: Find a specific student by email and update their enrollment_year. Commit.")

    student = session.query(Student).filter_by(email="studentone@gmail.com").first()
    if student:
        student.enrollment_year = 2027
        session.commit()
        print(f"Updated enrollment for student {student.first_name} {student.last_name} to 2027")

    print("86. DELETE: Remove an enrollment record using session.delete(enrollment_obj). Commit and verify.")
    enrollment_to_delete = session.query(Enrollment).join(Student).join(Course).filter(
        Student.email == "studenttwo@gmail.com",
        Course.course_name == "Machine Learning"
    ).first()

    if enrollment_to_delete:
        session.delete(enrollment_to_delete)
        session.commit()
        print(f"Deleted student: {enrollment_to_delete.student.first_name} {enrollment_to_delete.student.last_name} enrollment {enrollment_to_delete.course.course_name}")

except Exception as e:
    session.rollback()
    raise
finally:
    session.close()