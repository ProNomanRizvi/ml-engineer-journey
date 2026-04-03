# Topic: map() and filter()
# Phase: 1 — Python Complete Mastery
# Week: 1
# Description: Practice using map() and filter() with named functions and lambdas

# ── HELPER FUNCTIONS ──────────────────────────────────────

def square(x):
    return x ** 2

def is_even(x):
    return x % 2 == 0


# ── main() ────────────────────────────────────────────────

def main():

    numbers = [1, 2, 3, 4, 5]

    # ── 1. map() with named function ──────────────────────
    squared_numbers = list(map(square, numbers))
    print("Squared numbers (named function):", squared_numbers)
    # ── 2. map() with lambda ──────────────────────────────
    squared_numbers_lambda = list(map(lambda x: x ** 2, numbers))
    print("Squared numbers (lambda):", squared_numbers_lambda)

    # ── 3. map() on multiple iterables ───────────────────
    numbers1 = [1, 2, 3]
    numbers2 = [4, 5, 6]
    summed_numbers = list(map(lambda x, y: x + y, numbers1, numbers2))
    print("Summed numbers:", summed_numbers)

    # ── 4. filter() with named function ──────────────────
    even_numbers = list(filter(is_even, numbers))
    print("Even numbers (named function):", even_numbers)

    # ── 5. filter() with lambda ───────────────────────────
    even_numbers_lambda = list(filter(lambda x: x % 2 == 0, numbers))
    print("Even numbers (lambda):", even_numbers_lambda)

    # ── 6. Chaining map() and filter() ───────────────────
    chained_result = list(map(square, filter(is_even, numbers)))
    print("Squared even numbers (chained):", chained_result)

if __name__ == "__main__":
    main()