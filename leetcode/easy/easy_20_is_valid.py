# Topic: Stack
# Phase: —
# Week: LeetCode Easy
# Description: Determine if a string of brackets is valid — correctly opened and closed.

# ── Solution ──────────────────────────────────────

def is_valid(s):

    matching = {')': '(', '}': '{', ']': '['}
    stack = []

    for char in s:

        if char in '([{':
            stack.append(char)

        else:
            if not stack or stack[-1] != matching[char]:
                return False
            stack.pop()

    return len(stack) == 0

# ── Main ──────────────────────────────────────────

def main():

    # Example 1
    print("Example 1:", is_valid("()"))        # Expected: True

    # Example 2
    print("Example 2:", is_valid("()[]{}"))    # Expected: True

    # Example 3
    print("Example 3:", is_valid("(]"))        # Expected: False

    # Example 4
    print("Example 4:", is_valid("{[]}"))      # Expected: True

    # Example 5
    print("Example 5:", is_valid("([)]"))      # Expected: False

if __name__ == "__main__":
    main()