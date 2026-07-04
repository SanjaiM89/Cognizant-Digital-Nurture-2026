#Task 1: Insert, Update and Delete Data

-- departments
INSERT INTO departments (dept_name, hod_name, budget) VALUES
('Computer Science', 'Dr. Ramesh Kumar', 850000.00),
('Electronics', 'Dr. Priya Nair', 620000.00),
('Mechanical', 'Dr. Suresh Iyer', 540000.00),
('Civil', 'Dr. Ananya Sharma', 430000.00);
-- students
INSERT INTO students (first_name, last_name, email, date_of_birth, department_id,
enrollment_year) VALUES
('Arjun', 'Mehta', 'arjun.mehta@college.edu', '2003-04-12', 1, 2022),
('Priya', 'Suresh', 'priya.suresh@college.edu', '2003-07-25', 1, 2022),
('Rohan', 'Verma', 'rohan.verma@college.edu', '2002-11-08', 2, 2021),
('Sneha', 'Patel', 'sneha.patel@college.edu', '2004-01-30', 3, 2023),
('Vikram', 'Das', 'vikram.das@college.edu', '2003-09-14', 1, 2022),
('Kavya', 'Menon', 'kavya.menon@college.edu', '2002-05-17', 2, 2021),
('Aditya', 'Singh', 'aditya.singh@college.edu', '2004-03-22', 4, 2023),
('Deepika','Rao', 'deepika.rao@college.edu', '2003-08-09', 1, 2022);
-- courses
INSERT INTO courses (course_name, course_code, credits, department_id) VALUES
('Data Structures & Algorithms', 'CS101', 4, 1),
('Database Management Systems', 'CS102', 3, 1),
('Object Oriented Programming', 'CS103', 4, 1),
('Circuit Theory', 'EC101', 3, 2),
('Thermodynamics', 'ME101', 3, 3);
-- enrollments
INSERT INTO enrollments (student_id, course_id, enrollment_date, grade) VALUES
(1, 1, '2022-07-01', 'A'), (1, 2, '2022-07-01', 'B'),
(2, 1, '2022-07-01', 'B'), (2, 3, '2022-07-01', 'A'),
(3, 4, '2021-07-01', 'A'), (4, 5, '2023-07-01', NULL),
(5, 1, '2022-07-01', 'C'), (5, 2, '2022-07-01', 'A'),
(6, 4, '2021-07-01', 'B'), (7, 5, '2023-07-01', NULL),
(8, 1, '2022-07-01', 'A'), (8, 3, '2022-07-01', 'B');

-- professors
INSERT INTO professors (prof_name, email, department_id, salary) VALUES
('Dr. Anand Krishnan', 'anand.k@college.edu', 1, 95000.00),
('Dr. Meena Pillai', 'meena.p@college.edu', 1, 88000.00),
('Dr. Sunil Rajan', 'sunil.r@college.edu', 2, 82000.00),
('Dr. Latha Gopal', 'latha.g@college.edu', 3, 79000.00),
('Dr. Kartik Bose', 'kartik.b@college.edu', 4, 76000.00);

select count(*) from students;

insert into students (first_name, last_name,email, date_of_birth, department_id, enrollment_year) values 
('Sanjai','M','sanjaim899@gmail.com','2005-08-29','1',2023),
('san','S','san@gmail.com','2005-08-20','1',2024);

select count(*) from students;


update enrollments set grade = 'B' where student_id=5 and course_id=1;

select count(*) from enrollments;

delete from enrollments where grade is null;

select count(*) from enrollments;


#Task 2: Single-Table Queries and Filtering

select * from students where enrollment_year=2022 order by last_name asc;
/*
mysql> select * from students where enrollment_year=2022 order by last_name asc;
+------------+------------+-----------+--------------------------+---------------+---------------+-----------------+
| student_id | first_name | last_name | email                    | date_of_birth | department_id | enrollment_year |
+------------+------------+-----------+--------------------------+---------------+---------------+-----------------+
|          5 | Vikram     | Das       | vikram.das@college.edu   | 2003-09-14    |             1 |            2022 |
|          1 | Arjun      | Mehta     | arjun.mehta@college.edu  | 2003-04-12    |             1 |            2022 |
|          8 | Deepika    | Rao       | deepika.rao@college.edu  | 2003-08-09    |             1 |            2022 |
|          2 | Priya      | Suresh    | priya.suresh@college.edu | 2003-07-25    |             1 |            2022 |
+------------+------------+-----------+--------------------------+---------------+---------------+-----------------+
4 rows in set (0.000 sec)

mysql> 

*/

