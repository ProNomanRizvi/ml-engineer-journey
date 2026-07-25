# Topic: Linked Lists (Doubly)
# Phase: 3 - DSA
# Week: 2 - Day 2
# Description: Doubly Linked List implementation from scratch

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.tail = new_node
            return

        new_node.prev = self.tail
        self.tail.next = new_node
        self.tail = new_node

    def prepend(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.tail = new_node
            return

        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node

    def delete(self, data):
        current = self.head

        while current:
            if current.data == data:
                # If node to delete is head
                if current == self.head:
                    self.head = current.next
                    if self.head:
                        self.head.prev = None
                    else:
                        self.tail = None  # List is now empty
                # If node to delete is tail
                elif current == self.tail:
                    self.tail = current.prev
                    if self.tail:
                        self.tail.next = None
                    else:
                        self.head = None
                # Node is in the middle
                else:
                    current.prev.next = current.next
                    current.next.prev = current.prev

                return True
            current = current.next

        return False

    def print_forward(self):
        nodes = []
        current = self.head
        while current:
            nodes.append(str(current.data))
            current = current.next
        nodes.append("None")
        print(" <-> ".join(nodes))

    def print_backward(self):
        nodes = []
        current = self.tail
        while current:
            nodes.append(str(current.data))
            current = current.prev
        nodes.append("None")
        print(" <-> ".join(nodes))


def main():
    dll = DoublyLinkedList()

    print("=== Appending Values (10, 20, 30) ===")
    dll.append(10)
    dll.append(20)
    dll.append(30)

    print("\nPrint Forward:")
    dll.print_forward()

    print("Print Backward:")
    dll.print_backward()

    print("\n=== Deleting Middle Value (20) ===")
    dll.delete(20)

    print("\nPrint Forward after deletion:")
    dll.print_forward()

    print("Print Backward after deletion:")
    dll.print_backward()


if __name__ == "__main__":
    main()