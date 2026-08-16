import numpy as np


# ============================================
# Central Tendency + Spread
# ============================================

data = np.array([23, 45, 12, 67, 34, 89, 21, 56, 78, 500])

# 500 is a deliberate outlier.
# Most values are between 12 and 89,
# but 500 is extremely large.


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


# ============================================
# Effect of the Outlier
# ============================================

# Mean uses every value in the dataset.
# Therefore, the extreme value 500 pulls
# the mean strongly upward.
#
# Median depends on the middle position
# after sorting the data.
# Therefore, it is much less affected by
# a single extreme outlier.
#
# Without 500:
# [12, 21, 23, 34, 45, 56, 67, 78, 89]
# Median = 45
#
# With 500:
# [12, 21, 23, 34, 45, 56, 67, 78, 89, 500]
# Median = (45 + 56) / 2 = 50.5
#
# The outlier greatly increases the mean,
# while the median remains relatively stable.