# Find all courses with more than 3 credits, sorted by credits descending.
select * from courses where credits=3 order by credits desc;

/*

mysql> select * from courses where credits=3 order by credits desc
    -> ;
+-----------+-----------------------------+-------------+---------+---------------+---------+-----------+
| course_id | course_name                 | course_code | credits | department_id | max_set | max_seats |
+-----------+-----------------------------+-------------+---------+---------------+---------+-----------+
|         2 | Database Management Systems | CS102       |       3 |             1 |      60 |        60 |
|         4 | Circuit Theory              | EC101       |       3 |             2 |      60 |        60 |
|         5 | Thermodynamics              | ME101       |       3 |             3 |      60 |        60 |
+-----------+-----------------------------+-------------+---------+---------------+---------+-----------+
3 rows in set (0.000 sec)

mysql> 
*/

# 22. List all professors whose salary is between 80,000 and 95,000

select * from professors where salary between 80000 and 95000;

/*
mysql> select * from professors where salary between 80000 and 95000;
+--------------+--------------------+---------------------+---------------+----------+
| professor_id | prof_name          | email               | department_id | salary   |
+--------------+--------------------+---------------------+---------------+----------+
|            1 | Dr. Anand Krishnan | anand.k@college.edu |             1 | 95000.00 |
|            2 | Dr. Meena Pillai   | meena.p@college.edu |             1 | 88000.00 |
|            3 | Dr. Sunil Rajan    | sunil.r@college.edu |             2 | 82000.00 |
+--------------+--------------------+---------------------+---------------+----------+
3 rows in set (0.000 sec)
*/

# 23. Find all students whose email ends with '@college.edu' using the LIKE operator.

select * from students where email like '%@college.edu';

/*

mysql> select * from students where email like '%@college.edu';
+------------+------------+-----------+--------------------------+---------------+---------------+-----------------+
| student_id | first_name | last_name | email                    | date_of_birth | department_id | enrollment_year |
+------------+------------+-----------+--------------------------+---------------+---------------+-----------------+
|          1 | Arjun      | Mehta     | arjun.mehta@college.edu  | 2003-04-12    |             1 |            2022 |
|          2 | Priya      | Suresh    | priya.suresh@college.edu | 2003-07-25    |             1 |            2022 |
|          3 | Rohan      | Verma     | rohan.verma@college.edu  | 2002-11-08    |             2 |            2021 |
|          4 | Sneha      | Patel     | sneha.patel@college.edu  | 2004-01-30    |             3 |            2023 |
|          5 | Vikram     | Das       | vikram.das@college.edu   | 2003-09-14    |             1 |            2022 |
|          6 | Kavya      | Menon     | kavya.menon@college.edu  | 2002-05-17    |             2 |            2021 |
|          7 | Aditya     | Singh     | aditya.singh@college.edu | 2004-03-22    |             4 |            2023 |
|          8 | Deepika    | Rao       | deepika.rao@college.edu  | 2003-08-09    |             1 |            2022 |
+------------+------------+-----------+--------------------------+---------------+---------------+-----------------+
8 rows in set (0.000 sec)

mysql> 

*/

# 24. Count the total number of students per enrollment_yea

select enrollment_year, count(*) as totalStudents from students group by enrollment_year;

/*
mysql> select enrollment_year, count(*) as totalStudents from students group by enrollment_year;
+-----------------+---------------+
| enrollment_year | totalStudents |
+-----------------+---------------+
|            2022 |             4 |
|            2021 |             2 |
|            2023 |             3 |
|            2024 |             1 |
+-----------------+---------------+
4 rows in set (0.006 sec)

mysql> 

*/


# Task 3: Multi-Table Joins

#25. List each student's full name (first_name + ' ' + last_name) alongside the name of their department. (JOIN students and departments.)

select concat(students.first_name,' ',students.last_name) as full_name, departments.dept_name from students inner join departments on students.department_id=departments.department_id;

