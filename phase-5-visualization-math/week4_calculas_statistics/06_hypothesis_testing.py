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

# ============================================
# Step 2: Descriptive Statistics
# ============================================

# Calculate the mean accuracy of Model A.
# Mean tells us the average performance
# across all 30 test runs.

model_a_mean = np.mean(model_a_scores)


# Calculate the standard deviation of Model A.
# Standard deviation tells us how much the
# accuracy scores vary from the average.

model_a_std = np.std(model_a_scores)


# Calculate the mean accuracy of Model B.

model_b_mean = np.mean(model_b_scores)


# Calculate the standard deviation of Model B.

model_b_std = np.std(model_b_scores)


# ============================================
# Print Results
# ============================================

print("\n--- Descriptive Statistics ---")

print("Model A Mean:", model_a_mean)
print("Model A Std:", model_a_std)

print("Model B Mean:", model_b_mean)
print("Model B Std:", model_b_std)


# ============================================
# Interpretation
# ============================================

# Model B should have a higher mean than Model A
# because we generated B with loc=0.87
# and A with loc=0.85.
#
# However, the difference in sample means alone
# does NOT prove that Model B is truly better.
#
# Random variation can cause one model to have
# a higher average in a particular sample.
#
# That is why we perform a hypothesis test
# in the next step.