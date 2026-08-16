# ============================================
# Bayes' Theorem — Medical Test
# ============================================


# ============================================
# Given Probabilities
# ============================================

# Disease is rare:
# Only 1% of the population has the disease.

p_disease = 0.01

# Probability of a positive test
# when the person actually has the disease.
#
# This is the sensitivity of the test.

p_positive_given_disease = 0.95

# Probability of a positive test
# when the person does NOT have the disease.
#
# This is the false positive rate.

p_positive_given_no_disease = 0.10


# Probability of NOT having the disease
p_no_disease = 1 - p_disease


# ============================================
# Step 1: Calculate P(Positive)
# ============================================

# Total Law of Probability:
#
# P(positive) =
#
# P(positive | disease) * P(disease)
# +
# P(positive | no disease) * P(no disease)

p_positive = (
    p_positive_given_disease * p_disease
    + p_positive_given_no_disease * p_no_disease
)


print("P(Positive):", p_positive)
print("P(Positive) %:", p_positive * 100)


# ============================================
# Step 2: Apply Bayes' Theorem
# ============================================

# Bayes' theorem:
#
# P(disease | positive) =
#
# P(positive | disease) * P(disease)
# -----------------------------------
#             P(positive)

p_disease_given_positive = (
    p_positive_given_disease * p_disease
) / p_positive


print("P(Disease | Positive):", p_disease_given_positive)
print(
    "P(Disease | Positive) %:",
    p_disease_given_positive * 100
)


# ============================================
# Why is the result surprising?
# ============================================

# The result is only about 8.76%.
#
# Many people incorrectly assume:
#
# "The test is 95% accurate,
# so a positive result means
# there is a 95% chance of disease."
#
# That is WRONG.
#
# The disease is very rare:
# only 1% of people have it.
#
# Imagine 10,000 people:
#
# 100 people have the disease.
# 9,900 people do not have the disease.
#
# Of the 100 diseased people:
# 95 test positive.
#
# Of the 9,900 healthy people:
# 990 test positive falsely.
#
# Total positive tests:
# 95 + 990 = 1,085
#
# Actual diseased people among positives:
# 95
#
# Therefore:
#
# 95 / 1085 ≈ 8.76%
#
# This demonstrates the BASE-RATE EFFECT.
#
# The prior probability (1% disease prevalence)
# strongly affects the final probability.