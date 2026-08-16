import numpy as np


# ============================================
# Step 1: Central Tendency + Spread
# ============================================

data = np.array([23, 45, 12, 67, 34, 89, 21, 56, 78, 500])
# 500 is a deliberate outlier.
# Most values are between 12 and 89, but 500 is extremely large.


# Mean
mean = np.mean(data)

# Median
median = np.median(data)

# Standard deviation
std = np.std(data)


print("Data:", data)
print("Mean:", mean)
print("Median:", median)
print("Standard Deviation:", std)


# Why does the outlier affect the mean?
#
# Mean uses EVERY value in the dataset.
# Therefore, the very large value 500 pulls the mean upward.
#
# Median depends on the middle position after sorting.
# Therefore, one extreme value usually has much less effect on the median.
#
# Without the outlier:
# [12, 21, 23, 34, 45, 56, 67, 78, 89]
# Median = 45
#
# With the outlier:
# [12, 21, 23, 34, 45, 56, 67, 78, 89, 500]
# Median = (45 + 56) / 2 = 50.5
#
# So the outlier 500 pulls the MEAN strongly upward,
# while the MEDIAN remains relatively stable.

# ============================================
# Step 2: Normal Distribution
# ============================================

normal_data = np.random.normal(
    loc=100,
    scale=15,
    size=1000
)

# loc = theoretical mean
# scale = theoretical standard deviation
#
# We generated 1000 values from a normal distribution
# with mean = 100 and standard deviation = 15.


# Calculate actual mean and standard deviation
normal_mean = np.mean(normal_data)
normal_std = np.std(normal_data)

print("\n--- Normal Distribution ---")
print("Mean:", normal_mean)
print("Standard Deviation:", normal_std)


# The calculated values should be close to:
# Mean ≈ 100
# Standard deviation ≈ 15
#
# They will NOT be exactly 100 and 15 because
# we generated a random sample of only 1000 values.


# ============================================
# 68-95-99.7 Rule
# ============================================
#
# For a normal distribution:
#
# About 68% of data falls within:
# mean ± 1 standard deviation
#
# About 95% falls within:
# mean ± 2 standard deviations
#
# About 99.7% falls within:
# mean ± 3 standard deviations
#
# We verify this empirically using boolean masking.


# Within 1 standard deviation
within_1_std = (
    (normal_data >= normal_mean - normal_std)
    & (normal_data <= normal_mean + normal_std)
)

percentage_1_std = np.mean(within_1_std) * 100


# Within 2 standard deviations
within_2_std = (
    (normal_data >= normal_mean - 2 * normal_std)
    & (normal_data <= normal_mean + 2 * normal_std)
)

percentage_2_std = np.mean(within_2_std) * 100


# Within 3 standard deviations
within_3_std = (
    (normal_data >= normal_mean - 3 * normal_std)
    & (normal_data <= normal_mean + 3 * normal_std)
)

percentage_3_std = np.mean(within_3_std) * 100


print("\n--- 68-95-99.7 Rule ---")
print("Within 1 std:", percentage_1_std, "%")
print("Within 2 std:", percentage_2_std, "%")
print("Within 3 std:", percentage_3_std, "%")


# Expected approximate results:
#
# Within 1 std  ≈ 68%
# Within 2 std  ≈ 95%
# Within 3 std  ≈ 99.7%
#
# The results will vary slightly because the dataset
# is randomly generated.
#
# Why boolean masking?
# Each condition produces True/False values.
# np.mean(True/False) treats True as 1 and False as 0.
# Therefore, the mean gives us the fraction of values
# satisfying the condition.
#
# Example:
# [True, True, False, True]
# becomes [1, 1, 0, 1]
#
# Mean = 3 / 4 = 0.75 = 75%

# ============================================
# Step 3: Binomial Distribution
# ============================================

# 10 coin flips
# 1000 independent experiments
# p = 0.5 means fair coin
#
# Each experiment asks:
# "Out of 10 flips, how many times did we get Heads?"

binomial_data = np.random.binomial(
    n=10,
    p=0.5,
    size=1000
)


# Calculate the experimental mean
binomial_mean = np.mean(binomial_data)

print("\n--- Binomial Distribution ---")
print("Mean:", binomial_mean)


# ============================================
# Theoretical Expected Value
# ============================================

# For a binomial distribution:
#
# Expected Value (mean) = n * p
#
# n = number of trials = 10
# p = probability of success = 0.5
#
# Therefore:
#
# Expected Value = 10 * 0.5
#                = 5

