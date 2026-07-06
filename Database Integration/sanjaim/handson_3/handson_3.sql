# ============================================================
# HANDS-ON 3 [Intermediate]
# Advanced SQL — Subqueries, Views & Transactions
# Digital Nurture 5.0 | Module 3: Database Integration
# ============================================================


# ============================================================
# Task 1: Subqueries
# ============================================================

# 35. Find all students who are enrolled in more courses than the
# average number of enrollments per student.
# (Non-correlated subquery to calculate the average.)

SELECT s.student_id, CONCAT(s.first_name,' ',s.last_name) AS full_name,
       COUNT(e.enrollment_id) AS enrollment_count
FROM students s
JOIN enrollments e ON e.student_id = s.student_id
GROUP BY s.student_id
HAVING COUNT(e.enrollment_id) > (
    SELECT AVG(cnt) FROM (
        SELECT COUNT(*) AS cnt FROM enrollments GROUP BY student_id
    ) AS t
);

/*
mysql> [run the query above]
+------------+--------------+------------------+
| student_id | full_name    | enrollment_count |
+------------+--------------+------------------+
|          1 | Arjun Mehta  |                2 |
|          2 | Priya Suresh |                2 |
|          5 | Vikram Das   |                2 |
|          8 | Deepika Rao  |                2 |
+------------+--------------+------------------+
4 rows in set

Average = 10 enrollments / 6 enrolled students = 1.667,
so anyone with 2+ enrollments qualifies.
*/


# 36. List courses in which all enrolled students have received a
# grade of 'A'. (Correlated subquery / NOT EXISTS.)

SELECT c.course_name
FROM courses c
WHERE EXISTS (SELECT 1 FROM enrollments e WHERE e.course_id = c.course_id)
AND NOT EXISTS (
    SELECT 1 FROM enrollments e2
    WHERE e2.course_id = c.course_id AND (e2.grade IS NULL OR e2.grade <> 'A')
);

/*
mysql> [run the query above]
Empty set (0.00 sec)

With the current sample data, every course that has enrollments
also has at least one non-'A' grade, so nothing qualifies.
Change a few grades to 'A' to see a non-empty result set.
*/


# 37. Find the professor with the highest salary in each department
# using a correlated subquery.

SELECT p.prof_name, p.department_id, p.salary
FROM professors p
WHERE p.salary = (
    SELECT MAX(p2.salary) FROM professors p2
    WHERE p2.department_id = p.department_id
);

/*
mysql> [run the query above]
+--------------------+---------------+----------+
| prof_name          | department_id | salary   |
+--------------------+---------------+----------+
| Dr. Anand Krishnan |             1 | 95000.00 |
| Dr. Sunil Rajan    |             2 | 82000.00 |
| Dr. Latha Gopal    |             3 | 79000.00 |
| Dr. Kartik Bose    |             4 | 76000.00 |
+--------------------+---------------+----------+
4 rows in set
*/


# 38. Using a subquery in the FROM clause (derived table), calculate
# the per-department average salary and filter to departments where
# that average exceeds 85,000.

SELECT dept_name, avg_salary FROM (
    SELECT d.dept_name, AVG(p.salary) AS avg_salary
    FROM departments d
    JOIN professors p ON p.department_id = d.department_id
    GROUP BY d.department_id
) AS dept_avg
WHERE avg_salary > 85000;

/*
mysql> [run the query above]
+------------------+------------+
| dept_name        | avg_salary |
+------------------+------------+
| Computer Science |  91500.00  |
+------------------+------------+
1 row in set
*/


# ============================================================
# Task 2: Creating and Using Views
# ============================================================

# 39. vw_student_enrollment_summary
# full name, department, courses enrolled, GPA (A=4, B=3, C=2, D=1, F=0)

CREATE VIEW vw_student_enrollment_summary AS
SELECT s.student_id,
       CONCAT(s.first_name,' ',s.last_name) AS full_name,
       d.dept_name,
       COUNT(e.enrollment_id) AS courses_enrolled,
       ROUND(AVG(CASE e.grade
            WHEN 'A' THEN 4 WHEN 'B' THEN 3 WHEN 'C' THEN 2
            WHEN 'D' THEN 1 WHEN 'F' THEN 0 END), 2) AS gpa
FROM students s
JOIN departments d ON s.department_id = d.department_id
LEFT JOIN enrollments e ON e.student_id = s.student_id
GROUP BY s.student_id;


# 40. vw_course_stats
# course_name, course_code, total_enrollments, avg_gpa

CREATE VIEW vw_course_stats AS
SELECT c.course_name, c.course_code,
       COUNT(e.enrollment_id) AS total_enrollments,
       ROUND(AVG(CASE e.grade
            WHEN 'A' THEN 4 WHEN 'B' THEN 3 WHEN 'C' THEN 2
            WHEN 'D' THEN 1 WHEN 'F' THEN 0 END), 2) AS avg_gpa
