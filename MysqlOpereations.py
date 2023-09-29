import mysql.connector
# Connect to MySQL
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="assignment"
)
c = mydb.cursor()


# Create a new database
c = mydb.cursor()
c.execute("CREATE DATABASE IF NOT EXISTS assignment")
c.execute("USE assignment")

# Create the 'students' table
c.execute("""
    CREATE TABLE IF NOT EXISTS students (
        student_id INT AUTO_INCREMENT PRIMARY KEY,
        first_name VARCHAR(255),
        last_name VARCHAR(255),
        age INT,
        grade FLOAT
    )
""")

# Insert a new student record
insert_query = "INSERT INTO students (first_name, last_name, age, grade) VALUES (%s, %s, %s, %s)"
student_data = ("Alice", "Smith", 18, 95.5)
c.execute(insert_query, student_data)
mydb.commit()

# Update Alice's grade
update_query = "UPDATE students SET grade = %s WHERE first_name = %s"
new_grade = 97.0
c.execute(update_query, (new_grade, "Alice"))
mydb.commit()

# Delete the student with the last name "Smith"
delete_query = "DELETE FROM students WHERE last_name = %s"
c.execute(delete_query, ("Smith",))
mydb.commit()

# Fetch and display all student records
select_query = "SELECT * FROM students"
c.execute(select_query)
students = c.fetchall()

for student in students:
    print(f"Student ID: {student[0]}, First Name: {student[1]}, Last Name: {student[2]}, Age: {student[3]}, Grade: {student[4]}")

# Close the connection
c.close()
mydb.close()