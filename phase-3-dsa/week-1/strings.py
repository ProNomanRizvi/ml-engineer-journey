# Topic: Strings
# Phase: 3 - DSA
# Week: 1
# Description: Efficient string reversal using Two-Pointer technique (True O(n))

def reverse_string(s):
    chars = list(s)
    left, right = 0, len(chars) - 1
    
    # Swap characters moving inwards from both ends
    while left < right:
        chars[left], chars[right] = chars[right], chars[left]
        left += 1
        right -= 1
        
    return "".join(chars)

def main():
    test_str = "hello"
    result = reverse_string(test_str)
    print(f"Original: {test_str}")
    print(f"Reversed: {result}")

if __name__ == "__main__":
    main()