# ======================================
# TOPIC: Math Operations & Dot Product
# ======================================

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
