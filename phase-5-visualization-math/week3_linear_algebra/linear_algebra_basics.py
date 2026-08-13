import numpy as np

# ============================================================
# 1. VECTORS
# ============================================================
print("--- Vectors: Addition, Subtraction, Dot Product ---")

v1 = np.array([2, 4, 6])
v2 = np.array([1, 3, 5])

# Addition/subtraction of vectors matters because in ML we constantly
# combine feature vectors, gradients, or weight updates this way
# (e.g. weight_new = weight_old - learning_rate * gradient)
print("v1 + v2 =", v1 + v2)
print("v1 - v2 =", v1 - v2)

# Dot product isn't just "multiply and sum" — it measures how much two
# vectors point in the same direction (their alignment/similarity).
# A high dot product = vectors agree; a dot product of 0 = vectors are
# perpendicular (unrelated). This exact idea powers cosine similarity
# (recommendation systems, search), and every single neuron in a neural
# network computes a dot product between inputs and weights before
# applying an activation — so this one operation is the atomic unit of ML.
dot = np.dot(v1, v2)
print("Dot product (v1 . v2) =", dot)


# ============================================================
# 2. MATRICES
# ============================================================
print("\n--- Matrix Multiplication vs Element-wise ---")

A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

# A @ B is TRUE matrix multiplication — rows of A combine with columns of B.
# This is how neural network layers transform data (input @ weights),
# and how linear transformations (rotate, scale, project) are applied.
print("A @ B (matrix multiplication) =\n", A @ B)

# A * B is element-wise — position (i,j) of A just multiplies with (i,j) of B.
# We show it right next to A @ B on purpose: they look similar but mean
# completely different things, and mixing them up is a classic ML bug
# (e.g. accidentally using * instead of @ silently breaks a whole model
# because shapes still "work" but the math is wrong).
print("A * B (element-wise) =\n", A * B)

print("\n--- Transpose ---")
# Transpose flips rows<->columns. We need this constantly to make shapes
# align for matrix multiplication (e.g. X.T @ X in regression below),
# and conceptually it's how we switch between "data as rows" vs
# "data as columns" representations.
print("A.T =\n", A.T)

print("\n--- Inverse ---")
# The inverse of A is the matrix that "undoes" A's transformation.
# We care about it because it lets us SOLVE linear systems (Ax = b => x = A_inv @ b)
# instead of guessing — this is the backbone of the Normal Equation demo below.
A_inv = np.linalg.inv(A)
print("A_inv =\n", A_inv)

# A @ A_inv should give the Identity matrix (does nothing when applied).
# We round because floating point arithmetic almost never lands on a
# perfect clean 1.0 / 0.0 — this is a real-world numerical computing
# gotcha, not a bug in our math.
print("A @ A_inv (rounded, should be Identity) =\n", np.round(A @ A_inv))


# ============================================================
# 3. EIGENVALUES / EIGENVECTORS
# ============================================================
print("\n--- Eigenvalues & Eigenvectors ---")

C = np.array([[4, 2], [1, 3]])

# Eigenvectors are the special directions a matrix only STRETCHES
# (doesn't rotate), and eigenvalues are how much it stretches them by.
# Why this matters: PCA (dimensionality reduction) finds the eigenvectors
# of a data's covariance matrix — these become the "principal directions"
# of maximum variance, letting us compress data (e.g. 1000 features -> 50)
# while keeping the most important information.
eigenvalues, eigenvectors = np.linalg.eig(C)
print("Eigenvalues =", eigenvalues)
print("Eigenvectors =\n", eigenvectors)


# ============================================================
# 4. MINI PRACTICAL DEMO — LINEAR REGRESSION (NORMAL EQUATION)
# ============================================================
print("\n--- Linear Regression via Normal Equation ---")

# Fake data: X (features with bias column), y (targets)
X = np.array([[1, 1], [1, 2], [1, 3], [1, 4]])  # bias column of 1s + 1 feature
y = np.array([3, 5, 7, 9])

# This single line IS machine learning's "hello world": it finds the best-fit
# line without any iterative training loop, gradient descent, or guessing.
# It works because it directly uses matrix inverse + transpose + multiplication
# to solve for the theta that minimizes squared error in one shot — proving
# that "training a model" can literally just be linear algebra.
theta = np.linalg.inv(X.T @ X) @ X.T @ y
print("theta (intercept, slope) =", theta)
# Data was generated as y = 2x + 1, so we expect theta ≈ [1, 2]