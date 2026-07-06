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