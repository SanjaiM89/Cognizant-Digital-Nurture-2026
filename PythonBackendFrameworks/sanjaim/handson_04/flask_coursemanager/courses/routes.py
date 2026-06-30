from flask import Blueprint, jsonify, request
from courses.models import Course
courses_bp = Blueprint("courses",__name__,url_prefix="/api/courses")

@courses_bp.route('/',methods=['GET'])
def get_courses():
    result = []
    courses = Course.query.all()

    for course in courses:
        result.append({
            "id":course.id,
            "name":course.name,
            "code":course.code,
            "credits":course.credits,
            "department_id":course.department_id
        })
    return jsonify(result)

@courses_bp.route('/',methods=['POST'])
def add_courses():
    data = request.get_json()

    courses = Course(
        name=data["name"],
        code = data["code"],
        credits = data["credits"],
        department_id = data["department_id"]
    )

    db.session.add(courses)
    d.session.commit()
    return jsonify({
        "messeage":"Added Coruses",
    }),201