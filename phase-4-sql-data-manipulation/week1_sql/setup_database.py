# Purpose: Create a sample SQLite database with dummy student data for practice

import sqlite3
import os

DATABASE_PATH = "/home/pronomanrizvi/Desktop/ml-engineer-journey/phase-4-sql-data-manipulation/week1_sql/data"

def create_database():
    """Create students.db with a sample 'students' table."""
    os.makedirs(DATABASE_PATH, exist_ok=True)
    conn = sqlite3.connect(os.path.join(DATABASE_PATH, "students.db"))
    cursor = conn.cursor()

    cursor.execute("DROP TABLE IF EXISTS students")
    cursor.execute("""
        CREATE TABLE students (
            id INTEGER PRIMARY KEY,
            name TEXT,
            age INTEGER,
            department TEXT,
            gpa REAL
        )
    """)

    students = [
        (1, "Ali Raza", 21, "CS", 3.8),
        (2, "Sana Khan", 22, "SE", 3.5),
        (3, "Bilal Ahmed", 20, "CS", 2.9),
        (4, "Ayesha Malik", 23, "SE", 3.9),
        (5, "Noman Rizvi", 21, "SE", 3.7),
    ]
    cursor.executemany("INSERT INTO students VALUES (?, ?, ?, ?, ?)", students)

    conn.commit()
    conn.close()
    print(f"Database created: {os.path.join(DATABASE_PATH, 'students.db')}")

if __name__ == "__main__":
    create_database()