import numpy as np


# ============================================
# Binomial Distribution
# ============================================

# We simulate:
# 10 coin flips per experiment
# 1000 independent experiments
# p = 0.5 because the coin is fair
#
# Each value in binomial_data represents
# the number of successful outcomes (Heads)
# in one experiment of 10 flips.

binomial_data = np.random.binomial(
    n=10,
    p=0.5,
    size=1000
)


# ============================================
# Experimental Mean
# ============================================

binomial_mean = np.mean(binomial_data)

print("Experimental Mean:", binomial_mean)


# ============================================
# Theoretical Expected Value
# ============================================

# For a binomial distribution:
#
# Expected Value = n * p
#
# n = number of trials
# p = probability of success
#
# Expected Value = 10 * 0.5
#                = 5

theoretical_mean = 10 * 0.5

print("Theoretical Mean:", theoretical_mean)


# ============================================
# Difference
# ============================================

difference = abs(binomial_mean - theoretical_mean)

print("Difference:", difference)


# ============================================
# Interpretation
# ============================================

# The experimental mean should be close to 5.
#
# It will usually NOT be exactly 5 because
# our 1000 experiments are randomly generated.
#
# Random sampling creates natural variation.
#
# If we increase the number of experiments,
# for example from 1,000 to 100,000,
# the experimental mean will generally get
# closer to the theoretical mean of 5.
#
# This demonstrates an important statistical idea:
#
# More random samples → experimental result
# generally approaches the theoretical expectation.