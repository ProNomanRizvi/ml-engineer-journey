# Topic: Two Pointers
# Phase: —
# Week: LeetCode Easy
# Description: Merge two sorted arrays into nums1 in-place, filling from the back.

# ── Solution ──────────────────────────────────────

def merge(nums1, m, nums2, n):

    p1 = m - 1      # last real element in nums1
    p2 = n - 1      # last element in nums2
    p  = m + n - 1  # last slot in nums1

    while p1 >= 0 and p2 >= 0:
        if nums1[p1] >= nums2[p2]:
            nums1[p] = nums1[p1]
            p1 -= 1
        else:
            nums1[p] = nums2[p2]
            p2 -= 1
        p -= 1

    while p2 >= 0:      # leftover nums2 elements
        nums1[p] = nums2[p2]
        p2 -= 1
        p  -= 1

# ── Main ──────────────────────────────────────────

def main():

    # Example 1
    nums1 = [1, 2, 3, 0, 0, 0]
    merge(nums1, 3, [2, 5, 6], 3)
    print("Example 1:", nums1)

    # Example 2
    nums1 = [1]
    merge(nums1, 1, [], 0)
    print("Example 2:", nums1)

    # Example 3
    nums1 = [0]
    merge(nums1, 0, [1], 1)
    print("Example 3:", nums1)

if __name__ == "__main__":
    main()