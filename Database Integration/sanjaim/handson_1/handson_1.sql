#  Task 1: Create the Database and Tables
create table students (
student_id int primary key auto_increment,
first_name varchar(50) not null,
last_name varchar(50) not null,
email varchar(100) unique not null,
date_of_birth date,
department_id int,
enrollment_year int,
foreign key(department_id) references departments(department_id)
);

create table departments(
department_id int primary key auto_increment,
dept_name varchar(100) not null,
hod_name varchar(100),
budget decimal(12,2)
);

create table courses(
course_id int primary key auto_increment,
course_name varchar(150),
course_code varchar(20),
credits int,
department_id int,
foreign key(department_id) references departments(department_id)
);


create table enrollments (
enrollment_id int primary key auto_increment,
student_id int,
foreign key(student_id) references students(student_id),
course_id int,
foreign key(course_id) references courses(course_id),
enrollment_date date,
grade char(2) 
);

create table professors(
professor_id int primary key auto_increment,
prof_name varchar(100) not null,
email varchar(100) unique,
department_id int,
foreign key(department_id) references departments(department_id),
salary decimal(10,2)
)


describe courses;
describe departments;
describe students;
describe professors;
describe enrollments;

/*
Task 2: Verify Normalisation
1NF:-
-> It doesn’t needs a ordered data i.e every column needs to have one atomic value
-> Every table needs to have primary key
-> Repeating or the duplication is not allowed
-> Mixing data types in the same column is not allowed
If the multiple phone number is stored in one filed it would violate the 1NF rules of every column having atomic values.
All the tables satisfy the 1NF Rules
    - All the tables courses, departments, enrollments,professors and students has primary key
    - And no columns in table stored multiple values in same column every column has atomic vlaues

2NF:-
-> The tables must satisfy the 1NF condition
-> Every non key attributes must depend on the primary key column
-> Partial Dependency is not allowed
In the enrollment table enrollment_date and grade depend on the enrollment of a student in a course. They do not depend only on student_id or only on course_id so enrollment table satisfies 2NF
    - There is primary key in columns in enrollment_id
    - All columns student_id, course_id, enrollment_date and grade are depend on the primary key
    enrollment_id
    - There is no partial dependency all the columns are dependened on the student_id column

3NF:-
-> It must satisfy 2NF condition
-> There should be no dependency between non key attributes
-> Non key attributes should only depend only on primary key

The schema violates 3NF

In Student Table, student_id is the primaru key and department name is depends on the department_id which is not primary key in student table
Storing department name in student table will violate the 3NF rules
*/

/*
 Task 3: Alter and Extend the Schema


*/