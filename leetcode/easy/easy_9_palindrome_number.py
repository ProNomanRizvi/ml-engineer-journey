# Topic: Math
# Phase: —
# Week: LeetCode Easy
# Description: Return True if integer x reads the same forwards and backwards.

# ── Solution ──────────────────────────────────────

def is_palindrome(x):

    if x < 0 or (x % 10 == 0 and x != 0):
        return False

    reversed_half = 0

    while x > reversed_half:
        reversed_half = reversed_half * 10 + x % 10
        x //= 10

    return x == reversed_half or x == reversed_half // 10

# ── Main ──────────────────────────────────────────

def main():

    # Example 1
    print("Example 1:", is_palindrome(121))   # Expected: True

    # Example 2
    print("Example 2:", is_palindrome(-121))  # Expected: False

    # Example 3
    print("Example 3:", is_palindrome(10))    # Expected: False


if __name__ == "__main__":
    main()