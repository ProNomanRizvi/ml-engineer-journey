# Topic: Add Binary
# Phase: —
# Week: LeetCode Easy
# Description: Given two binary strings a and b, return their sum as a binary string.

# ── Solution ──────────────────────────────────────

def add_binary(a, b):

    i = len(a) - 1      # pointer for a (from right)
    j = len(b) - 1      # pointer for b (from right)
    carry = 0           # carry starts at 0
    result = []         # store bits right to left

    while i >= 0 or j >= 0 or carry:

        digit_a = int(a[i]) if i >= 0 else 0  # get digit or 0
        digit_b = int(b[j]) if j >= 0 else 0  # get digit or 0

        total = digit_a + digit_b + carry      # sum of bits + carry

        carry = total // 2                     # new carry
        result.append(total % 2)               # current bit

        i -= 1
        j -= 1

    return ''.join(map(str, result[::-1]))     # reverse and join

# ── Main ──────────────────────────────────────────
def main():
    # Example 1
    a = "11"
    b = "1"
    print("Example 1:", add_binary(a, b))  # Output: "100"

    # Example 2
    a = "1010"
    b = "1011"
    print("Example 2:", add_binary(a, b))  # Output: "10101"    

if __name__ == "__main__":
    main()