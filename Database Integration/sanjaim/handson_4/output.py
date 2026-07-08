"""
(venv) [sanjai@sanjai handson_4]$ python handson_4_task3.py
STEP 56
[{'student_name': 'Arjun Mehta'}, {'student_name': 'Arjun Mehta'}, {'student_name': 'Priya Suresh'}, {'student_name': 'Priya Suresh'}, {'student_name': 'Rohan Verma'}, {'student_name': 'Vikram Das'}, {'student_name': 'Vikram Das'}, {'student_name': 'Kavya Menon'}, {'student_name': 'Deepika Rao'}, {'student_name': 'Deepika Rao'}]
11
STEP 57
[{'student_name': 'Arjun Mehta'}, {'student_name': 'Arjun Mehta'}, {'student_name': 'Priya Suresh'}, {'student_name': 'Priya Suresh'}, {'student_name': 'Rohan Verma'}, {'student_name': 'Vikram Das'}, {'student_name': 'Vikram Das'}, {'student_name': 'Kavya Menon'}, {'student_name': 'Deepika Rao'}, {'student_name': 'Deepika Rao'}]
1
STEP 58
[{'student_name': 'Arjun Mehta'}, {'student_name': 'Arjun Mehta'}, {'student_name': 'Priya Suresh'}, {'student_name': 'Priya Suresh'}, {'student_name': 'Rohan Verma'}, {'student_name': 'Vikram Das'}, {'student_name': 'Vikram Das'}, {'student_name': 'Kavya Menon'}, {'student_name': 'Deepika Rao'}, {'student_name': 'Deepika Rao'}]
11
[{'student_name': 'Arjun Mehta'}, {'student_name': 'Arjun Mehta'}, {'student_name': 'Priya Suresh'}, {'student_name': 'Priya Suresh'}, {'student_name': 'Rohan Verma'}, {'student_name': 'Vikram Das'}, {'student_name': 'Vikram Das'}, {'student_name': 'Kavya Menon'}, {'student_name': 'Deepika Rao'}, {'student_name': 'Deepika Rao'}]
1
N+1 Problem Time Start_Time 1783513388.0852 End_Time 1783513388.0863
One Json Query Start_Time 1783513388.0863 End_Time 1783513388.0865
Time Difference -0.0009
Query Difference 10.0000
(venv) [sanjai@sanjai handson_4]$





59. Document in comments: in a real application with 10,000 enrollments, how many extra queries would
the N+1 version issue?

Issues in N+1
    -> In N+1 we use one query (select * from enrollments) to fetch all the enrollments and than use N additional queries to fetch the student name 
    registered for the course

    So for 10,000 enrollments the total queries would be N + 1 i.e 10,000+1 = 10,001 queries and the N additonal queries would be 10,001 + N queries

    When comparied to this to JOIN Approach which uses one JOIN query to get the values regardless of how any enrollments are there
"""