# Topic: Linked List
# Phase: —
# Week: LeetCode Easy
# Description: Merge two sorted linked lists into one sorted linked list.

# ── Solution ──────────────────────────────────────

def make_node(val):
    node = type('Node', (), {'val': val, 'next': None})()
    return node

def merge_two_lists(list1, list2):

    dummy = make_node(0)
    current = dummy

    while list1 and list2:

        if list1.val <= list2.val:
            current.next = list1
            list1 = list1.next
        else:
            current.next = list2
            list2 = list2.next

        current = current.next

    if list1:
        current.next = list1
    if list2:
        current.next = list2

    return dummy.next

# ── Main ──────────────────────────────────────────

def build_list(values):
    if not values:
        return None
    head = make_node(values[0])
    current = head
    for v in values[1:]:
        current.next = make_node(v)
        current = current.next
    return head

def print_list(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    print(result)

def main():

    # Example 1
    print("Example 1:", end=" ")
    print_list(merge_two_lists(build_list([1,2,4]), build_list([1,3,4])))  # Expected: [1,1,2,3,4,4]

    # Example 2
    print("Example 2:", end=" ")
    print_list(merge_two_lists(build_list([]), build_list([])))            # Expected: []

    # Example 3
    print("Example 3:", end=" ")
    print_list(merge_two_lists(build_list([]), build_list([0])))           # Expected: [0]

if __name__ == "__main__":
    main()