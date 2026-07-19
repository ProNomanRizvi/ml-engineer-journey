"""
File: 05_string_operations.py
Topic: Pandas String Operations and Data Type Conversions
Author: Noman Rizvi
Phase: 4 - Week 3
"""

import pandas as pd

# ====================================================
# Quick Reference / Concept Notes
# ====================================================
# --- String Operations ---
# df["name"].str.lower()                  # Convert all text to lowercase
# df["name"].str.len()                    # Get the length of each string
# df["name"].str.contains("Ali")          # Check if text contains "Ali" (True/False)
# df["name"].str.replace("Ali", "Aliyan") # Replace specific text with something else
# df["email"].str.split("@")              # Split text into a list around a character
# df["name"].str.startswith("A")          # Check if text starts with a specific letter

# --- Data Type (dtype) Conversions ---
# df.dtypes                                 # Show data types of all columns
# df["age"] = df["age"].astype(int)         # Convert float/string to integer
# df["age"] = df["age"].astype(str)         # Convert numbers to text/string
# pd.to_numeric(df["age"], errors="coerce") # Convert text to number, force invalid text to NaN


# ==========================================
# Setup: Create DataFrame
# ==========================================
print("--- Data Setup ---")
data = {
    "name": ["ali khan", "SARA ahmed", "Omer Sheikh", "fatima ALI"],
    "email": ["ali@gmail.com", "sara@yahoo.com", "omer@gmail.com", "fatima@outlook.com"],
    "age_text": ["20", "21", "twenty-two", "20"]
}

df = pd.DataFrame(data)
print("Original DataFrame:")
print(df)
print("\n" + "="*50 + "\n")


# ==========================================
# Task 5 (Part A): Check dtypes BEFORE
# ==========================================
print("--- Task 5 (Before): Data Types ---")
# 'object' in Pandas usually means strings/text
print("Notice that 'age_text' is an 'object' (string) type:")
print(df.dtypes)
print("\n" + "="*50 + "\n")


# ==========================================
# Task 1: Convert names to Title Case
# ==========================================
print("--- Task 1: Title Case Names ---")
# .str.title() capitalizes the first letter of every word
df["name"] = df["name"].str.title()
print("Names converted to Title Case:")
print(df)
print("\n" + "="*50 + "\n")


# ==========================================
# Task 2: Find names containing "Ali" 
# ==========================================
print("--- Task 2: Find 'Ali' in Names ---")
# case=False makes the search case-insensitive (matches "ali", "ALI", "Ali", etc.)
contains_ali = df[df["name"].str.contains("ali", case=False)]
print("Rows where the student's name contains 'Ali':")
print(contains_ali)
print("\n" + "="*50 + "\n")


# ==========================================
# Task 3: Split email and extract domain
# ==========================================
print("--- Task 3: Extract Email Domain ---")
# .str.split("@") splits "ali@gmail.com" into a list: ["ali", "gmail.com"]
# .str[1] safely extracts the second item from that list (the domain)
df["domain"] = df["email"].str.split("@").str[1]
print("DataFrame with the new 'domain' column:")
print(df)
print("\n" + "="*50 + "\n")


# ==========================================
# Task 4: Convert age_text to numeric
# ==========================================
print("--- Task 4: Convert 'age_text' to Numbers ---")
# errors="coerce" is a safety net. If it finds text like "twenty-two" 
# that it can't convert to a raw number, it replaces it with NaN (Not a Number).
df["age_numeric"] = pd.to_numeric(df["age_text"], errors="coerce")
print("DataFrame with numeric age column (notice 'twenty-two' became NaN):")
print(df)
print("\n" + "="*50 + "\n")


# ==========================================
# Task 5 (Part B): Check dtypes AFTER
# ==========================================
print("--- Task 5 (After): Data Types Comparison ---")
# Because of the NaN value, Pandas automatically makes 'age_numeric' a float64 
print("Notice that our new 'age_numeric' column is a proper numeric type (float64):")
print(df.dtypes)