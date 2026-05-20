# Topic: Linked List
# Phase: —
# Week: LeetCode Easy
# Description: Remove duplicates from a sorted linked list so each element appears only once.

# ── Solution ──────────────────────────────────────

def delete_duplicates(head):

    if not head:
        return head

    current = head

    while current and current.next:
        if current.val == current.next.val:  # duplicate found
            current.next = current.next.next  # skip it
        else:
            current = current.next  # move forward

    return head

# ── Main ──────────────────────────────────────────

def make_list(values):
    if not values:
        return None
    head = type('Node', (), {'val': values[0], 'next': None})()
    current = head
    for v in values[1:]:
        current.next = type('Node', (), {'val': v, 'next': None})()
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
    print_list(delete_duplicates(make_list([1, 1, 2])))

    # Example 2
    print("Example 2:", end=" ")
    print_list(delete_duplicates(make_list([1, 1, 2, 3, 3])))

    # Example 3
    print("Example 3:", end=" ")
    print_list(delete_duplicates(make_list([1, 1, 1, 2])))

if __name__ == "__main__":
    main()