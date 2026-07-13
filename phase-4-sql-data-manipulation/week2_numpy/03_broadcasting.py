# ============================
# TOPIC: Broadcasting
# ============================

import numpy as np

arr = np.array([1, 2, 3])
result = arr + 10          
print("Original array: ", arr)
print("Adding a scalar to an array: ", result)

# 2D + 1D Example
matrix = np.array([[1, 2, 3], [4, 5, 6]])   # shape (2,3)
row = np.array([10, 20, 30])                  # shape (3,)

result = matrix + row
print("\nOriginal matrix:\n", matrix)
print("Row to be added:\n", row)
print("Result after broadcasting:\n", result)

# ========= TASKS SECTION =========
print("\n=============== TASKS SECTION =================\n")
# TASK 1
x = np.array([1, 2, 3, 4, 5])

x = x + 10

print("TASK 1: Adding a scalar to an array")
print("Original array: ", np.array([1, 2, 3, 4, 5]))
print("After adding 10: ", x)

print("\n")
# TASK 2
array_2d = np.array([[1, 2, 3], [4, 5, 6]])
row_1d = np.array([10, 20, 30])

result = array_2d + row_1d

print("TASK 2: Broadcasting 2D array with 1D array")
print("Original 2D array:\n", array_2d)
print("1D array to be added:\n", row_1d)
print("Result after broadcasting:\n", result)

print("\n")
# TASK 3
arr_2d = np.array([[1], [2], [3]])  # shape (3,1)
arr_1d = np.array([10, 20, 30])     # shape (1,3)
result = arr_2d + arr_1d

print("TASK 3: Broadcasting 2D array with 1D array (different shapes)")
print("Original 2D array:\n", arr_2d)
print("1D array to be added:\n", arr_1d)
print("Result after broadcasting:\n", result)

print("\n")
# TASK 4

try:
    arr_2_by_3 = np.array([[1, 2, 3], [4, 5, 6]])  # shape (2,3)
    arr_2_by_2 = np.array([[10, 20], [30, 40]])        # shape (2,2)
    result = arr_2_by_3 + arr_2_by_2
    print("TASK 4: Attempting to broadcast incompatible shapes")
    print("Original 2D array (2x3):\n", arr_2_by_3)
    print("Original 2D array (2x2):\n", arr_2_by_2)
    print("Result after broadcasting:\n", result)
except Exception as e:
    print("TASK 4: Broadcasting failed due to incompatible shapes.")
    print("Error message:", e)