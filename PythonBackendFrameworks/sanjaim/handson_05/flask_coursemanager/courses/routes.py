from flask import Blueprint, jsonify, request
from courses.models import db, Course, Enrollment

courses_bp = Blueprint("courses", __name__, url_prefix="/api/courses")


def make_response_json(data, status_code):
    return jsonify({"status": "success", "data": data}), status_code


@courses_bp.route('/', methods=['GET'])
def get_courses():
    courses = Course.query.all()
    return make_response_json([course.to_dict() for course in courses], 200)


@courses_bp.route('/', methods=['POST'])
def add_course():
    data = request.get_json()

    if not data or not all(k in data for k in ("name", "code", "credits")):
        return jsonify({"status": "error", "message": "name, code and credits are required"}), 400

    course = Course(
        name=data["name"],
        code=data["code"],
        credits=data["credits"],
        department_id=data.get("department_id")
    )

    db.session.add(course)
    db.session.commit()
    return make_response_json(course.to_dict(), 201)


@courses_bp.route('/<int:course_id>/', methods=['GET'])
def get_course(course_id):
    course = Course.query.get_or_404(course_id)
    return make_response_json(course.to_dict(), 200)


@courses_bp.route('/<int:course_id>/', methods=['PUT'])
def update_course(course_id):
    course = Course.query.get_or_404(course_id)
    data = request.get_json()
    if not data:
        return jsonify({"status": "error", "message": "request body is required"}), 400

    course.name = data.get("name", course.name)
    course.code = data.get("code", course.code)
    course.credits = data.get("credits", course.credits)
    course.department_id = data.get("department_id", course.department_id)

    db.session.commit()
    return make_response_json(course.to_dict(), 200)


@courses_bp.route('/<int:course_id>/', methods=['DELETE'])
def delete_course(course_id):
    course = Course.query.get_or_404(course_id)
    db.session.delete(course)
    db.session.commit()
    return make_response_json(None, 200)


@courses_bp.route('/<int:course_id>/students/', methods=['GET'])
def get_course_students(course_id):
    course = Course.query.get_or_404(course_id)
    enrollments = Enrollment.query.filter_by(course_id=course.id).all()
    students = [enrollment.student.to_dict() for enrollment in enrollments]
    return make_response_json(students, 200)
