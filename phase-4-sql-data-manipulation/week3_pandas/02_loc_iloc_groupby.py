"""
File: 02_loc_iloc_groupby.py
Topic: GroupBy, Merge, Apply (Lambda), and Pivot Tables
Author: Noman Rizvi
Phase: 4 - Week 3
"""

import pandas as pd

# ====================================================
# Quick Reference / Concept Notes
# ====================================================
print("--- Concept Notes: GroupBy, Merge, Pivot, Apply ---")

# 1. Basic DataFrame for Concepts
df_employees = pd.DataFrame({
    "Name": ["Alice", "Bob", "Charlie", "David", "Eva", "Frank"],
    "Age": [25, 30, 35, 40, 45, 50],
    "City": ["New York", "Los Angeles", "Chicago", "Houston", "Phoenix", "Philadelphia"],
    "Salary": [50000, 60000, 70000, 80000, 90000, 100000],
    "Department": ["HR", "IT", "Finance", "IT", "Finance", "HR"],
    "Experience": [2, 5, 10, 15, 20, 25],
})

# Concept: Groupby
avg_salary_by_dept = df_employees.groupby("Department")["Salary"].mean()
print("1. Average Salary by Department:\n", avg_salary_by_dept)
print()

# Concept: Merge (Inner Join Example)
df1 = pd.DataFrame({"student_id": [1, 2, 3], "name": ["Ali", "Sara", "Omer"]})
df2 = pd.DataFrame({"student_id": [1, 2], "gpa": [3.5, 3.8]})
merged_df = pd.merge(df1, df2, on="student_id", how="inner")
print("2. Merge Example (Inner Join on student_id):\n", merged_df)
print()

# Concept: Pivot Table & Apply Lambda (Syntax references applied in Tasks below)
# df.pivot_table(values="gpa", index="department", aggfunc="mean")
# df["gpa_percent"] = df["gpa"].apply(lambda x: x * 25)

print("\n" + "="*50 + "\n")


# ==========================================
# Setup: Create Student DataFrame
# ==========================================
print("--- Data Setup (Tasks) ---")
# Extending the dictionary so 'Computer Science', 'Business', and 'Electrical' 
# have multiple students. This makes groupby operations useful.
student_data = {
    "name": ["Ali", "Sara", "Omer", "Fatima", "Hassan", "Ayesha", "Zain"],
    "age": [20, 21, 22, 20, 23, 21, 22],
    "department": ["Computer Science", "Electrical", "Business", "Computer Science", "Mechanical", "Business", "Electrical"],
    "gpa": [3.5, 3.8, 3.2, 3.9, 3.1, 3.6, 3.4]
}

df = pd.DataFrame(student_data)
print("Original Student DataFrame:")
print(df)
print("\n" + "="*50 + "\n")


# ==========================================
# Task 1: GroupBy - Average GPA per Department
# ==========================================
print("--- Task 1: Average GPA by Department ---")
# We group by the 'department' column, select only the 'gpa' column, and calculate the mean.
avg_gpa_by_dept = df.groupby("department")["gpa"].mean()

print(avg_gpa_by_dept)
print("\n" + "="*50 + "\n")


# ==========================================
# Task 2: GroupBy - Student Count per Department
# ==========================================
print("--- Task 2: Student Count by Department ---")
# We group by 'department' and use .size() to count total rows (students) in each group.
# Alternatively, df.groupby("department")["name"].count() works too.
student_count_by_dept = df.groupby("department").size()

print(student_count_by_dept)
print("\n" + "="*50 + "\n")


# ==========================================
# Task 3: Apply Lambda - Create gpa_percent column
# ==========================================
print("--- Task 3: Converting GPA to Percentage using apply() ---")
# We use apply with a lambda function. For every value 'x' in the 'gpa' column,
# it calculates (x / 4.0) * 100. We assign this to a new column 'gpa_percent'.
df["gpa_percent"] = df["gpa"].apply(lambda x: (x / 4.0) * 100)

print("DataFrame with new 'gpa_percent' column:")
print(df)
print("\n" + "="*50 + "\n")


# ==========================================
# Task 4: Pivot Table - Average GPA per Department
# ==========================================
print("--- Task 4: Average GPA using pivot_table ---")
# pivot_table does exactly what our groupby did in Task 1, but creates a clean DataFrame structure.
# index = what to group by (rows)
# values = what data to calculate
# aggfunc = what math operation to perform ('mean' is default, but it's good practice to write it)
pivot_avg_gpa = pd.pivot_table(df, index="department", values="gpa", aggfunc="mean")

print("Result from pivot_table:")
print(pivot_avg_gpa)
print("\n")

print("--- Comparison ---")
print("Notice that Task 1 (groupby) returns a Pandas Series, while Task 4 (pivot_table) returns a standard Pandas DataFrame. The mathematical result is exactly the same!")