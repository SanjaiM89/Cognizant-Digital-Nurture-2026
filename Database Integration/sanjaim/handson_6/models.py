from sqlalchemy import create_engine, text, Column, Integer, String, Float, Date, ForeignKey, Numeric, CHAR, Index
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.exc import OperationalError

Base = declarative_base()

def get_engine():
    engine = create_engine('mysql+pymysql://sanjai:abcdef@localhost:3306/college_db',echo=True)

    try:
        with engine.connect() as conn:
            conn.execute(text("select 1"))
        print("CONNECTED SUCCESSFULLY")
        return engine
    except OperationalError as e:
        if "Unknown databas" in str(e):
            print("Database not Exist... Creating it...")

            default_engine = create_engine('mysql+pymysql://sanjai:abcdef@localhost:3306/mysql',echo=True)

            with default_engine.connect() as conn:
                conn.execute(text('create database if not exists college_db'))
                conn.commit()
            print("Database Created")

            return create_engine('mysql+pymysql://sanjai:abcdef@localhost:3306/college_db',echo=True)
        else:
            raise

class Department(Base):
    __tablename__ = 'departments'

    department_id = Column(Integer, primary_key=True, autoincrement=True)
    dept_name = Column(String(100), nullable=True,unique=True)
    head_of_dept = Column(String(100), nullable=True, unique=True)
    budget = Column(Numeric(precision=10, scale=2), nullable=True)
    students = relationship("Student", back_populates="department")
    professors = relationship("Professor", back_populates="department")
    courses = relationship("Course", back_populates="department")

class Student(Base):
    __tablename__ = 'students'

    student_id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String(100), nullable=True)
    last_name = Column(String(100), nullable=True)
    email = Column(String(200), nullable=True, unique=True)
    date_of_birth = Column(Date, nullable=True)
    department_id = Column(Integer, ForeignKey('departments.department_id'),nullable=True)
    enrollment_year = Column(Integer, nullable=True)

    department = relationship("Department", back_populates="students")
    enrollments = relationship("Enrollment", back_populates="student")

class Professor(Base):
    __tablename__ = 'professors'
    
    professor_id = Column(Integer, primary_key=True, autoincrement=True)
    prof_name = Column(String(100), nullable=False)
    email = Column(String(100), unique=True, nullable=True)
    department_id = Column(Integer, ForeignKey('departments.department_id'), nullable=True)
    salary = Column(Numeric(10, 2), nullable=True)  # DECIMAL(10,2) in MySQL
    department = relationship("Department", back_populates="professors")

class Enrollment(Base):
    __tablename__ = 'enrollments'
    enrollment_id = Column(Integer, primary_key=True, autoincrement=True)
    student_id = Column(Integer, ForeignKey('students.student_id'), nullable=True)
    course_id = Column(Integer, ForeignKey('courses.course_id'), nullable=True)
    enrollment_date = Column(Date, nullable=True)
    grade = Column(CHAR(2), nullable=True)
    

    student = relationship("Student", back_populates="enrollments")
    course = relationship("Course", back_populates="enrollments")

class Course(Base):
    __tablename__ = 'courses'
    
    course_id = Column(Integer, primary_key=True, autoincrement=True)
    course_name = Column(String(150), nullable=True)
    course_code = Column(String(20), nullable=True)
    credits = Column(Integer, nullable=True)
    department_id = Column(Integer, ForeignKey('departments.department_id'), nullable=True)
    max_set = Column(Integer, nullable=True, default=60)
    max_seats = Column(Integer, nullable=True, default=60)
    
    department = relationship("Department", back_populates="courses")
    enrollments = relationship("Enrollment", back_populates="course")

    __table_args__ = (
        Index('idx_course_code', 'course_code'),
    )

if __name__ == "__main__":
    engine = get_engine()
    Base.metadata.create_all(engine)
    print("Tables created")


#Output

