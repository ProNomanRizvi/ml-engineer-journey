# Topic: Hash Map / Math
# Phase: —
# Week: LeetCode Easy
# Description: Convert a Roman numeral string to an integer.

# ── Solution ──────────────────────────────────────

def roman_to_int(s):

    roman = {
        'I': 1,   'V': 5,   'X': 10,
        'L': 50,  'C': 100, 'D': 500,
        'M': 1000
    }

    total = 0

    for i in range(len(s)):

        if i + 1 < len(s) and roman[s[i]] < roman[s[i + 1]]:
            total -= roman[s[i]]    # subtraction case
        else:
            total += roman[s[i]]    # normal addition

    return total

# ── Main ──────────────────────────────────────────

def main():
    
    # Example 1
    print("Example 1:", roman_to_int("III"))  # Expected: 3

    # Example 2
    print("Example 2:", roman_to_int("LVIII"))  # Expected: 58

    # Example 3
    print("Example 3:", roman_to_int("MCMXCIV"))  # Expected: 1994

if __name__ == "__main__":
    main()