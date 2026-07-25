# Topic: Stacks and Queues (LinkedList-based)
# Phase: 3 - DSA
# Week: 2 - Day 3
# Description: Stack and Queue implementations using Nodes/LinkedList

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedStack:
    def __init__(self):
        self.top = None

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node
        print(f"Stack Push: {data}")

    def pop(self):
        if not self.top:
            print("Stack Pop: Stack is empty!")
            return None
        popped_data = self.top.data
        self.top = self.top.next
        print(f"Stack Pop: {popped_data}")
        return popped_data

    def print_stack(self):
        nodes = []
        current = self.top
        while current:
            nodes.append(str(current.data))
            current = current.next
        print("Stack (Top to Bottom):", " -> ".join(nodes) if nodes else "Empty")


class LinkedQueue:
    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self, data):
        new_node = Node(data)
        if not self.tail:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        print(f"Queue Enqueue: {data}")

    def dequeue(self):
        if not self.head:
            print("Queue Dequeue: Queue is empty!")
            return None
        dequeued_data = self.head.data
        self.head = self.head.next
        if not self.head:
            self.tail = None
        print(f"Queue Dequeue: {dequeued_data}")
        return dequeued_data

    def print_queue(self):
        nodes = []
        current = self.head
        while current:
            nodes.append(str(current.data))
            current = current.next
        print("Queue (Front to Rear):", " -> ".join(nodes) if nodes else "Empty")


def main():
    print("=== Testing LinkedList-Based Stack (LIFO) ===")
    stack = LinkedStack()
    stack.push(10)
    stack.push(20)
    stack.push(30)
    stack.print_stack()
    stack.pop()
    stack.print_stack()

    print("\n=== Testing LinkedList-Based Queue (FIFO) ===")
    queue = LinkedQueue()
    queue.enqueue("A")
    queue.enqueue("B")
    queue.enqueue("C")
    queue.print_queue()
    queue.dequeue()
    queue.print_queue()


if __name__ == "__main__":
    main()