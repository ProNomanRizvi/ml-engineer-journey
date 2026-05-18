# Topic: Arrays & Hashing
# Phase: —
# Week: LeetCode Easy
# Description: Find two indices in nums that add up to target.

# ── Solution ──────────────────────────────────────

def two_sum(nums, target):

    seen = {}                           # stores {number: index}

    for i, num in enumerate(nums):

        complement = target - num       # what do I need?

        if complement in seen:          # did I see it before?
            return [seen[complement], i]

        seen[num] = i                   # store current number

    return []                           # no solution found

# ── Main ──────────────────────────────────────────

def main():
    print("Example 1:", two_sum([2, 7, 11, 15], 9))   # Expected: [0, 1]
    print("Example 2:", two_sum([3, 2, 4], 6))        # Expected: [1, 2]
    print("Example 3:", two_sum([3, 3], 6))           # Expected: [0, 1]

if __name__ == "__main__":
    main()