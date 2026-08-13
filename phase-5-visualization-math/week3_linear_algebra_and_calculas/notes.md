# Week 2-3 — Linear Algebra

## Industry context
Entry-level ML roles require matrix multiplication, eigenvalues, and
vector spaces — not a graduate-level treatment, but enough to read a
model paper and understand what's happening. Every major ML algorithm
(linear regression, PCA, neural network layers) is linear algebra
translated into code; the goal here isn't proving theorems, it's
building the intuition to know why an algorithm converges or fails.

## Core concepts

**Vector**
An ordered list of numbers — a single data point with each number as a
dimension (e.g. `[bedrooms, area, price]`).

**Matrix**
A collection of vectors (rows) — a full dataset, or a set of weights in
a neural network layer.

**Dot product**
Not just "multiply and sum" — it measures how much two vectors point in
the same direction (alignment/similarity). A high dot product means the
vectors agree; zero means they're perpendicular (unrelated). This is
the exact mechanism behind cosine similarity (recommendation systems,
search, NLP embeddings) and the atomic operation inside every neuron in
a neural network (inputs · weights, before activation).

**Vector norm (magnitude)**
The "length" of a vector — literally `sqrt(dot(v, v))`, derived directly
from the dot product. Cosine similarity divides the dot product by both
vectors' norms to cancel out magnitude and keep only direction. Also
the basis of L2 regularization (Ridge), which penalizes large weights
by their norm to reduce overfitting.

**Matrix multiplication vs. element-wise multiplication**
- `A @ B` — true matrix multiplication (rows of A combine with columns
  of B). This is how neural network layers transform data
  (`input @ weights`) and how linear transformations are applied.
- `A * B` — element-wise (position `[i,j]` of A times position `[i,j]`
  of B). Easy to confuse with `@` — mixing them up is a classic ML bug
  because the shapes can still "work" while the math is completely wrong.

**Transpose (`A.T`)**
Flips rows and columns. Needed constantly to align shapes for matrix
multiplication (e.g. `X.T @ X` in regression) and to switch between
"data as rows" vs. "data as columns" representations.

**Inverse (`np.linalg.inv(A)`)**
The matrix that "undoes" A's transformation — `A @ A_inv = Identity`.
Lets us directly *solve* linear systems (`Ax = b` → `x = A_inv @ b`)
instead of guessing. Note: floating-point arithmetic rarely lands on a
perfectly clean 1.0/0.0, so verifying against the identity matrix needs
rounding — a real numerical-computing gotcha, not a math error.

**Eigenvalues / eigenvectors (`np.linalg.eig(A)`)**
A matrix is a transformation that stretches/rotates vectors. Eigenvectors
are the special directions a matrix only *stretches* (no rotation);
eigenvalues are how much they stretch by. This is the basis of PCA
(dimensionality reduction) — PCA finds the eigenvectors of a dataset's
covariance matrix, which become the "principal directions" of maximum
variance, letting high-dimensional data (e.g. 1000 features) be
compressed to a handful of components while keeping most of the signal.

**NumPy gotcha:** `np.linalg.eig()` always returns complex-typed values
(`5.+0.j`) even when the eigenvalues are real, since NumPy can't know in
advance whether a given matrix's eigenvalues will be real or complex.
`+0.j` just means the imaginary part is zero — use `.real` for a clean
real-number view.

## Task
`linear_algebra_basics.py`
- Vectors: addition, subtraction, dot product, and norm (with a manual
  `sqrt(dot(v, v))` check to confirm the two are mathematically the
  same operation).
- Matrices: `@` vs `*` shown side-by-side deliberately (to make the
  distinction visible), transpose, and inverse verified by rounding
  `A @ A_inv` back to the identity matrix.
- Eigenvalues/eigenvectors of a 2x2 matrix.
- Mini practical demo: Linear Regression via the Normal Equation
  (`theta = inv(X.T @ X) @ X.T @ y`) on data generated as `y = 2x + 1` —
  confirms the closed-form solution recovers `theta ≈ [1, 2]` without
  any gradient descent or training loop.

## Output
Console output only (no plots/files) — this topic is about verifying
mathematical relationships numerically, not visualization.