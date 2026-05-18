# Topic: Two Pointers
# Phase: —
# Week: LeetCode Easy
# Description: Remove duplicates from sorted array in-place, return count of unique elements.

# ── Solution ──────────────────────────────────────

def remove_duplicates(nums):

    k = 1  # first element is always unique

    for i in range(1, len(nums)):
        if nums[i] != nums[i - 1]:  # new unique found
            nums[k] = nums[i]       # place it at position k
            k += 1

    return k  # count of unique elements

# ── Main ──────────────────────────────────────────

def main():

    # Example 1
    nums = [1, 1, 2]
    k = remove_duplicates(nums)
    print("Example 1:", k, nums[:k])

    # Example 2
    nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    k = remove_duplicates(nums)
    print("Example 2:", k, nums[:k])

if __name__ == "__main__":
    main()