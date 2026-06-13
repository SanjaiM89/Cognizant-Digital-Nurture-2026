from django.db import models


# Create your models here.
class Department(models.Model):
    name = models.CharField(max_length=30)
    head_of_dept = models.CharField(max_length=10)
    budget = models.DecimalField(max_digits=12, decimal_places=3)

    def __str__(self):
        return self.name


class Course(models.Model):
    name = models.CharField(max_length=30)
    code = models.CharField(max_length=7, unique=True)
    credits = models.PositiveIntegerField()
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Student(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    enrollment_year = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Enrollment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    enrollement_date = models.DateField(auto_now_add=True)
    grade = models.CharField(max_length=2, null=True, blank=True)

    def __str__(self):
        return f"{self.student} {self.course}"
        
    class Meta:
        unique_together = [['student','course']]