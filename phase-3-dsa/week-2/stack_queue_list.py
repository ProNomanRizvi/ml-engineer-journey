# Topic: Stacks and Queues (List-based)
# Phase: 3 - DSA
# Week: 2 - Day 3
# Description: Stack and Queue implementations using Python lists

class ListStack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)
        print(f"Stack Push: {item}")

    def pop(self):
        if self.is_empty():
            print("Stack Pop: Stack is empty!")
            return None
        item = self.items.pop()
        print(f"Stack Pop: {item}")
        return item

    def is_empty(self):
        return len(self.items) == 0

    def print_stack(self):
        print("Stack (Top to Bottom):", self.items[::-1])


class ListQueue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)
        print(f"Queue Enqueue: {item}")

    def dequeue(self):
        if self.is_empty():
            print("Queue Dequeue: Queue is empty!")
            return None
        item = self.items.pop(0)
        print(f"Queue Dequeue: {item}")
        return item

    def is_empty(self):
        return len(self.items) == 0

    def print_queue(self):
        print("Queue (Front to Rear):", self.items)


def main():
    print("=== Testing List-Based Stack (LIFO) ===")
    stack = ListStack()
    stack.push(10)
    stack.push(20)
    stack.push(30)
    stack.print_stack()
    stack.pop()
    stack.print_stack()

    print("\n=== Testing List-Based Queue (FIFO) ===")
    queue = ListQueue()
    queue.enqueue("A")
    queue.enqueue("B")
    queue.enqueue("C")
    queue.print_queue()
    queue.dequeue()
    queue.print_queue()


if __name__ == "__main__":
    main()