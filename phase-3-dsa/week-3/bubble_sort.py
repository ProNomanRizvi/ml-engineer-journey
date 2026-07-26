"""
# Topic: Sorting - Bubble Sort
# Phase: 3 - DSA
# Week: 3 - Day 2
# Description: Bubble Sort implementation from scratch
"""


def bubble_sort(arr):
    """
    Sort an array using Bubble Sort with early termination optimization.
    """

    n = len(arr)

    for i in range(n):
        is_sorted = True

        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                is_sorted = False

        if is_sorted:
            break

    return arr


def main():
    print("=" * 40)
    print("BUBBLE SORT")
    print("=" * 40)

    arr = [64, 34, 25, 12, 22, 11, 90]

    print("\nBefore Sorting:")
    print(arr)

    bubble_sort(arr)

    print("\nAfter Sorting:")
    print(arr)


if __name__ == "__main__":
    main()