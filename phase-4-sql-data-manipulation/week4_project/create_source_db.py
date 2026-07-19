# create_source_db.py
"""
File: create_source_db.py
Topic: Create a messy source database for the ETL project
Author: Noman Rizvi
Phase: 4 - Week 4
"""

import sqlite3
import os

def create_source_database():
    os.makedirs("data", exist_ok=True)
    conn = sqlite3.connect("data/source.db")
    cursor = conn.cursor()

    cursor.execute("DROP TABLE IF EXISTS sales")
    cursor.execute("""
        CREATE TABLE sales (
            id INTEGER PRIMARY KEY,
            product_name TEXT,
            category TEXT,
            price REAL,
            quantity INTEGER,
            sale_date TEXT
        )
    """)

    # Intentionally messy: extra spaces, mixed case, missing values, duplicates
    sales_data = [
        (1, "  Laptop  ", "Electronics", 800.0, 2, "2024-01-15"),
        (2, "mouse", "electronics", 20.0, 5, "2024-01-16"),
        (3, "Keyboard", "Electronics", None, 3, "2024-01-16"),
        (4, "  Desk Chair", "Furniture", 150.0, None, "2024-01-17"),
        (5, "Laptop", "electronics", 800.0, 2, "2024-01-15"),  # duplicate of row 1
        (6, "Notebook", "STATIONERY", 5.0, 10, "2024-01-18"),
        (7, "Pen", "Stationery", 1.5, None, "2024-01-19"),
        (8, "monitor", "Electronics", 300.0, 4, "2024-01-20"),
    ]
    cursor.executemany("INSERT INTO sales VALUES (?, ?, ?, ?, ?, ?)", sales_data)

    conn.commit()
    conn.close()
    print("Source database created: data/source.db")

if __name__ == "__main__":
    create_source_database()