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


'''
Output
(venv) [sanjai@sanjai handson_6]$ python crud.py
2026-07-11 16:05:43,846 INFO sqlalchemy.engine.Engine SELECT DATABASE()
2026-07-11 16:05:43,846 INFO sqlalchemy.engine.Engine [raw sql] {}
2026-07-11 16:05:43,847 INFO sqlalchemy.engine.Engine SELECT @@sql_mode
2026-07-11 16:05:43,847 INFO sqlalchemy.engine.Engine [raw sql] {}
2026-07-11 16:05:43,847 INFO sqlalchemy.engine.Engine SELECT @@lower_case_table_names
2026-07-11 16:05:43,847 INFO sqlalchemy.engine.Engine [raw sql] {}
2026-07-11 16:05:43,848 INFO sqlalchemy.engine.Engine BEGIN (implicit)
2026-07-11 16:05:43,849 INFO sqlalchemy.engine.Engine INSERT INTO departments (dept_name, head_of_dept, budget) VALUES (%(dept_name)s, %(head_of_dept)s, %(budget)s)
2026-07-11 16:05:43,849 INFO sqlalchemy.engine.Engine [generated in 0.00014s] {'dept_name': 'CSE', 'head_of_dept': 'dept_head1', 'budget': 50000.0}
2026-07-11 16:05:43,852 INFO sqlalchemy.engine.Engine INSERT INTO departments (dept_name, head_of_dept, budget) VALUES (%(dept_name)s, %(head_of_dept)s, %(budget)s)
2026-07-11 16:05:43,852 INFO sqlalchemy.engine.Engine [cached since 0.002942s ago] {'dept_name': 'IT', 'head_of_dept': 'dept_head2', 'budget': 35000.0}
2026-07-11 16:05:43,853 INFO sqlalchemy.engine.Engine INSERT INTO departments (dept_name, head_of_dept, budget) VALUES (%(dept_name)s, %(head_of_dept)s, %(budget)s)
2026-07-11 16:05:43,853 INFO sqlalchemy.engine.Engine [cached since 0.003604s ago] {'dept_name': 'EEE', 'head_of_dept': 'dept_head3', 'budget': 40000.0}
2026-07-11 16:05:43,853 INFO sqlalchemy.engine.Engine COMMIT
Inserted three departments
2026-07-11 16:05:43,856 INFO sqlalchemy.engine.Engine BEGIN (implicit)
2026-07-11 16:05:43,858 INFO sqlalchemy.engine.Engine SELECT departments.department_id AS departments_department_id, departments.dept_name AS departments_dept_name, departments.head_of_dept AS departments_head_of_dept, departments.budget AS departments_budget
FROM departments
WHERE departments.department_id = %(pk_1)s
2026-07-11 16:05:43,858 INFO sqlalchemy.engine.Engine [generated in 0.00010s] {'pk_1': 1}
2026-07-11 16:05:43,860 INFO sqlalchemy.engine.Engine SELECT departments.department_id AS departments_department_id, departments.dept_name AS departments_dept_name, departments.head_of_dept AS departments_head_of_dept, departments.budget AS departments_budget
FROM departments
WHERE departments.department_id = %(pk_1)s
2026-07-11 16:05:43,860 INFO sqlalchemy.engine.Engine [cached since 0.001649s ago] {'pk_1': 2}
2026-07-11 16:05:43,860 INFO sqlalchemy.engine.Engine SELECT departments.department_id AS departments_department_id, departments.dept_name AS departments_dept_name, departments.head_of_dept AS departments_head_of_dept, departments.budget AS departments_budget
FROM departments
WHERE departments.department_id = %(pk_1)s
2026-07-11 16:05:43,860 INFO sqlalchemy.engine.Engine [cached since 0.002441s ago] {'pk_1': 3}
2026-07-11 16:05:43,862 INFO sqlalchemy.engine.Engine INSERT INTO students (first_name, last_name, email, date_of_birth, department_id, enrollment_year) VALUES (%(first_name)s, %(last_name)s, %(email)s, %(date_of_birth)s, %(department_id)s, %(enrollment_year)s)
2026-07-11 16:05:43,862 INFO sqlalchemy.engine.Engine [generated in 0.00008s] {'first_name': 'student', 'last_name': 'one', 'email': 'studentone@gmail.com', 'date_of_birth': datetime.date(2005, 1, 1), 'department_id': 1, 'enrollment_year': 2026}
2026-07-11 16:05:43,865 INFO sqlalchemy.engine.Engine INSERT INTO students (first_name, last_name, email, date_of_birth, department_id, enrollment_year) VALUES (%(first_name)s, %(last_name)s, %(email)s, %(date_of_birth)s, %(department_id)s, %(enrollment_year)s)
2026-07-11 16:05:43,865 INFO sqlalchemy.engine.Engine [cached since 0.003694s ago] {'first_name': 'student', 'last_name': 'two', 'email': 'studenttwo@gmail.com', 'date_of_birth': datetime.date(2005, 1, 2), 'department_id': 1, 'enrollment_year': 2026}
2026-07-11 16:05:43,866 INFO sqlalchemy.engine.Engine INSERT INTO students (first_name, last_name, email, date_of_birth, department_id, enrollment_year) VALUES (%(first_name)s, %(last_name)s, %(email)s, %(date_of_birth)s, %(department_id)s, %(enrollment_year)s)
2026-07-11 16:05:43,866 INFO sqlalchemy.engine.Engine [cached since 0.004069s ago] {'first_name': 'student', 'last_name': 'three', 'email': 'studentthree@gmail.com', 'date_of_birth': datetime.date(2005, 1, 3), 'department_id': 2, 'enrollment_year': 2026}
2026-07-11 16:05:43,866 INFO sqlalchemy.engine.Engine INSERT INTO students (first_name, last_name, email, date_of_birth, department_id, enrollment_year) VALUES (%(first_name)s, %(last_name)s, %(email)s, %(date_of_birth)s, %(department_id)s, %(enrollment_year)s)
2026-07-11 16:05:43,866 INFO sqlalchemy.engine.Engine [cached since 0.004636s ago] {'first_name': 'student', 'last_name': 'four', 'email': 'studentfour@gmail.com', 'date_of_birth': datetime.date(2005, 1, 4), 'department_id': 3, 'enrollment_year': 2026}
2026-07-11 16:05:43,867 INFO sqlalchemy.engine.Engine INSERT INTO students (first_name, last_name, email, date_of_birth, department_id, enrollment_year) VALUES (%(first_name)s, %(last_name)s, %(email)s, %(date_of_birth)s, %(department_id)s, %(enrollment_year)s)
2026-07-11 16:05:43,867 INFO sqlalchemy.engine.Engine [cached since 0.005051s ago] {'first_name': 'student', 'last_name': 'five', 'email': 'studentfive@gmail.com', 'date_of_birth': datetime.date(2005, 1, 5), 'department_id': 1, 'enrollment_year': 2026}
2026-07-11 16:05:43,867 INFO sqlalchemy.engine.Engine COMMIT
Inserted 5 student details
2026-07-11 16:05:43,869 INFO sqlalchemy.engine.Engine BEGIN (implicit)
2026-07-11 16:05:43,869 INFO sqlalchemy.engine.Engine SELECT departments.department_id AS departments_department_id, departments.dept_name AS departments_dept_name, departments.head_of_dept AS departments_head_of_dept, departments.budget AS departments_budget
FROM departments
WHERE departments.department_id = %(pk_1)s
2026-07-11 16:05:43,869 INFO sqlalchemy.engine.Engine [cached since 0.01094s ago] {'pk_1': 1}
2026-07-11 16:05:43,870 INFO sqlalchemy.engine.Engine SELECT departments.department_id AS departments_department_id, departments.dept_name AS departments_dept_name, departments.head_of_dept AS departments_head_of_dept, departments.budget AS departments_budget
FROM departments
WHERE departments.department_id = %(pk_1)s
2026-07-11 16:05:43,870 INFO sqlalchemy.engine.Engine [cached since 0.01219s ago] {'pk_1': 2}
2026-07-11 16:05:43,872 INFO sqlalchemy.engine.Engine INSERT INTO courses (course_name, course_code, credits, department_id, max_set, max_seats) VALUES (%(course_name)s, %(course_code)s, %(credits)s, %(department_id)s, %(max_set)s, %(max_seats)s)
2026-07-11 16:05:43,872 INFO sqlalchemy.engine.Engine [generated in 0.00018s] {'course_name': 'TOC', 'course_code': 'CS200', 'credits': 3, 'department_id': 1, 'max_set': 60, 'max_seats': 60}
2026-07-11 16:05:43,874 INFO sqlalchemy.engine.Engine INSERT INTO courses (course_name, course_code, credits, department_id, max_set, max_seats) VALUES (%(course_name)s, %(course_code)s, %(credits)s, %(department_id)s, %(max_set)s, %(max_seats)s)
2026-07-11 16:05:43,874 INFO sqlalchemy.engine.Engine [cached since 0.002256s ago] {'course_name': 'Resource Management', 'course_code': 'CS201', 'credits': 3, 'department_id': 1, 'max_set': 60, 'max_seats': 60}
2026-07-11 16:05:43,875 INFO sqlalchemy.engine.Engine INSERT INTO courses (course_name, course_code, credits, department_id, max_set, max_seats) VALUES (%(course_name)s, %(course_code)s, %(credits)s, %(department_id)s, %(max_set)s, %(max_seats)s)
2026-07-11 16:05:43,875 INFO sqlalchemy.engine.Engine [cached since 0.002762s ago] {'course_name': 'Machine Learning', 'course_code': 'CS202', 'credits': 3, 'department_id': 2, 'max_set': 60, 'max_seats': 60}
2026-07-11 16:05:43,875 INFO sqlalchemy.engine.Engine COMMIT
Inserted three courses
2026-07-11 16:05:43,877 INFO sqlalchemy.engine.Engine BEGIN (implicit)
2026-07-11 16:05:43,878 INFO sqlalchemy.engine.Engine SELECT students.student_id AS students_student_id, students.first_name AS students_first_name, students.last_name AS students_last_name, students.email AS students_email, students.date_of_birth AS students_date_of_birth, students.department_id AS students_department_id, students.enrollment_year AS students_enrollment_year
FROM students
WHERE students.student_id = %(pk_1)s
2026-07-11 16:05:43,878 INFO sqlalchemy.engine.Engine [generated in 0.00009s] {'pk_1': 1}
2026-07-11 16:05:43,879 INFO sqlalchemy.engine.Engine SELECT courses.course_id AS courses_course_id, courses.course_name AS courses_course_name, courses.course_code AS courses_course_code, courses.credits AS courses_credits, courses.department_id AS courses_department_id, courses.max_set AS courses_max_set, courses.max_seats AS courses_max_seats
FROM courses
WHERE courses.course_id = %(pk_1)s
2026-07-11 16:05:43,879 INFO sqlalchemy.engine.Engine [generated in 0.00008s] {'pk_1': 1}
2026-07-11 16:05:43,880 INFO sqlalchemy.engine.Engine SELECT courses.course_id AS courses_course_id, courses.course_name AS courses_course_name, courses.course_code AS courses_course_code, courses.credits AS courses_credits, courses.department_id AS courses_department_id, courses.max_set AS courses_max_set, courses.max_seats AS courses_max_seats
FROM courses
WHERE courses.course_id = %(pk_1)s
2026-07-11 16:05:43,880 INFO sqlalchemy.engine.Engine [cached since 0.0006187s ago] {'pk_1': 2}
2026-07-11 16:05:43,880 INFO sqlalchemy.engine.Engine SELECT students.student_id AS students_student_id, students.first_name AS students_first_name, students.last_name AS students_last_name, students.email AS students_email, students.date_of_birth AS students_date_of_birth, students.department_id AS students_department_id, students.enrollment_year AS students_enrollment_year
FROM students
WHERE students.student_id = %(pk_1)s
2026-07-11 16:05:43,880 INFO sqlalchemy.engine.Engine [cached since 0.002374s ago] {'pk_1': 2}
2026-07-11 16:05:43,881 INFO sqlalchemy.engine.Engine SELECT courses.course_id AS courses_course_id, courses.course_name AS courses_course_name, courses.course_code AS courses_course_code, courses.credits AS courses_credits, courses.department_id AS courses_department_id, courses.max_set AS courses_max_set, courses.max_seats AS courses_max_seats
FROM courses
WHERE courses.course_id = %(pk_1)s
2026-07-11 16:05:43,881 INFO sqlalchemy.engine.Engine [cached since 0.001526s ago] {'pk_1': 3}
2026-07-11 16:05:43,881 INFO sqlalchemy.engine.Engine SELECT students.student_id AS students_student_id, students.first_name AS students_first_name, students.last_name AS students_last_name, students.email AS students_email, students.date_of_birth AS students_date_of_birth, students.department_id AS students_department_id, students.enrollment_year AS students_enrollment_year
FROM students
WHERE students.student_id = %(pk_1)s
2026-07-11 16:05:43,881 INFO sqlalchemy.engine.Engine [cached since 0.003216s ago] {'pk_1': 3}
2026-07-11 16:05:43,882 INFO sqlalchemy.engine.Engine INSERT INTO enrollments (student_id, course_id, enrollment_date, grade) VALUES (%(student_id)s, %(course_id)s, %(enrollment_date)s, %(grade)s)
2026-07-11 16:05:43,882 INFO sqlalchemy.engine.Engine [generated in 0.00007s] {'student_id': 1, 'course_id': 1, 'enrollment_date': datetime.date(2026, 1, 15), 'grade': 'A'}
2026-07-11 16:05:43,883 INFO sqlalchemy.engine.Engine INSERT INTO enrollments (student_id, course_id, enrollment_date, grade) VALUES (%(student_id)s, %(course_id)s, %(enrollment_date)s, %(grade)s)
2026-07-11 16:05:43,883 INFO sqlalchemy.engine.Engine [cached since 0.0007791s ago] {'student_id': 1, 'course_id': 2, 'enrollment_date': datetime.date(2026, 1, 15), 'grade': 'B+'}
2026-07-11 16:05:43,883 INFO sqlalchemy.engine.Engine INSERT INTO enrollments (student_id, course_id, enrollment_date, grade) VALUES (%(student_id)s, %(course_id)s, %(enrollment_date)s, %(grade)s)
2026-07-11 16:05:43,883 INFO sqlalchemy.engine.Engine [cached since 0.0009816s ago] {'student_id': 2, 'course_id': 3, 'enrollment_date': datetime.date(2026, 1, 16), 'grade': 'A'}
2026-07-11 16:05:43,883 INFO sqlalchemy.engine.Engine INSERT INTO enrollments (student_id, course_id, enrollment_date, grade) VALUES (%(student_id)s, %(course_id)s, %(enrollment_date)s, %(grade)s)
2026-07-11 16:05:43,883 INFO sqlalchemy.engine.Engine [cached since 0.001136s ago] {'student_id': 3, 'course_id': 2, 'enrollment_date': datetime.date(2026, 1, 17), 'grade': 'B'}
2026-07-11 16:05:43,883 INFO sqlalchemy.engine.Engine COMMIT
Inserted Four enrollments
83. READ: Query all students in department 'Computer Science' using session.query(Student).join(Department).filter(Department.dept_name == 'Computer Science').
2026-07-11 16:05:43,885 INFO sqlalchemy.engine.Engine BEGIN (implicit)
2026-07-11 16:05:43,886 INFO sqlalchemy.engine.Engine SELECT students.student_id AS students_student_id, students.first_name AS students_first_name, students.last_name AS students_last_name, students.email AS students_email, students.date_of_birth AS students_date_of_birth, students.department_id AS students_department_id, students.enrollment_year AS students_enrollment_year
FROM students INNER JOIN departments ON departments.department_id = students.department_id
WHERE departments.head_of_dept = %(head_of_dept_1)s
2026-07-11 16:05:43,886 INFO sqlalchemy.engine.Engine [generated in 0.00011s] {'head_of_dept_1': 'Dr. Alan Turing'}
84. READ: Query all enrollments and print each student's name alongside course name. Enable echo=True on the engine to count SQL queries issued
2026-07-11 16:05:43,891 INFO sqlalchemy.engine.Engine SELECT enrollments.enrollment_id AS enrollments_enrollment_id, enrollments.student_id AS enrollments_student_id, enrollments.course_id AS enrollments_course_id, enrollments.enrollment_date AS enrollments_enrollment_date, enrollments.grade AS enrollments_grade, students_1.student_id AS students_1_student_id, students_1.first_name AS students_1_first_name, students_1.last_name AS students_1_last_name, students_1.email AS students_1_email, students_1.date_of_birth AS students_1_date_of_birth, students_1.department_id AS students_1_department_id, students_1.enrollment_year AS students_1_enrollment_year, courses_1.course_id AS courses_1_course_id, courses_1.course_name AS courses_1_course_name, courses_1.course_code AS courses_1_course_code, courses_1.credits AS courses_1_credits, courses_1.department_id AS courses_1_department_id, courses_1.max_set AS courses_1_max_set, courses_1.max_seats AS courses_1_max_seats
FROM enrollments LEFT OUTER JOIN students AS students_1 ON students_1.student_id = enrollments.student_id LEFT OUTER JOIN courses AS courses_1 ON courses_1.course_id = enrollments.course_id
2026-07-11 16:05:43,891 INFO sqlalchemy.engine.Engine [generated in 0.00009s] {}
   - student one → TOC (Grade: A)
   - student one → Resource Management (Grade: B+)
   - student two → Machine Learning (Grade: A)
   - student three → Resource Management (Grade: B)
85. UPDATE: Find a specific student by email and update their enrollment_year. Commit.
2026-07-11 16:05:43,892 INFO sqlalchemy.engine.Engine SELECT students.student_id AS students_student_id, students.first_name AS students_first_name, students.last_name AS students_last_name, students.email AS students_email, students.date_of_birth AS students_date_of_birth, students.department_id AS students_department_id, students.enrollment_year AS students_enrollment_year
FROM students
WHERE students.email = %(email_1)s
 LIMIT %(param_1)s
2026-07-11 16:05:43,892 INFO sqlalchemy.engine.Engine [generated in 0.00008s] {'email_1': 'studentone@gmail.com', 'param_1': 1}
2026-07-11 16:05:43,894 INFO sqlalchemy.engine.Engine UPDATE students SET enrollment_year=%(enrollment_year)s WHERE students.student_id = %(students_student_id)s
2026-07-11 16:05:43,894 INFO sqlalchemy.engine.Engine [generated in 0.00007s] {'enrollment_year': 2027, 'students_student_id': 1}
2026-07-11 16:05:43,894 INFO sqlalchemy.engine.Engine COMMIT
2026-07-11 16:05:43,896 INFO sqlalchemy.engine.Engine BEGIN (implicit)
2026-07-11 16:05:43,896 INFO sqlalchemy.engine.Engine SELECT students.student_id AS students_student_id, students.first_name AS students_first_name, students.last_name AS students_last_name, students.email AS students_email, students.date_of_birth AS students_date_of_birth, students.department_id AS students_department_id, students.enrollment_year AS students_enrollment_year
FROM students
WHERE students.student_id = %(pk_1)s
2026-07-11 16:05:43,896 INFO sqlalchemy.engine.Engine [cached since 0.01819s ago] {'pk_1': 1}
Updated enrollment for student student one to 2027
86. DELETE: Remove an enrollment record using session.delete(enrollment_obj). Commit and verify.
2026-07-11 16:05:43,898 INFO sqlalchemy.engine.Engine SELECT enrollments.enrollment_id AS enrollments_enrollment_id, enrollments.student_id AS enrollments_student_id, enrollments.course_id AS enrollments_course_id, enrollments.enrollment_date AS enrollments_enrollment_date, enrollments.grade AS enrollments_grade
FROM enrollments INNER JOIN students ON students.student_id = enrollments.student_id INNER JOIN courses ON courses.course_id = enrollments.course_id
WHERE students.email = %(email_1)s AND courses.course_name = %(course_name_1)s
 LIMIT %(param_1)s
2026-07-11 16:05:43,898 INFO sqlalchemy.engine.Engine [generated in 0.00008s] {'email_1': 'studenttwo@gmail.com', 'course_name_1': 'Machine Learning', 'param_1': 1}
2026-07-11 16:05:43,899 INFO sqlalchemy.engine.Engine DELETE FROM enrollments WHERE enrollments.enrollment_id = %(enrollment_id)s
2026-07-11 16:05:43,899 INFO sqlalchemy.engine.Engine [generated in 0.00008s] {'enrollment_id': 3}
2026-07-11 16:05:43,900 INFO sqlalchemy.engine.Engine COMMIT
2026-07-11 16:05:43,903 INFO sqlalchemy.engine.Engine BEGIN (implicit)
2026-07-11 16:05:43,903 INFO sqlalchemy.engine.Engine SELECT students.student_id AS students_student_id, students.first_name AS students_first_name, students.last_name AS students_last_name, students.email AS students_email, students.date_of_birth AS students_date_of_birth, students.department_id AS students_department_id, students.enrollment_year AS students_enrollment_year
FROM students
WHERE students.student_id = %(pk_1)s
2026-07-11 16:05:43,903 INFO sqlalchemy.engine.Engine [cached since 0.02535s ago] {'pk_1': 2}
2026-07-11 16:05:43,904 INFO sqlalchemy.engine.Engine SELECT courses.course_id AS courses_course_id, courses.course_name AS courses_course_name, courses.course_code AS courses_course_code, courses.credits AS courses_credits, courses.department_id AS courses_department_id, courses.max_set AS courses_max_set, courses.max_seats AS courses_max_seats
FROM courses
WHERE courses.course_id = %(pk_1)s
2026-07-11 16:05:43,904 INFO sqlalchemy.engine.Engine [cached since 0.02479s ago] {'pk_1': 3}
Deleted student: student two enrollment Machine Learning
2026-07-11 16:05:43,904 INFO sqlalchemy.engine.Engine ROLLBACK
(venv) [sanjai@sanjai handson_6]$

'''