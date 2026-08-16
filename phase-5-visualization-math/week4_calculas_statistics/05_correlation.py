import numpy as np


# ============================================
# Correlation
# ============================================

# x is normally distributed around 50
x = np.random.normal(50, 10, 100)


# y depends on x.
# x is multiplied by 2 and random noise is added.
#
# Because y changes when x changes,
# x and y should have a strong positive
# linear correlation.

y = x * 2 + np.random.normal(0, 5, 100)


# z is completely unrelated to x.
# It is generated independently.

z = np.random.normal(50, 10, 100)


# ============================================
# Correlation Matrices
# ============================================

correlation_xy = np.corrcoef(x, y)
correlation_xz = np.corrcoef(x, z)


print("Correlation Matrix (x, y):")
print(correlation_xy)

print("\nCorrelation Matrix (x, z):")
print(correlation_xz)


# ============================================
# Extract Correlation Coefficients
# ============================================

# np.corrcoef() returns a 2x2 matrix:
#
# [[corr(x,x), corr(x,y)],
#  [corr(y,x), corr(y,y)]]
#
# The value [0, 1] gives the correlation
# between x and y.

corr_xy = np.corrcoef(x, y)[0, 1]
corr_xz = np.corrcoef(x, z)[0, 1]


print("\nCorrelation coefficient (x, y):", corr_xy)
print("Correlation coefficient (x, z):", corr_xz)


# ============================================
# Interpretation
# ============================================

# x and y:
#
# y = x * 2 + noise
#
# When x increases, y generally increases.
# Therefore, they should have a strong
# positive correlation.
#
# corr_xy should be close to +1.


# x and z:
#
# z has no relationship with x.
#
# Therefore, their correlation should be
# close to 0.
#
# corr_xz should usually be somewhere around 0.


# ============================================
# Important ML Concept
# ============================================

# Correlation measures the strength and direction
# of a LINEAR relationship between two variables.
#
# +1  → strong positive linear relationship
#  0  → no linear relationship
# -1  → strong negative linear relationship
#
# IMPORTANT:
#
# Correlation does NOT automatically mean causation.
#
# Two variables can be correlated without one
# actually causing the other.