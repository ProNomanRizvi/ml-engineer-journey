# Topic: Binary Search
# Phase: —
# Week: LeetCode Easy
# Description: Implement int sqrt(int x) which computes and returns the square root of x, where x is guaranteed to be a non-negative integer. Since the return type is an integer, the decimal digits are truncated and only the integer part of the result is returned.

# ── Solution ──────────────────────────────────────

def my_sqrt(x):

    if x == 0:
        return 0

    left = 1
    right = x
    result = 0              # stores best valid answer so far

    while left <= right:

        mid = (left + right) // 2

        if mid * mid == x:          # perfect square
            return mid

        elif mid * mid < x:         # mid too small → go right
            result = mid            # save as candidate
            left = mid + 1

        else:                       # mid too big → go left
            right = mid - 1

    return result                   # floor of sqrt(x)

# ── Main ──────────────────────────────────────────
def main():
    # Example 1
    x = 4
    print("Example 1:", my_sqrt(x))  # Output: 2

    # Example 2
    x = 8
    print("Example 2:", my_sqrt(x))  # Output: 2

    # Example 3
    x = 0
    print("Example 3:", my_sqrt(x))  # Output: 0    

if __name__ == "__main__":
    main()