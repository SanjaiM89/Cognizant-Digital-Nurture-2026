#Task 2: Django ORM Queries

#16) Open the Django shell with python manage.py shell. Create at least 2 Department, 4 Course, and 5 Student objects using Model.objects.create(...).

"""
bash: cd: saa: No such file or directory
(venv) [sanjai@sanjai PythonBackendFrameworks]$ cd sanjaim/
(venv) [sanjai@sanjai sanjaim]$ ls
handson_01  handson_02
(venv) [sanjai@sanjai sanjaim]$ cd handson_02
(venv) [sanjai@sanjai handson_02]$ ls
coursemanager
(venv) [sanjai@sanjai handson_02]$ cd coursemanager/
(venv) [sanjai@sanjai coursemanager]$ ls
coursemanager  courses  db.sqlite3  manage.py
(venv) [sanjai@sanjai coursemanager]$ python manage.py shell
\16 objects imported automatically (use -v 2 for details).

Python 3.14.5 (main, May 10 2026, 18:26:20) [GCC 16.1.1 20260430] on linux
Type "help", "copyright", "credits" or "license" for more information.
(InteractiveConsole)

>>> from courses.models import Department,Course,Student,Enrollment
>>> d1 = Department.objects.create(name="Cse",head_of_dept="abg",budget="1000000.000")
>>> d2 = Department.objects.create(name="It",head_of_dept="efg",budget="900000.000")
>>> Course.objects.create(name="TOC",code="CS22301",credits=3,department=d1)
<Course: TOC>
>>> Course.objects.create(name="Compiler",code="CS22602",credits=3,department=d1)
<Course: Compiler>
>>> Course.objects.create(name="Software Engineering",code="IT12602",credits=3,department=d2)
<Course: Software Engineering>
>>> Course.objects.create(name="IOT",code="IT13602",credits=3,department=d2)
<Course: IOT>
>>> Student.objects.create(first_name="sanjai",last_name="m",email="sanjaim@myyahoo.com",department=d1,enrollment_year=2026)
<Student: sanjai m>
>>> Student.objects.create(first_name="san",last_name="m",email="sanm@myyahoo.com",department=d1,enrollment_year=2026)
<Student: san m>
>>> Student.objects.create(first_name="tanish",last_name="m",email="tanish@gmail.com",department=d2,enrollment_year=2026)
<Student: tanish m>
>>> Student.objects.create(first_name="vasanth",last_name="v",email="vasanth@gmail.com",department=d1,enrollment_year=2026)
<Student: vasanth v>
>>> Student.objects.create(first_name="prince",last_name="r",email="princer@gmail.com",department=d2,enrollment_year=2026)
<Student: prince r>
>>>
"""

#17) Query all courses in a specific department using Course.objects.filter(department__name='Computer Science'). Note the double underscore — this is a Django ORM lookup across a ForeignKey.
# 
"""
>>> Course.objects.filter(department__name="Cse")
<QuerySet [<Course: TOC>, <Course: Compiler>]>
>>>
 
"""

#18) Use .values() and .annotate() to count the number of courses per department: Department.objects.annotate(course_count=Count('course')).
"""
>>> from django.db.models import Count
>>> Department.objects.annotate(course_count=Count('course'))
<QuerySet [<Department: Cse>, <Department: It>]>
>>> Department.objects.values('name').annotate(course_count=Count('course'))
<QuerySet [{'name': 'Cse', 'course_count': 2}, {'name': 'It', 'course_count': 2}]>
>>>
"""

#19) Use select_related to fetch all students along with their department in a single SQL query. Confirm with Django's connection.queries log.

"""
>>> student = Student.objects.select_related("department")
>>> for i in student:
...     print(f"{i.first_name} {i.last_name} Department - {i.department}")
...
sanjai m Department - Cse
san m Department - Cse
tanish m Department - It
vasanth v Department - Cse
prince r Department - It
>>>
"""

#20. Perform an update: increase the budget of all departments by 10% using Department.objects.update(budget=F('budget') * 1.1).

"""
>>> from django.db.models import F
>>> Department.objects.update(budget=F('budget') * 1.1)
2
>>>
"""