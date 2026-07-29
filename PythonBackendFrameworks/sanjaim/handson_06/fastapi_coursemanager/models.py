from sqlalchemy import Column, Integer, String, Numeric, ForeignKey, Date, UniqueConstraint
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from database import Base


class Department(Base):
    __tablename__ = "departments"

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False, unique=True)
    head_of_dept = Column(String(100), nullable=False)
    budget = Column(Numeric(precision=18, scale=3), nullable=False)

    courses = relationship("Course", back_populates="department")


class Course(Base):
    __tablename__ = "courses"

    id = Column(Integer, primary_key=True)
    name = Column(String(30))
    code = Column(String(7), unique=True)
    credits = Column(Integer)
    department_id = Column(Integer, ForeignKey("departments.id"))

    department = relationship("Department", back_populates="courses")


class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True)
    first_name = Column(String(30), nullable=False)
    last_name = Column(String(30), nullable=False)
    email = Column(String(100), nullable=False, unique=True)
    department_id = Column(Integer, ForeignKey("departments.id"))
    enrollment_year = Column(Integer, nullable=False)


class Enrollment(Base):
    __tablename__ = "enrollments"
    __table_args__ = (UniqueConstraint("student_id", "course_id"),)

    id = Column(Integer, primary_key=True)
    student_id = Column(Integer, ForeignKey("students.id"))
    course_id = Column(Integer, ForeignKey("courses.id"))
    enrollment_date = Column(Date, server_default=func.current_date())
    grade = Column(String(2), nullable=True)

    student = relationship("Student")
    course = relationship("Course")
