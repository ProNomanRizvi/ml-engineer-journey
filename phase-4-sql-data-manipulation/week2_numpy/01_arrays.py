"""
File: 01_arrays.py
Topic: NumPy Arrays - Creation & Attributes
Author: Noman Rizvi
Phase: 4 - Week 2
"""

import numpy as np

# Normal Python list
prices = [100, 200, 300]
discounted = [p * 0.9 for p in prices]

# NumPy array
prices_np = np.array([100, 200, 300])
discounted = prices_np * 0.9

# Array Creation Methods

print("============= Array Creation Methods =============")
# 1- Using np.array() to create an array from a list
np.array([1, 2, 3])
print("Array created using np.array():", np.array([1, 2, 3]))

# 2- Using np.zeros() to create an array of zeros
np.zeros(5) 
print("Array created using np.zeros():", np.zeros(5))

# 3- Using np.ones() to create an array of ones
np.ones(5)
print("Array created using np.ones():", np.ones(5))

# 4- Using np.arange() to create an array with a range of values   
np.arange(0, 10, 2)
print("Array created using np.arange():", np.arange(0, 10, 2))

# 5- Using np.linspace() to create an array with evenly spaced values  
np.linspace(0, 1, 5)
print("Array created using np.linspace():", np.linspace(0, 1, 5))
print("=====================================================\n")

# Important Attributes of NumPy Arrays
print("============= Important Attributes of NumPy Arrays =============")
arr = np.array([1, 2, 3])
print("Array:\n", arr)
print("Shape of the array:", arr.shape)
print("Number of dimensions:", arr.ndim)
print("Data type of the array:", arr.dtype)
print("Size of each element in bytes:", arr.itemsize)
print("Total number of elements in the array:", arr.size)
print("Total size of the array in bytes:", arr.nbytes)
print("=====================================================\n")

# 1D Array VS 2D Array
print("============= 1D Array VS 2D Array =============")
# 1D Array
arr_1d = np.array([1, 2, 3])
print("1D Array:\n", arr_1d)
# 2D Array
arr_2d = np.array([[1, 2, 3], [4, 5, 6]])
print("2D Array:\n", arr_2d)
print("================================================\n")

# TASKS SECTION
print("================ Tasks Section =================")

# Task 1: Create a NumPy array from a list and print it.
print("Task 1")
lst = [10, 20, 30, 40, 50]
# Convert the list to a NumPy array and print it
arr_from_list = np.array(lst)
print("NumPy array from list:", arr_from_list)
print("\n")

# Task 2: Create zeros, ones, and a range of values using NumPy functions and print them.
print("Task 2")
print(np.zeros(5))
print(np.ones(5))
print(np.arange(0, 20, 5))
print("\n")
# Task 3: Create a 2D NumPy array and print its shape, number of dimensions, data type, and size.
print("Task 3")
arr_2d_task3 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("2D Array (3x3):")
print(arr_2d_task3)
print("Shape:", arr_2d_task3.shape)   # Expected: (3, 3)
print("Dimensions:", arr_2d_task3.ndim)
print("Data type:", arr_2d_task3.dtype)
print("Size:", arr_2d_task3.size)      # Expected: 9
print("\n")

# Task 4:
print("Task 4")
print(np.linspace(0, 100, 5))
print("\n")

# Task 5:
print("Task 5")
int_array = np.array([1, 2, 3, 4, 5])
print("Array:", int_array)
print("Data type:", int_array.dtype)

# Method 1: Convert existing array using astype
converted_array = int_array.astype(float)
print("Converted using astype():", converted_array, "| dtype:", converted_array.dtype)

# Method 2: Create new array with dtype specified at creation
float_array = np.array([1, 2, 3, 4, 5], dtype=float)
print("Created with dtype=float:", float_array, "| dtype:", float_array.dtype)