/*
mysql> select concat(students.first_name,' ',students.last_name) as full_name, departments.dept_name from students inner join departments on students.department_id=departments.department_id;
+--------------+------------------+
| full_name    | dept_name        |
+--------------+------------------+
| Arjun Mehta  | Computer Science |
| Priya Suresh | Computer Science |
| Rohan Verma  | Electronics      |
| Sneha Patel  | Mechanical       |
| Vikram Das   | Computer Science |
| Kavya Menon  | Electronics      |
| Aditya Singh | Civil            |
| Deepika Rao  | Computer Science |
| Sanjai M     | Computer Science |
| san S        | Computer Science |
+--------------+------------------+
10 rows in set (0.004 sec)

mysql> 


*/


#26. Show each enrollment along with the student's name and the course name. (3-table JOIN: enrollments, students, courses.)

select concat(students.first_name,students.last_name), courses.course_name from enrollments inner join students on students.student_id = enrollments.student_id inner join
courses on courses.course_id=enrollments.course_id;

/*

mysql> select concat(students.first_name,students.last_name), courses.course_name from enrollments inner join students on students.student_id = enrollments.student_id inner join
    -> courses on courses.course_id=enrollments.course_id;
+------------------------------------------------+------------------------------+
| concat(students.first_name,students.last_name) | course_name                  |
+------------------------------------------------+------------------------------+
| ArjunMehta                                     | Data Structures & Algorithms |
| ArjunMehta                                     | Database Management Systems  |
| PriyaSuresh                                    | Data Structures & Algorithms |
| PriyaSuresh                                    | Object Oriented Programming  |
| RohanVerma                                     | Circuit Theory               |
| VikramDas                                      | Data Structures & Algorithms |
| VikramDas                                      | Database Management Systems  |
| KavyaMenon                                     | Circuit Theory               |
| DeepikaRao                                     | Data Structures & Algorithms |
| DeepikaRao                                     | Object Oriented Programming  |
+------------------------------------------------+------------------------------+
10 rows in set (0.006 sec)

mysql> 

*/

# 27. Find all students who are NOT enrolled in any course using a LEFT JOIN and WHERE ... IS NULL pattern.

select concat(students.first_name,students.last_name) as name from students left join enrollments on students.student_id = enrollments.student_id where enrollments.student_id is null;

/*

mysql> select concat(students.first_name,students.last_name) as name from students left join enrollments on students.student_id = enrollments.student_id where enrollments.student_id is null;
+-------------+
| name        |
+-------------+
| SnehaPatel  |
| AdityaSingh |
| SanjaiM     |
| sanS        |
+-------------+
4 rows in set (0.000 sec)

mysql> 

*/

#28. Display every course along with the number of students enrolled in it. Courses with zero enrolments must still appear. (LEFT JOIN courses with enrollments, GROUP BY course.)

select courses.course_name, count(enrollments.student_id) as student_count from courses left join enrollments on enrollments.course_id=courses.course_id
group by courses.course_id;

/*
mysql> select courses.course_name, count(enrollments.student_id) as student_count from courses left join enrollments on enrollments.course_id=courses.course_id
    -> group by courses.course_id;
+------------------------------+---------------+
| course_name                  | student_count |
+------------------------------+---------------+
| Data Structures & Algorithms |             4 |
| Database Management Systems  |             2 |
| Object Oriented Programming  |             2 |
| Circuit Theory               |             2 |
| Thermodynamics               |             0 |
+------------------------------+---------------+
5 rows in set (0.022 sec)

mysql> 

*/

# 29. List each department along with its professors and their salaries. Include departments that have no professors yet.

select professors.prof_name,departments.dept_name, professors.salary from departments left join professors on departments.department_id = professors.department_id;

/*
mysql> select professors.prof_name,departments.dept_name, professors.salary from departments left join professors on departments.department_id = professors.department_id;
+--------------------+------------------+----------+
| prof_name          | dept_name        | salary   |
+--------------------+------------------+----------+
| Dr. Anand Krishnan | Computer Science | 95000.00 |
| Dr. Meena Pillai   | Computer Science | 88000.00 |
| Dr. Sunil Rajan    | Electronics      | 82000.00 |
| Dr. Latha Gopal    | Mechanical       | 79000.00 |
| Dr. Kartik Bose    | Civil            | 76000.00 |
| NULL               | Computer Science |     NULL |
| NULL               | Electronics      |     NULL |
| NULL               | Mechanical       |     NULL |
| NULL               | Civil            |     NULL |
+--------------------+------------------+----------+
9 rows in set (0.005 sec)

mysql> 

*/

