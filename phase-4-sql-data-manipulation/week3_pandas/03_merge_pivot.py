"""
File: 03_merge_pivot.py
Topic: Pandas Merge (Deep Dive - Inner, Left, Right, Outer Joins)
Author: Noman Rizvi
Phase: 4 - Week 3
"""

import pandas as pd

# ====================================================
# Quick Reference / Concept Notes: Merge (Deep Dive)
# ====================================================
# Basic Merge on a single column (Inner Join by default):
# pd.merge(df1, df2, on="student_id", how="inner")
#
# Merge on multiple columns (Useful when a single ID isn't enough to uniquely identify rows):
# pd.merge(df1, df2, on=["student_id", "semester"])


# ==========================================
# Setup: Create DataFrames
# ==========================================
print("--- Data Setup ---")
students_df = pd.DataFrame({
    "student_id": [1, 2, 3, 4, 5],
    "name": ["Ali", "Sara", "Omer", "Fatima", "Hassan"]
})

enrollments_df = pd.DataFrame({
    "student_id": [1, 2, 3, 6],  # Note: 6 doesn't exist in students, 4&5 have no enrollments
    "course": ["Data Structures", "Web Dev", "ML Basics", "Cloud Computing"]
})

print("Students DataFrame:\n", students_df, "\n")
print("Enrollments DataFrame:\n", enrollments_df, "\n")
print("="*50, "\n")


# ==========================================
# Task 1: Inner Merge
# ==========================================
print("--- Task 1: Inner Merge ---")
# 'inner' merge keeps ONLY the rows where 'student_id' exists in BOTH DataFrames.
# Kon gayab hoga? Students 4 (Fatima) aur 5 (Hassan) ki koi enrollment nahi hai, 
# aur Student 6 ka record students table mein nahi hai, toh yeh teeno gayab ho jayenge.
inner_merge = pd.merge(students_df, enrollments_df, on="student_id", how="inner")
print(inner_merge)
print("\n" + "="*50 + "\n")


# ==========================================
# Task 2: Left Merge
# ==========================================
print("--- Task 2: Left Merge ---")
# 'left' merge keeps ALL rows from the left DataFrame (students_df).
# Agar right mein match nahi milta, toh NaN fill kar dega.
# Result: Fatima aur Hassan ka course NaN/NULL aayega.
left_merge = pd.merge(students_df, enrollments_df, on="student_id", how="left")
print(left_merge)
print("\n" + "="*50 + "\n")


# ==========================================
# Task 3: Right Merge
# ==========================================
print("--- Task 3: Right Merge ---")
# 'right' merge keeps ALL rows from the right DataFrame (enrollments_df).
# Agar left mein match nahi milta, toh NaN fill kar dega.
# Result: student_id=6 ka course "Cloud Computing" dikhega, par name NaN hoga.
right_merge = pd.merge(students_df, enrollments_df, on="student_id", how="right")
print(right_merge)
print("\n" + "="*50 + "\n")


# ==========================================
# Task 4: Outer Merge
# ==========================================
print("--- Task 4: Outer Merge ---")
# 'outer' merge keeps EVERYTHING from both DataFrames (matched + unmatched dono side se).
# Jo match hua theek, jo nahi hua wahan NaN aa jayega.
outer_merge = pd.merge(students_df, enrollments_df, on="student_id", how="outer")
print(outer_merge)
print("\n" + "="*50 + "\n")


# ==========================================
# Task 5: Shape Comparison (Rows Count)
# ==========================================
print("--- Task 5: Comparing Row Counts ---")
print(f"Inner Merge gave: {inner_merge.shape[0]} rows")
print(f"Left Merge gave:  {left_merge.shape[0]} rows")
print(f"Right Merge gave: {right_merge.shape[0]} rows")
print(f"Outer Merge gave: {outer_merge.shape[0]} rows")
print("\nConclusion:")

# Explanation in simple English:
# Which one has the most rows and why?
print("-> The 'outer' merge gives the highest number of rows.")
print("   Why? Because it keeps EVERYTHING. It combines all matching rows")
print("   plus all unmatched rows from both the left and right DataFrames.")