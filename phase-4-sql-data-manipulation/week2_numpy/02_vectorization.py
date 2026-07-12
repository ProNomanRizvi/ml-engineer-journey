"""
File: 02_vectorization.py
Topic: Vectorization
Author: Noman Rizvi
Phase: 4 - Week 2
"""

import numpy as np
import time

# Common Vectorized Operations
a = np.array([1, 2, 3])
b = np.array([10, 20, 30])

print("Array 1: ", a)
print("Array 2: ", b)    

print("Addition: ", a + b)
print("Subtraction: ", a - b)
print("Multiplication: ", a * b)
print("Division: ", a / b)
print("Power: ", a ** b)

print("Greater than 2: ", a > 2)

# ============= TASKS SECTIONS ===============
print("\n\n================= TASKS =================")
# Task 1: 
x = np.array([1, 2, 3, 4, 5])
y = np.array([10, 20, 30, 40, 50])

print("TASK 1: Vectorized Operations")
print("x: ", x)
print("y: ", y)
print("x + y: ", x + y)
print("x - y: ", x - y)
print("x * y: ", x * y)
print("x / y: ", x / y)
print("a ** 2: ", a ** 2)

# Task 2:
print("\nTASK 2: Speed Comparison")

# Create large arrays for speed comparison
arr = np.arange(1000000)  # Array of 1 million elements

# Check Time Via Python LOOP

start_time = time.time()
result = []
for i in range(len(arr)):
    result.append(arr[i] ** 2)
end_time = time.time()
print("Time taken by Python loop: ", end_time - start_time)

# Check Time Via Vectorized Operation
start_time = time.time()
result = arr ** 2
end_time = time.time()
print("Time taken by vectorized operation: ", end_time - start_time)

# Task 3: Boolean Comparison
print("\nTASK 3: Boolean Comparison")
arr1 = np.array([1, 2, 3, 4, 5])
print("arr1: ", arr1)

print("arr1 > 3: ", arr1 > 3)
print("a[arr1 > 3]: ", arr1[arr1 > 3])  # Using boolean indexing to filter values greater than 3