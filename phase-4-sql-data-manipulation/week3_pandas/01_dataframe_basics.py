"""
File: 01_dataframe_basics.py
Topic: DataFrame Creation, loc & iloc
Author: Noman Rizvi
Phase: 4 - Week 3
"""

import pandas as pd

# ==========================================
# Quick Reference / Concept Notes
# ==========================================
# DataFrame Creation Methods:
# pd.DataFrame(dictionary)                       # From dictionary
# pd.DataFrame(list_of_lists, columns=["a","b"]) # From list of lists
# pd.read_csv("file.csv")                        # From CSV file (very common)

# Indexing Basics (Assuming default integer index):
# df.loc[0]           # Row with index label 0
# df.loc[0, "name"]   # Row with index label 0, column "name"
# df.iloc[0]          # Row at position 0 (regardless of index label)
# df.iloc[0, 1]       # Row at position 0, column at position 1

# Slicing differences:
# df.loc[0:2]         # 0, 1, 2 — inclusive (label-based slicing includes end)
# df.iloc[0:2]        # 0, 1 — exclusive (position-based slicing excludes end, like Python lists)


# ==========================================
# Task 1: Create Dictionary and DataFrame
# ==========================================
print("--- Task 1: DataFrame Creation ---")
# Create a dictionary with data for 5 students
student_data = {
    "name": ["Ali", "Sara", "Omer", "Fatima", "Hassan"],
    "age": [20, 21, 22, 20, 23],
    "department": ["Computer Science", "Electrical", "Business", "Physics", "Mechanical"],
    "gpa": [3.5, 3.8, 3.2, 3.9, 3.1]
}

# Convert the dictionary into a pandas DataFrame
df = pd.DataFrame(student_data)
print("Original DataFrame:")
print(df)
print("\n")


# ==========================================
# Task 2: Exploring Basic DataFrame Methods
# ==========================================
print("--- Task 2: Built-in Methods Output ---")
# df.head() shows the first 5 rows by default
print("1. df.head() -> Shows top rows:\n", df.head())
print()

# df.tail(2) shows the last 2 rows
print("2. df.tail(2) -> Shows bottom 2 rows:\n", df.tail(2))
print()

# df.info() provides a concise summary of the DataFrame
print("3. df.info() -> Structural summary:")
df.info() 
print()

# df.describe() calculates statistical data for numeric columns
print("4. df.describe() -> Statistical summary for 'age' and 'gpa':\n", df.describe())
print("\n")


# ==========================================
# Task 3: Using 'loc' (Label-based indexing)
# ==========================================
print("--- Task 3: Extracting with loc ---")
# Get the complete row at index label 2
row_2_full = df.loc[2]
print("Complete row at index 2:\n", row_2_full)
print()

# Get only the 'name' and 'gpa' columns for row index 2
row_2_specific = df.loc[2, ["name", "gpa"]]
print("Only 'name' and 'gpa' for row 2:\n", row_2_specific)
print("\n")


# ==========================================
# Task 4: Using 'iloc' (Position-based indexing)
# ==========================================
print("--- Task 4: Extracting with iloc ---")
# Get the row at physical position/index 2
row_2_position = df.iloc[2]
print("Row at position 2 using iloc:\n", row_2_position)
print()

# Observation: loc[2] and iloc[2] match here because the default index is 0, 1, 2...
print("-> Comparison: loc and iloc outputs match here because default labels equal row positions.\n")


# ==========================================
# Task 5: Changing the Index & Comparing loc vs iloc
# ==========================================
print("--- Task 5: set_index and loc vs iloc differences ---")
# Create a new DataFrame where the "name" column becomes the index
df_custom = df.set_index("name")
print("New DataFrame (names are now the index):\n", df_custom)
print()

# Now we MUST use a name string with .loc
student_row = df_custom.loc["Sara"]
print("Extracting Sara's data using loc['Sara']:\n", student_row)
print()

# However, .iloc ALWAYS uses integer positions
first_row_iloc = df_custom.iloc[0]
print("Extracting the very first row using iloc[0]:\n", first_row_iloc)
print()

# Final Conclusion
print("-> Final Observation:")
print("   'loc' looks at the exact LABEL you set (like 'Sara').")
print("   'iloc' looks at the integer POSITION (like 0 for the 1st row), ignoring custom labels.")