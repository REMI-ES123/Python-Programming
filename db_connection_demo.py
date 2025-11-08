import sqlite3

try:
    # connect  to the database
    connection = sqlite3.connect('remi_db.db')
    cursor = connection.cursor()
    # Select and print data
    cursor.execute("SELECT * FROM book")
    print("book table")
    for row in cursor.fetchall():
        print(row)
except sqlite3.Error as e:
    print(f"SQLite error : {e}")
finally:
    if connection:
       connection.close