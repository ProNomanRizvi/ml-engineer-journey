# Topic: list comprehensions
# Phase: 1 — Python Complete Mastery
# Week: 1
# Description: Practice using list comprehensions to create lists in a more concise and readable way



def main():

    # ── 1. Basic list comprehension ──────────────────────
    nums = [1,2,3,4,5]
    square = [num ** 2 for num in nums]
    print(f"Squared numbers: {square}")
    # ── 2. List comprehension with condition (filtering) ──────────────────────
    words = ["Happy", "Good", "Bad", "Banana", "Vegetables"]
    short_words = [word for word in words if len(word) <= 3]
    print(f"Short words: {short_words}")


    # ── 3. List comprehension with if-else (conditional expressions) ──────────────────────
    nums = [i for i in range(11)]
    is_even = ["Even" if x%2==0 else "Odd" for x in nums]
    print(f"Even and Odd numbers: {is_even}")

    # ── 4. Nested list comprehension ──────────────────────
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ] 
    greater_than_five = [num for row in matrix for num in row if num > 5]
    print(f"Numbers greater than 5: {greater_than_five}")

    # ── 5. Dictionary comprehension ──────────────────────
    names = ["Noman", "Ali", "Iqbal"]
    ages = [45, 41, 65]
    name_to_age = {name: age for name, age in zip(names, ages)}
    print(f"Name to Age mapping: {name_to_age}")

    # ── 6. Set comprehension ──────────────────────
    nums = [1, 2, 3, 4, 5, 5, 4]
    unique_squares = {num ** 2 for num in nums}
    print(f"Unique squares: {unique_squares}")

if __name__ == "__main__":
    main()