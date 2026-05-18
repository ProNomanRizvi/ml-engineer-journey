# Topic: Strings
# Phase: —
# Week: LeetCode Easy
# Description: Find the longest common prefix string amongst an array of strings.

# ── Solution ──────────────────────────────────────

def longest_common_prefix(strs):

    if not strs:
        return ""

    prefix = strs[0]

    for s in strs[1:]:

        while not s.startswith(prefix):
            prefix = prefix[:-1]
            if not prefix:
                return ""

    return prefix

# ── Main ──────────────────────────────────────────

def main():

    # Example 1
    print("Example 1:", longest_common_prefix(["flower", "flow", "flight"]))  # Expected: "fl"

    # Example 2
    print("Example 2:", longest_common_prefix(["dog", "racecar", "car"]))     # Expected: ""

    # Example 3
    print("Example 3:", longest_common_prefix(["interview", "interact", "interface"]))  # Expected: "inter"

if __name__ == "__main__":
    main()