theoretical_mean = 10 * 0.5

print("Theoretical Mean:", theoretical_mean)


# The experimental mean should be close to 5.
#
# Why isn't it exactly 5?
#
# Because binomial_data contains only 1000 random experiments.
# Random sampling naturally creates small differences.
#
# If we increased size from 1000 to 100000,
# the experimental mean would generally get even closer
# to the theoretical value of 5.


# ============================================
# Compare Experimental vs Theoretical
# ============================================

difference = abs(binomial_mean - theoretical_mean)

print("Difference:", difference)


# Small difference = experimental result is close
# to the theoretical expected value.
#
# This demonstrates an important statistical idea:
# with more random samples, experimental results tend
# to approach their theoretical expectations.

# ============================================
# Step 4: Bayes' Theorem — Medical Test
# ============================================

# Disease is rare:
# Only 1% of the population has the disease.

p_disease = 0.01

# Probability that the test is positive
# when the person actually has the disease.
# This is called sensitivity.

p_positive_given_disease = 0.95

# Probability that the test is positive
# when the person does NOT have the disease.
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
# P(positive | disease) * P(disease)
# +
# P(positive | no disease) * P(no disease)

p_positive = (
    p_positive_given_disease * p_disease
    + p_positive_given_no_disease * p_no_disease
)


print("\n--- Bayes' Theorem: Medical Test ---")
print("P(Positive):", p_positive)
print("P(Positive) %:", p_positive * 100)


# ============================================
# Step 2: Calculate P(Disease | Positive)
# ============================================

# Bayes' Theorem:
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

# The final probability is only about 8.76%.
#
# Even though the test has 95% sensitivity,
# a positive result does NOT mean there is a 95%
# chance that the person has the disease.
#
# Why?
#
# The disease is very rare:
# only 1% of people have it.
#
# The 10% false-positive rate is applied to the
# much larger group of healthy people.
#
# Imagine 10,000 people:
#
# 100 people have the disease.
# 9,900 people do not have the disease.
#
# Among the 100 diseased people:
# 95 test positive.
#
# Among the 9,900 healthy people:
# 990 test positive falsely.
#
# Total positive tests:
# 95 + 990 = 1,085
#
# Actual diseased people among positive tests:
# 95
#
# Therefore:
#
# 95 / 1085 ≈ 8.76%
#
# This is the key lesson of Bayes' theorem:
# the base rate (prior probability) matters.

# ============================================
# Step 5: Correlation
# ============================================

# x is normally distributed around 50
x = np.random.normal(50, 10, 100)

# y depends directly on x.
# We multiply x by 2 and then add some random noise.
#
# Because y changes when x changes,
# x and y should have a strong positive correlation.

y = x * 2 + np.random.normal(0, 5, 100)

# z is completely unrelated to x.
# It is generated independently from another
# normal distribution.

z = np.random.normal(50, 10, 100)


# ============================================
# Calculate Correlation
# ============================================

correlation_xy = np.corrcoef(x, y)
correlation_xz = np.corrcoef(x, z)


print("\n--- Correlation ---")

print("Correlation matrix (x, y):")
print(correlation_xy)

print("\nCorrelation matrix (x, z):")
print(correlation_xz)


# ============================================
# Extract the actual correlation coefficient
# ============================================

# np.corrcoef() returns a 2x2 correlation matrix:
#
# [[corr(x,x), corr(x,y)],
#  [corr(y,x), corr(y,y)]]
#
# The value at [0, 1] is the correlation
# between x and y.

corr_xy = np.corrcoef(x, y)[0, 1]
corr_xz = np.corrcoef(x, z)[0, 1]


print("\nCorrelation coefficient x,y:", corr_xy)
print("Correlation coefficient x,z:", corr_xz)


# ============================================
# Interpretation
# ============================================

# x and y:
# y = x * 2 + noise
#
# Therefore, when x increases, y generally increases.
# This creates a strong positive correlation.
#
# corr_xy should be close to +1.


# x and z:
# z has no relationship with x.
#
# Therefore, knowing x tells us almost nothing
# about z.
#
# corr_xz should be close to 0.


# Important:
# Correlation measures the strength and direction
# of a LINEAR relationship.
#
# Correlation close to +1:
# Strong positive linear relationship.
#
# Correlation close to -1:
# Strong negative linear relationship.
#
# Correlation close to 0:
# Little or no linear relationship.
#
# Correlation does NOT automatically mean causation.