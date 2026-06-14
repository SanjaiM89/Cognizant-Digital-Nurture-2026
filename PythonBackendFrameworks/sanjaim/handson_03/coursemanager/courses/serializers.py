from rest_framework import serializers
from .models import Department, Course, Student, Enrollment

class department_serializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'


class course_serializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'

class student_serializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'

class enrollment_serializer(serializers.ModelSerializer):
    class Meta:
        model = Enrollment
        fields = '__all__'