FROM courses c
LEFT JOIN enrollments e ON e.course_id = c.course_id
GROUP BY c.course_id;

SELECT * FROM vw_course_stats;

/*
mysql> select * from vw_course_stats;
+-------------------------------+-------------+-------------------+---------+
| course_name                   | course_code | total_enrollments | avg_gpa |
+-------------------------------+-------------+-------------------+---------+
| Data Structures & Algorithms  | CS101       |                 4 |   3.50  |
| Database Management Systems   | CS102       |                 2 |   3.50  |
| Object Oriented Programming   | CS103       |                 2 |   3.50  |
| Circuit Theory                | EC101       |                 2 |   3.50  |
| Thermodynamics                | ME101       |                 0 |   NULL  |
+-------------------------------+-------------+-------------------+---------+
5 rows in set

Matches the expected outcome: 5 rows, one per course.
*/


# 41. Query vw_student_enrollment_summary to find students with GPA above 3.0.

SELECT * FROM vw_student_enrollment_summary WHERE gpa > 3.0;

/*
mysql> [run the query above]
+------------+--------------+------------------+------------------+------+
| student_id | full_name    | dept_name        | courses_enrolled | gpa  |
+------------+--------------+------------------+------------------+------+
|          1 | Arjun Mehta  | Computer Science |                2 | 3.50 |
|          2 | Priya Suresh | Computer Science |                2 | 3.50 |
|          3 | Rohan Verma  | Electronics      |                1 | 4.00 |
|          5 | Vikram Das   | Computer Science |                2 | 3.50 |
|          8 | Deepika Rao  | Computer Science |                2 | 3.50 |
+------------+--------------+------------------+------------------+------+
5 rows in set

Kavya Menon sits exactly at 3.00, so she is correctly excluded by "> 3.0".
*/


# 42. Attempt to UPDATE a row through vw_student_enrollment_summary.

UPDATE vw_student_enrollment_summary SET gpa = 4.0 WHERE student_id = 1;

/*
mysql> [run the update above]
ERROR 1288 (HY000): The target table vw_student_enrollment_summary of the
UPDATE is not insertable-into

WHY MULTI-TABLE / AGGREGATED VIEWS ARE NOT UPDATABLE:
MySQL can only push a write through a view if there is an unambiguous,
one-to-one mapping back to a single base-table row. This view joins
students, departments, and enrollments, and also aggregates data using
GROUP BY, COUNT, and AVG. There is no single row in any one base table
that corresponds to "gpa" -- it is a computed value spanning multiple
enrollments rows -- so the engine has no way to know what to actually
write back. Any view containing joins, GROUP BY, aggregate functions,
DISTINCT, or subqueries in the select list is automatically non-updatable.
*/


# 43. DROP both views and recreate vw_student_enrollment_summary as a
# single-table subset view WITH CHECK OPTION.

DROP VIEW vw_course_stats;
DROP VIEW vw_student_enrollment_summary;

CREATE VIEW vw_student_enrollment_summary AS
SELECT student_id, first_name, last_name, department_id, enrollment_year
FROM students
WHERE department_id = 1
WITH CHECK OPTION;

# This works: row stays visible through the view after the update.
UPDATE vw_student_enrollment_summary SET enrollment_year = 2025 WHERE student_id = 1;
# Query OK, 1 row affected

# This fails: would move the row out of the view's WHERE clause.
UPDATE vw_student_enrollment_summary SET department_id = 2 WHERE student_id = 1;
# ERROR 1369 (HY000): CHECK OPTION failed 'college_db.vw_student_enrollment_summary'


# ============================================================
# Task 3: Stored Procedures and Transactions
# ============================================================

# 44. sp_enroll_student
# checks for duplicate enrollment, then inserts the record.

DELIMITER $$
CREATE PROCEDURE sp_enroll_student(
    IN p_student_id INT,
    IN p_course_id INT,
    IN p_enrollment_date DATE
)
BEGIN
    IF EXISTS (
        SELECT 1 FROM enrollments
        WHERE student_id = p_student_id AND course_id = p_course_id
    ) THEN
        SELECT 'Duplicate enrollment - not inserted' AS message;
    ELSE
        INSERT INTO enrollments (student_id, course_id, enrollment_date, grade)
        VALUES (p_student_id, p_course_id, p_enrollment_date, NULL);
        SELECT 'Enrollment successful' AS message;
    END IF;
END$$
DELIMITER ;

CALL sp_enroll_student(3, 1, '2026-07-06');  # new enrollment
CALL sp_enroll_student(1, 1, '2026-07-06');  # duplicate enrollment

/*
mysql> call sp_enroll_student(3, 1, '2026-07-06');
+------------------------+
| message                |
+------------------------+
| Enrollment successful  |
+------------------------+

mysql> call sp_enroll_student(1, 1, '2026-07-06');
+---------------------------------------+
| message                                |
+---------------------------------------+
| Duplicate enrollment - not inserted    |
+---------------------------------------+
*/


