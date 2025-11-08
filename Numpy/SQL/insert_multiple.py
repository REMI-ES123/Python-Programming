import sqlite3

try:
    connection = sqlite3.connect("remi_db.db")
    cursor = connection.cursor()
    insert_data_query = """
        INSERT INTO student(name,email,course,cgpa) VALUES (?,?,?,?)
        """
    student_records = [
        ("Chitra", "chitra@gmail.com", "AIML", 6.9),
        ("Prakash", "prakash@gmail.com", "AIDS", 7.2),
        ("Kavitha", "kavi@gmail.com", "MECH", 8.8),
        ]
    cursor.executemany(insert_data_query, student_records)
    connection.commit()
    print("All Student Records Inserted Successfully")
except sqlite3.Error as error:
    print(error)
finally:
    cursor.close()
    connection.close()
