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