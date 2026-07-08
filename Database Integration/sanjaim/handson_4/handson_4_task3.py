import db

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

if __name__ == "__main__":
    con = db.get_connection()
    enrollments_n_plus_1_problem(con)
    con.close()