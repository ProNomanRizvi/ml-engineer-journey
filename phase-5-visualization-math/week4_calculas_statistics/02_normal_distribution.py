import numpy as np


# ============================================
# Normal Distribution
# ============================================

normal_data = np.random.normal(
    loc=100,
    scale=15,
    size=1000
)

# loc = theoretical mean
# scale = theoretical standard deviation
# size = number of generated values
#
# We expect:
# Mean ≈ 100
# Standard deviation ≈ 15


# Calculate mean and standard deviation
normal_mean = np.mean(normal_data)
normal_std = np.std(normal_data)


print("Mean:", normal_mean)
print("Standard Deviation:", normal_std)


# ============================================
# 68-95-99.7 Rule
# ============================================

# In a normal distribution:
#
# Approximately 68% of data falls within
# mean ± 1 standard deviation.
#
# Approximately 95% falls within
# mean ± 2 standard deviations.
#
# Approximately 99.7% falls within
# mean ± 3 standard deviations.


# --------------------------------------------
# Within 1 Standard Deviation
# --------------------------------------------

within_1_std = (
    (normal_data >= normal_mean - normal_std)
    & (normal_data <= normal_mean + normal_std)
)

percentage_1_std = np.mean(within_1_std) * 100


# --------------------------------------------
# Within 2 Standard Deviations
# --------------------------------------------

within_2_std = (
    (normal_data >= normal_mean - 2 * normal_std)
    & (normal_data <= normal_mean + 2 * normal_std)
)

percentage_2_std = np.mean(within_2_std) * 100


# --------------------------------------------
# Within 3 Standard Deviations
# --------------------------------------------

within_3_std = (
    (normal_data >= normal_mean - 3 * normal_std)
    & (normal_data <= normal_mean + 3 * normal_std)
)

percentage_3_std = np.mean(within_3_std) * 100


# ============================================
# Print Results
# ============================================

print("\n68-95-99.7 Rule")

print("Within 1 std:", percentage_1_std, "%")
print("Within 2 std:", percentage_2_std, "%")
print("Within 3 std:", percentage_3_std, "%")


# ============================================
# Why Boolean Masking?
# ============================================

# Each comparison produces True or False.
#
# Example:
# [True, True, False, True]
#
# NumPy treats:
# True  = 1
# False = 0
#
# Therefore:
# mean([1, 1, 0, 1]) = 0.75
#
# 0.75 * 100 = 75%
#
# This allows us to calculate what percentage
# of the data satisfies a condition.
#
# Because the data is randomly generated,
# the results will not be exactly 68%, 95%,
# and 99.7%. They should be approximately
# those values.