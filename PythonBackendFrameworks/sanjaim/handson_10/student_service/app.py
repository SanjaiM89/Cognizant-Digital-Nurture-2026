from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
import requests

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = (
    'sqlite:////home/sanjai/Desktop/cognizant/PythonBackendFrameworks/sanjaim/'
    'handson_10/student_service/student_service.sqlite3'
)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

COURSE_SERVICE_URL = 'http://127.0.0.1:5001'


class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)

    def to_dict(self):
        return {'id': self.id, 'name': self.name, 'email': self.email}


class Enrollment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey('student.id'), nullable=False)
    course_id = db.Column(db.Integer, nullable=False)

    def to_dict(self):
        return {'id': self.id, 'student_id': self.student_id, 'course_id': self.course_id}


with app.app_context():
    db.create_all()


@app.route('/api/students/', methods=['GET'])
def list_students():
    students = Student.query.all()
    return jsonify([student.to_dict() for student in students])


@app.route('/api/students/', methods=['POST'])
def create_student():
    data = request.get_json()
    student = Student(name=data['name'], email=data['email'])
    db.session.add(student)
    db.session.commit()
    return jsonify(student.to_dict()), 201


@app.route('/api/students/<int:student_id>/', methods=['GET'])
def get_student(student_id):
    student = Student.query.get(student_id)
    if not student:
        return jsonify({'error': 'Student not found'}), 404
    return jsonify(student.to_dict())


@app.route('/api/students/<int:student_id>/enroll', methods=['POST'])
def enroll_student(student_id):
    student = Student.query.get(student_id)
    if not student:
        return jsonify({'error': 'Student not found'}), 404

    data = request.get_json()
    course_id = data.get('course_id')

    # Student Service does not own course data, so it verifies the course
    # exists by calling Course Service over HTTP rather than querying its
    # database directly - that's the core microservices rule (each service
    # owns its own data).
    try:
        response = requests.get(f'{COURSE_SERVICE_URL}/api/courses/{course_id}/', timeout=3)
    except requests.exceptions.ConnectionError:
        return jsonify({'error': 'Course Service is unavailable'}), 503

    if response.status_code == 404:
        return jsonify({'error': 'Course not found'}), 404

    enrollment = Enrollment(student_id=student_id, course_id=course_id)
    db.session.add(enrollment)
    db.session.commit()
    return jsonify(enrollment.to_dict()), 201


if __name__ == '__main__':
    app.run(port=5002)
