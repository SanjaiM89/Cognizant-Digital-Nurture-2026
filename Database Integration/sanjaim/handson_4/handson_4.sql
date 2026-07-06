# Task 1: Baseline Performance — No Indexes

/*
48. Run EXPLAIN (PostgreSQL) or EXPLAIN FORMAT=JSON (MySQL) on the following query and save
the output as a comment in your .sql file: SELECT s.first_name, s.last_name, c.course_name FROM
enrollments e JOIN students s ON s.student_id = e.student_id JOIN courses c ON c.course_id =
e.course_id WHERE s.enrollment_year = 2022;
*/

explain
select s.first_name, s.last_name, c.course_name from enrollments e join students s on s.student_id = e.student_id join courses c on 
c.course_id = e.course_id where s.enrollment_year=2022;

/*
mysql> explain
    -> select s.first_name, s.last_name, c.course_name from enrollments e join students s on s.student_id = e.student_id join courses c on 
    -> c.course_id = e.course_id where s.enrollment_year=2022;
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| EXPLAIN                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| -> Nested loop inner join  (cost=5.47 rows=1.67)
    -> Nested loop inner join  (cost=3.63 rows=1.67)
        -> Filter: (s.enrollment_year = 2022)  (cost=1.8 rows=1)
            -> Table scan on s  (cost=1.8 rows=8)
        -> Filter: (e.course_id is not null)  (cost=1.83 rows=1.67)
            -> Index lookup on e using student_id (student_id = s.student_id)  (cost=1.83 rows=1.67)
    -> Single-row index lookup on c using PRIMARY (course_id = e.course_id)  (cost=1.06 rows=1)
 |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
1 row in set (0.000 sec)

mysql> 

*/

# 49. Identify whether the query plan shows a Sequential Scan (Postgres) or Full Table Scan (MySQL) on any table

/*

The query plan shows Full Table Scan on the student table.

*/

# 50. Note the estimated cost (PostgreSQL) or rows examined (MySQL) in your comments

/*
Total Row Examined for the Full Table Scan is 8 Rows.
*/


# Task 2: Add Indexes and Compare Plans

# 51. Create a B-Tree index on students.enrollment_year

create index student_enroll_index on students(enrollment_year) using btree;
/*
mysql> create index student_enroll_index on students(enrollment_year) using btree;
Query OK, 0 rows affected (0.031 sec)
Records: 0  Duplicates: 0  Warnings: 0

mysql> 

*/

 
# 52. Create a composite UNIQUE index on enrollments(student_id, course_id) — this also prevents duplicate enrollments.

create unique index unique_student_enrollement_course on enrollments(student_id,course_id);

/*
mysql> create unique index unique_student_enrollement_course on enrollments(student_id,course_id);
Query OK, 0 rows affected (0.018 sec)
Records: 0  Duplicates: 0  Warnings: 0

mysql> 

*/

# 53. Create an index on courses.course_code.

create index course_code_index on courses(course_code);

/*
mysql> create index course_code_index on courses(course_code);
Query OK, 0 rows affected (0.019 sec)
Records: 0  Duplicates: 0  Warnings: 0

mysql> 

*/

# 54. Re-run the EXPLAIN from Task 1 and compare the new plan to the baseline. Document the change (Seq Scan → Index Scan?) as a comment.

/*

mysql> explain select s.first_name, s.last_name, c.course_name from enrollments e join students s on s.student_id = e.student_id join courses c on  c.course_id = e.course_id where s.enrollment_year=2022;
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| EXPLAIN                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| -> Nested loop inner join  (cost=4.9 rows=6.67)
    -> Nested loop inner join  (cost=2.57 rows=6.67)
        -> Index lookup on s using student_enroll_index (enrollment_year = 2022)  (cost=0.9 rows=4)
        -> Filter: (e.course_id is not null)  (cost=0.292 rows=1.67)
            -> Covering index lookup on e using unique_student_enrollement_course (student_id = s.student_id)  (cost=0.292 rows=1.67)
    -> Single-row index lookup on c using PRIMARY (course_id = e.course_id)  (cost=0.265 rows=1)
 |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
1 row in set (0.005 sec)

mysql> 


The DIFFERENCE:

-> The scan changed from "Table scan on s" to "Index lookup on s". It skipped the Full Table scan and jumped directly to the matching
Records
-> Previosuly the rows scanned was 8 rows not it examined only 4 rows


*/


# 55. Create a partial index on enrollments(student_id) WHERE grade IS NULL to optimise lookups for unevaluated enrollments.
create index enrollments_index on enrollments(student_id) where grade is null;
/*
Patial indexing is only supported PostgreSQL. MYSQL doesnot support it