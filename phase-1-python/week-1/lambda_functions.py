# Topic: Lambda Functions
# Phase: 1 — Python Complete Mastery
# Week: 1
# Description: Practice using lambda with map, filter, sorted


# ── LAMBDA DEFINITIONS ────────────────────────────────────


def create_multiplier(n):
    return lambda x: x * n


# ── main() ────────────────────────────────────────────────

def main():

    # ── 1. Basic Lambda ───────────────────────────────────
    print("===== 1. Basic Lambda =====")
    print(f"Square of 5: {(lambda x: x ** 2)(5)}")  # Output: 25

    # ── 2. Lambda with map() ──────────────────────────────
    print("\n===== 2. Lambda with map() =====")
    numbers = [1, 2, 3, 4, 5]
    squared_numbers = list(map(lambda x: x ** 2, numbers))
    print(f"Squared numbers: {squared_numbers}")  # Output: [1, 4, 9, 16, 25]

    # ── 3. Lambda with filter() ───────────────────────────
    print("\n===== 3. Lambda with filter() =====")
    even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
    print(f"Even numbers: {even_numbers}")  # Output: [2, 4]

    # ── 4. Lambda with sorted() ───────────────────────────
    print("\n===== 4. Lambda with sorted() =====")
    students = [("Alice", 85), ("Bob", 90), ("Charlie", 78)]
    sorted_by_score = sorted(students, key=lambda x: x[1], reverse=True)
    print(f"Sorted by score (desc): {sorted_by_score}")
    sorted_by_name = sorted(students, key=lambda x: x[0])
    print(f"Sorted by name  (asc):  {sorted_by_name}")

    # ── 5. Lambda inside a Function ───────────────────────
    print("\n===== 5. Lambda inside a Function =====")
    double = create_multiplier(2)
    triple = create_multiplier(3)
    print(f"Double 5: {double(5)}")  # Output: 10
    print(f"Triple 5: {triple(5)}")  # Output: 15

    # ─ 6. Lambda for Immediate Use ───────────────────────
    print("\n===== 6. Lambda for Immediate Use =====")
    print(f"Add 3 + 7: {(lambda x, y: x + y)(3, 7)}")

if __name__ == "__main__":
    main()