'''
2026-07-11 13:13:52,125 INFO sqlalchemy.engine.Engine create database if not exists college_db
2026-07-11 13:13:52,125 INFO sqlalchemy.engine.Engine [generated in 0.00023s] {}
2026-07-11 13:13:52,134 INFO sqlalchemy.engine.Engine COMMIT
Database Created
2026-07-11 13:13:52,144 INFO sqlalchemy.engine.Engine SELECT DATABASE()
2026-07-11 13:13:52,144 INFO sqlalchemy.engine.Engine [raw sql] {}
2026-07-11 13:13:52,144 INFO sqlalchemy.engine.Engine SELECT @@sql_mode
2026-07-11 13:13:52,144 INFO sqlalchemy.engine.Engine [raw sql] {}
2026-07-11 13:13:52,145 INFO sqlalchemy.engine.Engine SELECT @@lower_case_table_names
2026-07-11 13:13:52,145 INFO sqlalchemy.engine.Engine [raw sql] {}
2026-07-11 13:13:52,145 INFO sqlalchemy.engine.Engine BEGIN (implicit)
2026-07-11 13:13:52,145 INFO sqlalchemy.engine.Engine DESCRIBE `college_db`.`departments`
2026-07-11 13:13:52,145 INFO sqlalchemy.engine.Engine [raw sql] {}
2026-07-11 13:13:52,147 INFO sqlalchemy.engine.Engine DESCRIBE `college_db`.`students`
2026-07-11 13:13:52,147 INFO sqlalchemy.engine.Engine [raw sql] {}
2026-07-11 13:13:52,148 INFO sqlalchemy.engine.Engine DESCRIBE `college_db`.`professors`
2026-07-11 13:13:52,148 INFO sqlalchemy.engine.Engine [raw sql] {}
2026-07-11 13:13:52,149 INFO sqlalchemy.engine.Engine DESCRIBE `college_db`.`enrollments`
2026-07-11 13:13:52,149 INFO sqlalchemy.engine.Engine [raw sql] {}
2026-07-11 13:13:52,149 INFO sqlalchemy.engine.Engine DESCRIBE `college_db`.`courses`
2026-07-11 13:13:52,149 INFO sqlalchemy.engine.Engine [raw sql] {}
2026-07-11 13:13:52,150 INFO sqlalchemy.engine.Engine
CREATE TABLE departments (
	department_id INTEGER NOT NULL AUTO_INCREMENT,
	head_of_dept VARCHAR(100),
	budget NUMERIC(10, 2),
	PRIMARY KEY (department_id),
	UNIQUE (head_of_dept)
)


2026-07-11 13:13:52,150 INFO sqlalchemy.engine.Engine [no key 0.00009s] {}
2026-07-11 13:13:52,171 INFO sqlalchemy.engine.Engine
CREATE TABLE students (
	student_id INTEGER NOT NULL AUTO_INCREMENT,
	first_name VARCHAR(100),
	last_name VARCHAR(100),
	email VARCHAR(200),
	date_of_birth DATE,
	department_id INTEGER,
	enrollment_year INTEGER,
	PRIMARY KEY (student_id),
	UNIQUE (email),
	FOREIGN KEY(department_id) REFERENCES departments (department_id)
)


2026-07-11 13:13:52,172 INFO sqlalchemy.engine.Engine [no key 0.00011s] {}
2026-07-11 13:13:52,185 INFO sqlalchemy.engine.Engine
CREATE TABLE professors (
	professor_id INTEGER NOT NULL AUTO_INCREMENT,
	prof_name VARCHAR(100) NOT NULL,
	email VARCHAR(100),
	department_id INTEGER,
	salary NUMERIC(10, 2),
	PRIMARY KEY (professor_id),
	UNIQUE (email),
	FOREIGN KEY(department_id) REFERENCES departments (department_id)
)


2026-07-11 13:13:52,186 INFO sqlalchemy.engine.Engine [no key 0.00013s] {}
2026-07-11 13:13:52,198 INFO sqlalchemy.engine.Engine
CREATE TABLE courses (
	course_id INTEGER NOT NULL AUTO_INCREMENT,
	course_name VARCHAR(150),
	course_code VARCHAR(20),
	credits INTEGER,
	department_id INTEGER,
	max_set INTEGER,
	max_seats INTEGER,
	PRIMARY KEY (course_id),
	FOREIGN KEY(department_id) REFERENCES departments (department_id)
)


2026-07-11 13:13:52,198 INFO sqlalchemy.engine.Engine [no key 0.00010s] {}
2026-07-11 13:13:52,208 INFO sqlalchemy.engine.Engine CREATE INDEX idx_course_code ON courses (course_code)
2026-07-11 13:13:52,208 INFO sqlalchemy.engine.Engine [no key 0.00016s] {}
2026-07-11 13:13:52,224 INFO sqlalchemy.engine.Engine
CREATE TABLE enrollments (
	enrollment_id INTEGER NOT NULL AUTO_INCREMENT,
	student_id INTEGER,
	course_id INTEGER,
	enrollment_date DATE,
	grade CHAR(2),
	PRIMARY KEY (enrollment_id),
	FOREIGN KEY(student_id) REFERENCES students (student_id),
	FOREIGN KEY(course_id) REFERENCES courses (course_id)
)


2026-07-11 13:13:52,224 INFO sqlalchemy.engine.Engine [no key 0.00011s] {}
2026-07-11 13:13:52,237 INFO sqlalchemy.engine.Engine COMMIT
Tables created
(venv) [sanjai@sanjai handson_6]$
'''