"""
# Topic: Arrays
# Phase: 3 - DSA
# Week: 1 - Day 1
# Description: Manual array operations (insert, delete, search)
"""


def insert_at(arr, index, value):
    """
    Insert a value at the given index by manually shifting elements.
    """

    if index < 0 or index > len(arr):
        print("Invalid index!")
        return arr

    # Increase array size
    arr.append(None)

    # Shift elements to the right
    i = len(arr) - 1
    while i > index:
        arr[i] = arr[i - 1]
        i -= 1

    # Insert value
    arr[index] = value

    return arr


def delete_at(arr, index):
    """
    Delete the element at the given index by manually shifting elements.
    """

    if index < 0 or index >= len(arr):
        print("Invalid index!")
        return arr

    # Shift elements to the left
    i = index
    while i < len(arr) - 1:
        arr[i] = arr[i + 1]
        i += 1

    # Remove last duplicate element
    arr.pop()

    return arr


def linear_search(arr, target):
    """
    Search for target using linear search.
    Return index if found, otherwise -1.
    """

    i = 0
    while i < len(arr):
        if arr[i] == target:
            return i
        i += 1

    return -1


def main():
    print("=" * 40)
    print("ARRAY OPERATIONS")
    print("=" * 40)

    arr = [10, 20, 30, 40, 50]

    print("\nOriginal Array:")
    print(arr)

    print("\n1. Insert 25 at index 2")
    insert_at(arr, 2, 25)
    print(arr)

    print("\n2. Delete element at index 4")
    delete_at(arr, 4)
    print(arr)

    print("\n3. Search for 40")
    index = linear_search(arr, 40)
    print(f"40 found at index: {index}")

    print("\n4. Search for 100")
    index = linear_search(arr, 100)
    print(f"100 found at index: {index}")


if __name__ == "__main__":
    main()