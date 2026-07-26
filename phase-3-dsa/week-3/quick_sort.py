"""
# Topic: Sorting - Quick Sort
# Phase: 3 - DSA
# Week: 3 - Day 4
# Description: Quick Sort implementation from scratch (pivot + partition)
"""


def partition(arr, low, high):
    """
    Partition the array using the last element as the pivot.
    """

    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]

    return i + 1


def quick_sort(arr, low, high):
    """
    Sort the array using the Quick Sort algorithm.
    """

    if low >= high:
        return

    pivot_index = partition(arr, low, high)

    quick_sort(arr, low, pivot_index - 1)
    quick_sort(arr, pivot_index + 1, high)


def main():
    print("=" * 40)
    print("QUICK SORT")
    print("=" * 40)

    arr = [10, 80, 30, 90, 40, 50, 70]

    print("\nBefore Sorting:")
    print(arr)

    quick_sort(arr, 0, len(arr) - 1)

    print("\nAfter Sorting:")
    print(arr)


if __name__ == "__main__":
    main()