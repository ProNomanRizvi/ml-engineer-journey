# Topic: Plus One
# Phase: —
# Week: LeetCode Easy
# Description: Given a non-empty array of decimal digits representing a non-negative integer, increment one to the integer. The digits are stored such that the most significant digit is at the head of the list, and each element in the array contains a single digit. You may assume the integer does not contain any leading zero, except the number 0 itself.
# ── Solution ──────────────────────────────────────

def plus_one(digits):

    # Go from last digit to first digit (right to left)
    for i in range(len(digits) - 1, -1, -1):

        if digits[i] < 9:       # No carry needed
            digits[i] += 1
            return digits       # Done immediately!

        digits[i] = 0           # 9 + 1 = 10 → write 0, carry left

    # If we reach here, all digits were 9
    # e.g. [9,9,9] → [0,0,0] → need [1,0,0,0]
    return [1] + digits

# ── Main ──────────────────────────────────────────
def main():
    # Example 1
    digits = [1, 2, 3]
    print("Example 1:", plus_one(digits))  # Output: [1, 2, 4]

    # Example 2
    digits = [4, 3, 2, 1]
    print("Example 2:", plus_one(digits))  # Output: [4, 3, 2, 2]

    # Example 3
    digits = [9]
    print("Example 3:", plus_one(digits))  # Output: [1, 0]

if __name__ == "__main__":
    main()