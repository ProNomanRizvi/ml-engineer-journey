"""
File: 04_data_cleaning.py
Topic: Data Cleaning in Pandas (dropna, fillna, duplicates, string ops)
Author: Noman Rizvi
Phase: 4 - Week 3
"""

import pandas as pd

# ====================================================
# Quick Reference / Concept Notes: Data Cleaning
# ====================================================
# df.dropna()                       # Remove all rows with missing values (NaN)
# df.dropna(subset=["gpa"])         # Remove row ONLY if the "gpa" column has NaN
# df.fillna(0)                      # Replace all NaN values with 0
# df.fillna(df["gpa"].mean())       # Replace NaN values with the average (mean)
# df.duplicated()                   # Check which rows are exact duplicates (True/False)
# df.drop_duplicates()              # Remove duplicate rows
# df["age"] = df["age"].astype(int) # Convert a column's data type (e.g., to integer)
# df["name"].str.upper()            # String op: Convert text to UPPERCASE
# df["name"].str.strip()            # String op: Remove extra spaces at start and end
# df["name"].str.contains("Ali")    # String op: Check if the text contains a specific word


# ==========================================
# Setup: Create the Messy DataFrame
# ==========================================
print("--- Setup: Original Messy Data ---")
messy_data = {
    "name": ["Ali", "Sara", "  Omer  ", "Fatima", "Ali", None],
    "age": [20, None, 22, 20, 20, 25],
    "gpa": [3.5, 3.8, None, 3.9, 3.5, 3.2]
}

df = pd.DataFrame(messy_data)
print(df)
print("\n" + "="*40 + "\n")


# ==========================================
# Task 1: Check Missing Values
# ==========================================
print("--- Task 1: Count Missing Values ---")
# .isnull().sum() counts how many NaN/None values are in each column
missing_values = df.isnull().sum()
print(missing_values)
print("\n" + "="*40 + "\n")


# ==========================================
# Task 2: Drop Missing Values
# ==========================================
print("--- Task 2: Drop Rows with Missing Values ---")
# .dropna() removes any row that has at least one missing value
df_dropped = df.dropna()
print(df_dropped)
print("\n" + "="*40 + "\n")


# ==========================================
# Task 3: Fill Missing Values
# ==========================================
print("--- Task 3: Fill Missing Values (Fresh Start) ---")
# Make a fresh copy of the original data so we don't use the dropped version
df_filled = df.copy()

# Calculate the average (mean) age
mean_age = df_filled["age"].mean()

# Fill missing 'age' with the mean, and missing 'gpa' with 0
df_filled["age"] = df_filled["age"].fillna(mean_age)
df_filled["gpa"] = df_filled["gpa"].fillna(0)

print(f"Filled missing Age with Mean ({mean_age}) and GPA with 0:")
print(df_filled)
print("\n" + "="*40 + "\n")


# ==========================================
# Task 4: Check and Drop Duplicates
# ==========================================
print("--- Task 4: Handle Duplicate Rows ---")
# 1. Check for duplicates (Returns True for the duplicate "Ali" row at index 4)
print("Are there duplicates? (True/False):")
print(df.duplicated())

# 2. Drop the duplicates
print("\nDataFrame after dropping exact duplicates:")
df_deduped = df.drop_duplicates()
print(df_deduped)
print("\n" + "="*40 + "\n")


# ==========================================
# Task 5: Clean Text Data (Strings)
# ==========================================
print("--- Task 5: Clean String Data (Spaces & Uppercase) ---")
# Make another fresh copy to easily see the text changes
df_text = df.copy()

# .str.strip() removes extra empty spaces around words (fixes "  Omer  ")
df_text["name"] = df_text["name"].str.strip()

# .str.upper() makes all letters capital
df_text["name"] = df_text["name"].str.upper()

print("Names are now stripped of extra spaces and capitalized:")
print(df_text)