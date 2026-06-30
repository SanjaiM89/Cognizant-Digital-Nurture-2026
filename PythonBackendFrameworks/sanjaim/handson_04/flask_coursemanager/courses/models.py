from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Department(db.Model):
    __tablename__ = "departments"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, unique=True)
    head_of_dept = db.Column(db.String(100), nullable=False)
    budget = db.Column(db.Numeric(precision=18, scale=3), nullable=False)

    def __str__(self):
        return self.name


class Course(db.Model):
    __tablename__ = "courses_course"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30))
    code = db.Column(db.String(7), unique=True)
    credits = db.Column(db.Integer)
    department_id = db.Column(db.Integer, db.ForeignKey("department.id"))