# Task 4: Aggregations and Grouping

# 30. Calculate the total number of enrollments per course. Display course_name and enrollment_count.

select courses.course_name, count(enrollments.student_id) as enrollement_per_course from courses left join enrollments on enrollments.course_id = courses.course_id group by courses.course_id;

/*

mysql> select courses.course_name, count(enrollments.student_id) as enrollement_per_course from courses left join enrollments on enrollments.course_id = courses.course_id group by courses.course_id;
+------------------------------+------------------------+
| course_name                  | enrollement_per_course |
+------------------------------+------------------------+
| Data Structures & Algorithms |                      4 |
| Database Management Systems  |                      2 |
| Object Oriented Programming  |                      2 |
| Circuit Theory               |                      2 |
| Thermodynamics               |                      0 |
+------------------------------+------------------------+
5 rows in set (0.000 sec)

mysql> 

*/

# 31. Find the average salary of professors per department. Round to 2 decimal places.

select departments.dept_name, round(avg(professors.salary),2) as Average_Salary from departments left join professors on professors.department_id = departments.department_id group by departments.department_id;

/*

mysql> select departments.dept_name, round(avg(professors.salary),2) as Average_Salary from departments left join professors on professors.department_id = departments.department_id group by departments.department_id;
+------------------+----------------+
| dept_name        | Average_Salary |
+------------------+----------------+
| Computer Science |       91500.00 |
| Electronics      |       82000.00 |
| Mechanical       |       79000.00 |
| Civil            |       76000.00 |
| Computer Science |           NULL |
| Electronics      |           NULL |
| Mechanical       |           NULL |
| Civil            |           NULL |
+------------------+----------------+
8 rows in set (0.000 sec)

mysql> 

*/

# 32. Find all departments where the total budget exceeds 600,000

select departments.dept_name from departments where budget>600000;

/*
mysql> select departments.dept_name from departments where budget>600000;
+------------------+
| dept_name        |
+------------------+
| Computer Science |
| Electronics      |
| Computer Science |
| Electronics      |
+------------------+
4 rows in set (0.000 sec)

mysql> 

*/

# 33. Show the grade distribution for course CS101: count of each grade (A, B, C, D, F).

select grade, count(enrollments.student_id) as count_of_grade from enrollments left join courses on enrollments.course_id=courses.course_id group by grade;

/*
mysql> select * from enrollments;
+---------------+------------+-----------+-----------------+-------+
| enrollment_id | student_id | course_id | enrollment_date | grade |
+---------------+------------+-----------+-----------------+-------+
|             1 |          1 |         1 | 2022-07-01      | A     |
|             2 |          1 |         2 | 2022-07-01      | B     |
|             3 |          2 |         1 | 2022-07-01      | B     |
|             4 |          2 |         3 | 2022-07-01      | A     |
|             5 |          3 |         4 | 2021-07-01      | A     |
|             7 |          5 |         1 | 2022-07-01      | B     |
|             8 |          5 |         2 | 2022-07-01      | A     |
|             9 |          6 |         4 | 2021-07-01      | B     |
|            11 |          8 |         1 | 2022-07-01      | A     |
|            12 |          8 |         3 | 2022-07-01      | B     |
+---------------+------------+-----------+-----------------+-------+
10 rows in set (0.000 sec)

mysql> select grade, count(enrollments.student_id) as count_of_grade from enrollments left join courses on enrollments.course_id=courses.course_id group by grade;
+-------+----------------+
| grade | count_of_grade |
+-------+----------------+
| A     |              5 |
| B     |              5 |
+-------+----------------+
2 rows in set (0.000 sec)

mysql> 


*/

# 34. Using HAVING, list departments where more than 2 students are enrolled across all courses in that department.

select departments.dept_name from departments inner join courses on departments.department_id = courses.department_id inner join
enrollments on courses.course_id = enrollments.course_id group by departments.department_id having count(enrollments.student_id)>2;

/*
mysql> select departments.dept_name from departments inner join courses on departments.department_id = courses.department_id inner join
    -> enrollments on courses.course_id = enrollments.course_id group by departments.department_id having count(enrollments.student_id)>2;
+------------------+
| dept_name        |
+------------------+
| Computer Science |
+------------------+
1 row in set (0.004 sec)

mysql> 

*/