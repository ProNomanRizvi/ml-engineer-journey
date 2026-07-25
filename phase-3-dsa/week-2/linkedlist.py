# Topic: Linked Lists (Singly) with Tail Pointer
# Phase: 3 - DSA
# Week: 2 - Day 1
# Description: Singly Linked List with O(1) append using tail pointer

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.tail = new_node
            return

        # Direct pointer update: O(1) time
        self.tail.next = new_node
        self.tail = new_node

    def prepend(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.tail = new_node
            return

        new_node.next = self.head
        self.head = new_node

    def delete(self, data):
        if not self.head:
            return False

        # If deleting head node
        if self.head.data == data:
            if self.head == self.tail:
                self.head = None
                self.tail = None
            else:
                self.head = self.head.next
            return True

        current = self.head
        while current.next:
            if current.next.data == data:
                # Update tail if the last node is deleted
                if current.next == self.tail:
                    self.tail = current
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

    print("=== Appending Values (O(1)) ===")
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

    print("\n=== Deleting Tail Value (40) ===")
    ll.delete(40)
    ll.print_list()
    print("New tail data:", ll.tail.data if ll.tail else "None")

if __name__ == "__main__":
    main()