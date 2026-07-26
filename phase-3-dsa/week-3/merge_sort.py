"""
# Topic: Sorting - Merge Sort
# Phase: 3 - DSA
# Week: 3 - Day 3
# Description: Merge Sort implementation from scratch (divide and conquer)
"""


def merge(left, right):
    """
    Merge two sorted lists into one sorted list.
    """

    result = []
    i = 0
    j = 0

    # Compare elements from both lists
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # Add remaining elements from left list
    while i < len(left):
        result.append(left[i])
        i += 1

    # Add remaining elements from right list
    while j < len(right):
        result.append(right[j])
        j += 1

    return result


def merge_sort(arr):
    """
    Sort an array using Merge Sort.
    """

    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2

    left_half = arr[:mid]
    right_half = arr[mid:]

    left_sorted = merge_sort(left_half)
    right_sorted = merge_sort(right_half)

    return merge(left_sorted, right_sorted)


def main():
    print("=" * 40)
    print("MERGE SORT")
    print("=" * 40)

    arr = [38, 27, 43, 3, 9, 82, 10]

    print("\nBefore Sorting:")
    print(arr)

    sorted_arr = merge_sort(arr)

    print("\nAfter Sorting:")
    print(sorted_arr)


if __name__ == "__main__":
    main()