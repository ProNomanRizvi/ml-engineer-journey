# Purpose: Create a sample SQLite database with dummy student data for practice

import sqlite3
import os

DATABASE_PATH = "/home/pronomanrizvi/Desktop/ml-engineer-journey/phase-4-sql-data-manipulation/week1_sql/data"


def create_database():
    """Create students.db with sample 'students' and 'enrollments' tables."""

    os.makedirs(DATABASE_PATH, exist_ok=True)

    db_file = os.path.join(DATABASE_PATH, "students.db")

    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()

    # Keep OFF because one enrollment intentionally references
    # a non-existing student for LEFT JOIN practice.
    cursor.execute("PRAGMA foreign_keys = OFF")

    # -----------------------------
    # Create Students Table
    # -----------------------------
    cursor.execute("DROP TABLE IF EXISTS students")

    cursor.execute("""
        CREATE TABLE students (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
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

    cursor.executemany(
        "INSERT INTO students VALUES (?, ?, ?, ?, ?)",
        students
    )

    # -----------------------------
    # Create Enrollments Table
    # -----------------------------
    cursor.execute("DROP TABLE IF EXISTS enrollments")

    cursor.execute("""
        CREATE TABLE enrollments (
            enrollment_id INTEGER PRIMARY KEY,
            student_id INTEGER,
            course_name TEXT,
            FOREIGN KEY (student_id) REFERENCES students(id)
        )
    """)

    enrollments = [
        (1, 1, "Data Structures"),
        (2, 2, "Web Development"),
        (3, 3, "Data Structures"),
        (4, 5, "Machine Learning"),
        (5, 6, "Cloud Computing"),   # Intentional for LEFT JOIN practice
    ]

    cursor.executemany(
        "INSERT INTO enrollments VALUES (?, ?, ?)",
        enrollments
    )

    # -----------------------------
    # Save Changes & Close
    # -----------------------------
    conn.commit()
    conn.close()

    print(f"Database created successfully: {db_file}")


if __name__ == "__main__":
    create_database()