# ==========================================
# TOPIC: Indexing and Slicing in NumPy
# ==========================================

import numpy as np

# Basic Indexing
print("\n============ Basic Indexing =============\n")
arr = np.array([10, 20, 30, 40, 50])
print("First element:", arr[0])
print("Last element:", arr[-1])
print("\n=========================================\n")

# Slicing
print("\n============ Slicing =============\n")
print("Elements from index 1 to 3:", arr[1:4])  
print("Elements from start to index 2:", arr[:3])
print("Every second element:", arr[::2])
print("\n=========================================\n")

# 2D Indexing
print("\n============ 2D Indexing =============\n")
matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("Element at row 1, column 2:", matrix[1, 2])
print("First row:", matrix[0, :])
print("Second column:", matrix[:, 1])
print("Submatrix (rows 0-1, columns 0-1):", matrix[0:2, 0:2])
print("\n=========================================\n")

# Boolean Indexing
print("\n============ Boolean Indexing =============\n")
bool_arr = arr > 30
print("Boolean array for elements greater than 30:", bool_arr)
filtered_arr = arr[bool_arr]
print("Filtered array (elements > 30):", filtered_arr)
print("\n=========================================\n")

# Fancy Indexing
print("\n============ Fancy Indexing =============\n")
indices = [0, 2, 4]
fancy_indexed_arr = arr[indices]
print("Fancy indexed array (elements at indices 0, 2, 4):", fancy_indexed_arr)
print("\n=========================================\n")


# TASKS 
print("\n============ TASKS =============\n")

# TASK 1
print("\n ----- Task 1 -----")

array = np.array([10,20,30,40,50,60,70,80,90,100])
print("Original array:", array)
print("First Element:", array[0])
print("Last Element:", array[-1])
print("Slice [2:6]:", array[2:6]) 
print("\n")

# TASK 2
print("\n ----- Task 2 -----")
print("Every third element:", array[::3])
print("\n")

# TASK 3
print("\n ----- Task 3 -----")
mrx = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])
print("3x3 Matrix: ")
print(mrx)

print("Complete 2nd Row | Complete 3rd Column")
print(mrx[1, :], "|", mrx[:, 2])
print("\n")

# TASK 4
print("\n ----- Task 4 -----")
print("top-left 2x2 block of the matrix:")
print(mrx[0:2, 0:2])
print("\n")

# TASK 5
print("\n ----- Task 5 -----")
arr_1d = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90, 100])
indices = [0, 3, 7]
print("Elements at indices 0, 3, and 7:", arr_1d[indices])
print("\n")

# TASK 6
print("\n ----- Task 6 -----")
print("Elements greater than 50:", arr_1d[arr_1d > 50])
print("\n")