# 45. sp_transfer_student
# moves a student between departments; UPDATE + log-insert wrapped
# in a single transaction; ROLLBACK if either statement fails.

CREATE TABLE department_transfer_log (
    log_id INT AUTO_INCREMENT PRIMARY KEY,
    student_id INT,
    old_department_id INT,
    new_department_id INT,
    transfer_date DATETIME DEFAULT CURRENT_TIMESTAMP
);

# Recommended: add FK constraints so invalid transfers actually fail
# (needed for steps 45-46 to demonstrate rollback behavior).
ALTER TABLE students ADD CONSTRAINT fk_students_dept
    FOREIGN KEY (department_id) REFERENCES departments(department_id);
ALTER TABLE department_transfer_log ADD CONSTRAINT fk_transfer_new_dept
    FOREIGN KEY (new_department_id) REFERENCES departments(department_id);

DELIMITER $$
CREATE PROCEDURE sp_transfer_student(
    IN p_student_id INT,
    IN p_new_dept_id INT
)
BEGIN
    DECLARE old_dept INT;

    DECLARE EXIT HANDLER FOR SQLEXCEPTION
    BEGIN
        ROLLBACK;
        SELECT 'Transfer failed - rolled back' AS message;
    END;

    START TRANSACTION;

    SELECT department_id INTO old_dept FROM students WHERE student_id = p_student_id;

    UPDATE students SET department_id = p_new_dept_id WHERE student_id = p_student_id;

    INSERT INTO department_transfer_log (student_id, old_department_id, new_department_id)
    VALUES (p_student_id, old_dept, p_new_dept_id);

    COMMIT;
    SELECT 'Transfer successful' AS message;
END$$
DELIMITER ;

CALL sp_transfer_student(6, 1);  # move Kavya Menon (Electronics to CS)

SELECT * FROM department_transfer_log;

/*
mysql> call sp_transfer_student(6, 1);
+----------------------+
| message              |
+----------------------+
| Transfer successful  |
+----------------------+

mysql> select * from department_transfer_log;
+--------+------------+--------------------+--------------------+---------------------+
| log_id | student_id | old_department_id  | new_department_id  | transfer_date        |
+--------+------------+--------------------+--------------------+---------------------+
|      1 |          6 |                  2 |                  1 | 2026-07-06 ...       |
+--------+------------+--------------------+--------------------+---------------------+
*/


# 46. Test the transaction with a forced error (invalid foreign key)
# and verify the first UPDATE is also rolled back.

CALL sp_transfer_student(6, 999);  # department 999 does not exist, FK violation

SELECT department_id FROM students WHERE student_id = 6;

/*
mysql> call sp_transfer_student(6, 999);
+---------------------------------+
| message                          |
+---------------------------------+
| Transfer failed - rolled back    |
+---------------------------------+

mysql> select department_id from students where student_id = 6;
+---------------+
| department_id |
+---------------+
|             1 |
+---------------+

Still 1 (unchanged) -- since department_transfer_log.new_department_id
has an FK referencing departments(department_id), the INSERT fails,
the EXIT HANDLER fires, and ROLLBACK undoes the earlier UPDATE too.
*/


# 47. SAVEPOINT test: insert two enrollment records, SAVEPOINT after
# the first, deliberately fail the second, ROLLBACK TO SAVEPOINT,
# and verify only the first record was saved.

START TRANSACTION;

INSERT INTO enrollments (student_id, course_id, enrollment_date, grade)
VALUES (3, 2, '2026-07-06', NULL);          # record 1: valid

SAVEPOINT sp1;

INSERT INTO enrollments (student_id, course_id, enrollment_date, grade)
VALUES (999, 999, '2026-07-06', NULL);      # record 2: invalid FK, fails

ROLLBACK TO SAVEPOINT sp1;
COMMIT;

SELECT * FROM enrollments WHERE student_id = 3;

/*
mysql> insert into enrollments (...) values (3, 2, '2026-07-06', NULL);
Query OK, 1 row affected

mysql> savepoint sp1;
Query OK, 0 rows affected

mysql> insert into enrollments (...) values (999, 999, '2026-07-06', NULL);
ERROR 1452 (23000): Cannot add or update a child row: a foreign key
constraint fails

mysql> rollback to savepoint sp1;
Query OK, 0 rows affected

mysql> commit;
Query OK, 0 rows affected

mysql> select * from enrollments where student_id = 3;
+---------------+------------+-----------+------------------+-------+
| enrollment_id | student_id | course_id | enrollment_date  | grade |
+---------------+------------+-----------+------------------+-------+
|             5 |          3 |         4 | 2021-07-01       | A     |
|            13 |          3 |         2 | 2026-07-06       | NULL  |
+---------------+------------+-----------+------------------+-------+
2 rows in set

Only the first (valid) insert survives -- ROLLBACK TO SAVEPOINT undid
just the failed statement's work, not the whole transaction, and the
earlier insert became permanent once COMMIT ran.
*/
