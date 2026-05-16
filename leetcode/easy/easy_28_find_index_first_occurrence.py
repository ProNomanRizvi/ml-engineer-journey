# Topic: String Searching
# Phase: —
# Week: LeetCode Easy
# Description: Find the index of the first occurrence of needle in haystack using a sliding window.

# ── Solution ──────────────────────────────────────

def str_str(haystack, needle):
    """
    Find the index of the first occurrence of needle in haystack.
    
    :type haystack: str
    :type needle: str
    :rtype: int
    """
    # Edge case: empty needle
    if not needle:
        return 0
    
    n = len(haystack)  # length of big string
    m = len(needle)    # length of small string
    
    # Slide window across haystack
    for i in range(n - m + 1):
        
        # Cut a slice of size m starting at i
        if haystack[i:i + m] == needle:
            return i   # Found it! Return the position
    
    return -1  # Never found

# ── Main ──────────────────────────────────────────
def main():
    # Example 1
    haystack = "hello"
    needle = "ll"
    print("Example 1:", str_str(haystack, needle))  # Output: 2

    # Example 2
    haystack = "aaaaa"
    needle = "bba"
    print("Example 2:", str_str(haystack, needle))  # Output: -1

    # Example 3
    haystack = ""
    needle = ""
    print("Example 3:", str_str(haystack, needle))  # Output: 0

if __name__ == "__main__":
    main()