"""
# Topic: Trees - Binary Search Tree (BST)
# Phase: 3 - DSA
# Week: 3 - Day 1
# Description: BST implementation from scratch (insert, search)
"""


class Node:
    """
    Represents a single node in a Binary Search Tree.
    """

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BST:
    """
    Binary Search Tree implementation.
    """

    def __init__(self):
        self.root = None

    def insert(self, data):
        """
        Insert a new value into the BST.
        """

        new_node = Node(data)

        if self.root is None:
            self.root = new_node
            return

        current = self.root

        while True:
            # Go to left subtree
            if data < current.data:
                if current.left is None:
                    current.left = new_node
                    return
                current = current.left

            # Go to right subtree
            elif data > current.data:
                if current.right is None:
                    current.right = new_node
                    return
                current = current.right

            # Ignore duplicate values
            else:
                return

    def search(self, data):
        """
        Search for a value in the BST.
        Returns True if found, otherwise False.
        """

        current = self.root

        while current is not None:

            if data == current.data:
                return True

            elif data < current.data:
                current = current.left

            else:
                current = current.right

        return False


def main():
    print("=" * 45)
    print("BINARY SEARCH TREE (BST)")
    print("=" * 45)

    bst = BST()

    values = [50, 30, 70, 20, 40, 60, 80]

    print("\nInserting values:")
    for value in values:
        bst.insert(value)
        print(f"Inserted {value}")

    print("\nSearch Results:")

    test_values = [40, 25, 80]

    for value in test_values:
        found = bst.search(value)
        print(f"{value}: {found}")


if __name__ == "__main__":
    main()