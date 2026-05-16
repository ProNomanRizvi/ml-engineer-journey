# Topic: Binary Search
# Phase: —
# Week: LeetCode Easy
# Description: Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

# ── Solution ──────────────────────────────────────


def search_insert(nums, target):

    left = 0
    right = len(nums) - 1

    while left <= right:

        mid = (left + right) // 2  # Find middle index

        if nums[mid] == target:    # Exact match found
            return mid

        elif nums[mid] < target:   # Target is in RIGHT half
            left = mid + 1

        else:                      # Target is in LEFT half
            right = mid - 1

    return left                    # Insert position

# ── Main ──────────────────────────────────────────
def main():
    # Example 1
    nums = [1, 3, 5, 6]
    target = 5
    print("Example 1:", search_insert(nums, target))  # Output: 2

    # Example 2
    nums = [1, 3, 5, 6]
    target = 2
    print("Example 2:", search_insert(nums, target))  # Output: 1

    # Example 3
    nums = [1, 3, 5, 6]
    target = 7
    print("Example 3:", search_insert(nums, target))  # Output: 4

if __name__ == "__main__":
    main()