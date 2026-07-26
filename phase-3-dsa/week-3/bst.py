"""
# Topic: Trees - Binary Search Tree (BST)
# Phase: 3 - DSA
# Week: 3 - Day 1
# Description: BST implementation from scratch (insert, search, traversals)
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    def insert(self, data):
        new_node = Node(data)

        if self.root is None:
            self.root = new_node
            return

        current = self.root

        while True:
            if data < current.data:
                if current.left is None:
                    current.left = new_node
                    return
                current = current.left

            elif data > current.data:
                if current.right is None:
                    current.right = new_node
                    return
                current = current.right

            else:
                return

    def search(self, data):
        current = self.root

        while current is not None:
            if data == current.data:
                return True
            elif data < current.data:
                current = current.left
            else:
                current = current.right

        return False

    # -----------------------------
    # Inorder Traversal
    # -----------------------------
    def inorder(self):
        result = []
        self._inorder_helper(self.root, result)
        return result

    def _inorder_helper(self, node, result):
        if node:
            self._inorder_helper(node.left, result)
            result.append(node.data)
            self._inorder_helper(node.right, result)

    # -----------------------------
    # Preorder Traversal
    # -----------------------------
    def preorder(self):
        result = []
        self._preorder_helper(self.root, result)
        return result

    def _preorder_helper(self, node, result):
        if node:
            result.append(node.data)
            self._preorder_helper(node.left, result)
            self._preorder_helper(node.right, result)

    # -----------------------------
    # Postorder Traversal
    # -----------------------------
    def postorder(self):
        result = []
        self._postorder_helper(self.root, result)
        return result

    def _postorder_helper(self, node, result):
        if node:
            self._postorder_helper(node.left, result)
            self._postorder_helper(node.right, result)
            result.append(node.data)


def main():
    bst = BST()

    values = [50, 30, 70, 20, 40, 60, 80]

    for value in values:
        bst.insert(value)

    print("Search 40:", bst.search(40))
    print("Search 25:", bst.search(25))

    print("\nInorder Traversal:")
    print(bst.inorder())

    print("\nPreorder Traversal:")
    print(bst.preorder())

    print("\nPostorder Traversal:")
    print(bst.postorder())


if __name__ == "__main__":
    main()