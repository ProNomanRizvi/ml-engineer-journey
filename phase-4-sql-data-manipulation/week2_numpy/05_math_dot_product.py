"""
File: 05_math_dot_product.py
Topic: Math Operations & Dot Product
Author: Noman Rizvi
Phase: 4 - Week 2
"""
import numpy as np

# Basic Math Functions
arr = np.array([1, 4, 9, 16])
print("Original array:", arr)
print("Square root:", np.sqrt(arr))     # square root of each element → [1, 2, 3, 4]
print("Exponential:", np.exp(arr))       # e^x of each element
print("Logarithm:", np.log(arr))       # natural log of each element
print("Sum:", np.sum(arr))       # total sum
print("Mean:", np.mean(arr))      # average
print("Max:", np.max(arr))       # largest value
print("Min:", np.min(arr))       # smallest value
print("Standard Deviation:", np.std(arr))       # standard deviation

# Dot Product
print("\n============ Dot Product =============\n")
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

dot = np.dot(a, b)

print("Array a:", a)
print("Array b:", b)
print("Dot product of a and b:", dot)  # Output: 32 (1*4 + 2*5 + 3*6)
print("=================================================\n")

# Matrix Multiplication (2D Dot Product)
print("\n============ Matrix Multiplication =============\n")

A = np.array([
    [1, 2],
    [3, 4]
])
B = np.array([
    [5, 6],
    [7, 8]
])

result = np.dot(A, B)
print("Matrix A:\n", A)
print("Matrix B:\n", B)
print("Result of A dot B:\n", result)  # Output: [[19 22], [43 50]]
print("=================================================\n")


# =========== TASKS SECTION ===========

# ==========================================
# Task 1: Basic Array Math Operations
# ==========================================
print("--- Task 1: Basic Array Math ---")
# 1. Create the initial array
numbers_array = np.array([1, 4, 9, 16, 25])
print(f"Original Array: {numbers_array}")

# Calculate and print all the requested statistics
print(f"Square Root: {np.sqrt(numbers_array)}")
print(f"Sum: {np.sum(numbers_array)}")
print(f"Mean (Average): {np.mean(numbers_array)}")
print(f"Max Value: {np.max(numbers_array)}")
print(f"Min Value: {np.min(numbers_array)}")
print(f"Standard Deviation (std): {np.std(numbers_array):.2f}\n")


# ==========================================
# Task 2: Vector Dot Product & Manual Verification
# ==========================================
print("--- Task 2: Vector Dot Product ---")
# Create two 1D arrays (vectors)
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

# Calculate using NumPy's built-in dot function
vector_dot = np.dot(a, b)
print(f"Vector a: {a}, Vector b: {b}")
print(f"NumPy dot product result: {vector_dot}")

# Manual Calculation for verification:
# The dot product multiplies corresponding elements and adds them up:
# (a[0]*b[0]) + (a[1]*b[1]) + (a[2]*b[2])
# = (1 * 4) + (2 * 5) + (3 * 6) 
# = 4 + 10 + 18 
# = 32
print("Manual verification: (1*4) + (2*5) + (3*6) = 32\n")


# ==========================================
# Task 3: 2x2 Matrix Multiplication
# ==========================================
print("--- Task 3: 2x2 Matrix Multiplication ---")
# Create two 2x2 matrices (lists of lists)
matrix1 = np.array([[1, 2], 
                    [3, 4]])
matrix2 = np.array([[5, 6], 
                    [7, 8]])

# Multiply them using np.dot()
result_2x2 = np.dot(matrix1, matrix2)
print("Result of multiplying two 2x2 matrices:")
print(result_2x2)
print()


# ==========================================
# Task 4: Multiplying Matrices of Different Shapes
# ==========================================
print("--- Task 4: Shape Rule Verification (2x3 * 3x2) ---")
# Create a 2x3 matrix (2 rows, 3 columns)
mat_2x3 = np.array([[1, 2, 3], 
                    [4, 5, 6]]) 

# Create a 3x2 matrix (3 rows, 2 columns)
mat_3x2 = np.array([[7, 8], 
                    [9, 10], 
                    [11, 12]])

# Multiply them. Because the inner dimensions match (3 and 3), this will work.
result_mixed = np.dot(mat_2x3, mat_3x2)

print(f"Shape of first matrix: {mat_2x3.shape}")
print(f"Shape of second matrix: {mat_3x2.shape}")
print("Resulting Matrix:")
print(result_mixed)

# Verify the output shape. The outer dimensions (2 and 2) dictate the result shape.
print(f"Shape of resulting matrix: {result_mixed.shape} -> Rule Verified!\n")


# ==========================================
# Task 5: Handling Incompatible Shapes (Try/Except)
# ==========================================
print("--- Task 5: Incompatible Shapes Error Handling ---")
# Setup two matrices that CANNOT be multiplied 
incompatible_mat1 = np.array([[1, 2, 3], [4, 5, 6]]) # Shape: 2x3
incompatible_mat2 = np.array([[1, 2], [3, 4]])       # Shape: 2x2

print(f"Trying to multiply a {incompatible_mat1.shape} matrix with a {incompatible_mat2.shape} matrix...")

# We wrap this in a try/except block so the program doesn't crash when it fails
try:
    # This will throw a ValueError because the inner dimensions (3 and 2) don't match
    failed_result = np.dot(incompatible_mat1, incompatible_mat2)
except Exception as e:
    print("Failure caught successfully! Here is the error:")
    print(f"-> {type(e).__name__}: {e}")
