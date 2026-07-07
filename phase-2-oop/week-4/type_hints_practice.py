"""
=========================================================
Project: Type Hints Practice
Concepts:
- Type Hints
- Optional
- Union
- Dictionary
- Functions

Author: Noman Rizvi
=========================================================
"""

from typing import Optional, Union


STUDENT_GRADES: dict[str, float] = {
    "S101": 88.5,
    "S102": 91.0,
    "S103": 79.5,
}

STUDENT_NAMES: dict[str, str] = {
    "S101": "Ali",
    "S102": "Sara",
    "S103": "Ahmed",
}


def find_student_grade(student_id: str) -> Optional[float]:
    return STUDENT_GRADES.get(student_id)


def calculate_average(grades: list[float]) -> float:
    if not grades:
        return 0.0

    return sum(grades) / len(grades)


def get_student_info(student_id: str) -> dict[str, Union[str, float, None]]:
    return {
        "name": STUDENT_NAMES.get(student_id, "Unknown"),
        "grade": find_student_grade(student_id),
    }


def main() -> None:
    student_id = "S102"

    grade = find_student_grade(student_id)

    if grade is not None:
        print(f"{student_id} Grade: {grade}")
    else:
        print(f"{student_id} not found.")

    average = calculate_average(list(STUDENT_GRADES.values()))
    print(f"\nAverage Grade: {average:.2f}")

    info = get_student_info(student_id)
    print("\nStudent Information:")
    print(info)

    print("\nSearching for a non-existing student...")

    missing_student = "S999"
    missing_grade = find_student_grade(missing_student)

    if missing_grade is not None:
        print(f"{missing_student} Grade: {missing_grade}")
    else:
        print(f"{missing_student} not found.")

    missing_info = get_student_info(missing_student)
    print(missing_info)


if __name__ == "__main__":
    main()