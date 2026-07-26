"""
# Topic: Binary Search
# Phase: 3 - DSA
# Week: 2 - Day 4
# Description: Binary Search implementation (iterative) on sorted array
"""


def binary_search(arr, target):
    """
    Perform iterative binary search on a sorted array.

    Returns:
        Index of target if found, otherwise -1.
    """

    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            return mid

        elif arr[mid] < target:
            low = mid + 1

        else:
            high = mid - 1

    return -1


def main():
    print("=" * 40)
    print("BINARY SEARCH")
    print("=" * 40)

    arr = [10, 20, 30, 40, 50, 60, 70]

    print("\nSorted Array:")
    print(arr)

    test_targets = [40, 25, 10, 70]

    for target in test_targets:
        index = binary_search(arr, target)

        if index != -1:
            print(f"\nTarget {target} found at index {index}")
        else:
            print(f"\nTarget {target} not found")


if __name__ == "__main__":
    main()