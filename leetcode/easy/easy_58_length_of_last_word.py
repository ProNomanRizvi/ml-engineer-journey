# Topic: Length of Last Word
# Phase: —
# Week: LeetCode Easy
# Description: Given a string s consisting of words and spaces, return the length of the last word in the string. A word is a maximal substring consisting of non-space characters only.

# ── Solution ──────────────────────────────────────

def length_of_last_word(s):

    s = s.rstrip()          # Remove trailing spaces from right
    
    length = 0              # Counter for last word length
    i = len(s) - 1          # Start from the last character

    while i >= 0 and s[i] != ' ':   # Walk left until space or start
        length += 1
        i -= 1

    return length

# ── Main ──────────────────────────────────────────
def main():
    # Example 1
    s = "Hello World"
    print("Example 1:", length_of_last_word(s))  # Output: 5

    # Example 2
    s = "   fly me   to   the moon  "
    print("Example 2:", length_of_last_word(s))  # Output: 4

    # Example 3
    s = "luffy is still joyboy"
    print("Example 3:", length_of_last_word(s))  # Output: 6

if __name__ == "__main__":
    main()