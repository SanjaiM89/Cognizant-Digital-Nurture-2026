from tokenize import endpats

import db
import time
#  56. Simulate the N+1 problem in Python: fetch all enrollments with SELECT * FROM enrollments, then
# loop through each row and issue a separate SELECT to fetch the student's name. Count the total
# queries executed
# 

def enrollments_n_plus_1_problem(con):
    cursor = con.cursor(dictionary=True, buffered=True)
    count_of_query = 0

    cursor.execute("select * from enrollments")
    enrollments = cursor.fetchall()
    count_of_query+=1

    enroll = []
    for enrollment in enrollments:
        cursor.execute(
            #select concat(students.first_name,' ',students.last_name) from enrollments left join students on enrollments.student_id = students.student_id where enrollments.student_id=2
            "select concat(students.first_name,' ',students.last_name) as name from enrollments left join students on enrollments.student_id = students.student_id where enrollments.student_id=%s",(enrollment["student_id"],),
        )

        student = cursor.fetchone()
        count_of_query+=1

        enroll.append({
            "student_name":student["name"] if student else None
        })

    cursor.close()

    print(enroll)
    print(count_of_query)
    return enroll, count_of_query

# 57. Rewrite the script using a single JOIN query that retrieves all enrollment records with student names in one query.

def enrollments_json(con):
    cursor = con.cursor(dictionary=True, buffered=True)
    count_of_query = 0

    # cursor.execute("select * from enrollments")
    # 
    
    cursor.execute(
        """
        select concat(students.first_name,' ',students.last_name) as name from enrollments join students on enrollments.student_id
        = students.student_id
        """
    )
    # enrollments = cursor.fetchall()
    count_of_query+=1

    enroll = []
    for row in cursor.fetchall():
        enroll.append({"student_name":row["name"]})

    # enroll = []
    # for enrollment in enrollments:
    #     cursor.execute(
    #         #select concat(students.first_name,' ',students.last_name) from enrollments left join students on enrollments.student_id = students.student_id where enrollments.student_id=2
    #         "select concat(students.first_name,' ',students.last_name) as name from enrollments left join students on enrollments.student_id = students.student_id where enrollments.student_id=%s",(enrollment["student_id"],),
    #     )

    #     student = cursor.fetchone()
    #     count_of_query+=1

    #     enroll.append({
    #         "student_name":student["name"] if student else None
    #     })
    
    cursor.close()

    print(enroll)
    print(count_of_query)

    return enroll, count_of_query


def comparison(con):
    start_time = time.time()
    enroll, query_count = enrollments_n_plus_1_problem(con)
    end_time = time.time()

    start = time.time()
    enroll_json, query_count_json = enrollments_json(con)
    end = time.time()
    print(f"N+1 Problem Time Start_Time {start_time:.4f} End_Time {end_time:.4f}")
    print(f"One Json Query Start_Time {start:.4f} End_Time {end:.4f}")
    print(f"Time Difference {(start_time - end_time)-(start - end):.4f}")
    print(f"Query Difference {query_count - query_count_json:.4f}")
    

if __name__ == "__main__":
    con = db.get_connection()
    print("STEP 56")
    enrollments_n_plus_1_problem(con)
    print("STEP 57")
    enrollments_json(con)
    print("STEP 58")
    comparison(con)
    con.close()