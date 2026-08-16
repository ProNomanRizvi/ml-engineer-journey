import numpy as np


# ============================================
# Step 1: Generate Fake Model Accuracy Scores
# ============================================

# Fix the random seed so that we get the same
# random results every time we run the program.
#
# This is important for reproducibility.
# In ML experiments, reproducibility allows us
# to compare and debug experiments consistently.

np.random.seed(42)


# ============================================
# Model A
# ============================================

# Generate 30 accuracy scores.
#
# loc=0.85  -> average accuracy is expected
#              to be around 85%
#
# scale=0.03 -> scores naturally vary around
#               the mean by about 3 percentage points
#
# size=30 -> 30 different test runs

model_a_scores = np.random.normal(
    loc=0.85,
    scale=0.03,
    size=30
)


# ============================================
# Model B
# ============================================

# Model B is expected to perform slightly better.
#
# Average is around 87%, but there is overlap
# between Model A and Model B because both models
# have the same standard deviation.

model_b_scores = np.random.normal(
    loc=0.87,
    scale=0.03,
    size=30
)


# ============================================
# Print the generated scores
# ============================================

print("Model A Scores:")
print(model_a_scores)

print("\nModel B Scores:")
print(model_b_scores)