# Topic: Linked Lists (Singly)
# Phase: 3 - DSA
# Week: 2 - Day 1
# Description: Singly Linked List implementation from scratch

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def delete(self, data):
        if not self.head:
            return False

        # If the head node itself holds the data to be deleted
        if self.head.data == data:
            self.head = self.head.next
            return True

        # Search for the node to delete and adjust pointer
        current = self.head
        while current.next:
            if current.next.data == data:
                current.next = current.next.next
                return True
            current = current.next

        return False

    def print_list(self):
        nodes = []
        current = self.head
        while current:
            nodes.append(str(current.data))
            current = current.next
        nodes.append("None")
        print(" -> ".join(nodes))

def main():
    ll = LinkedList()

    print("=== Appending Values ===")
    ll.append(20)
    ll.append(30)
    ll.append(40)
    ll.print_list()

    print("\n=== Prepending Value ===")
    ll.prepend(10)
    ll.print_list()

    print("\n=== Deleting Value (30) ===")
    ll.delete(30)
    ll.print_list()

if __name__ == "__main__":
    main()