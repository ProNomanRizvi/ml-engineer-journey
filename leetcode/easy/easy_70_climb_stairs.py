# Topic: Dynamic Programming
# Phase: —
# Week: LeetCode Easy
# Description: Count the number of distinct ways to climb n stairs, taking 1 or 2 steps at a time.

# ── Solution ──────────────────────────────────────

def climb_stairs(n):

    if n == 1:
        return 1
    if n == 2:
        return 2

    prev2 = 1
    prev1 = 2

    for i in range(3, n + 1):
        current = prev1 + prev2
        prev2 = prev1
        prev1 = current

    return prev1

# ── Main ──────────────────────────────────────────

def main():
    print("Example 1:", climb_stairs(2))   # Expected: 2
    print("Example 2:", climb_stairs(3))   # Expected: 3
    print("Bonus n=5:", climb_stairs(5))   # Expected: 8

if __name__ == "__main__":
    main()