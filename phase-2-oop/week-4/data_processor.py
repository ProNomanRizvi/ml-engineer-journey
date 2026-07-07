"""
=========================================================
Project: Data Processor
Concepts:
- OOP
- Composition
- Dataclass
- Type Hints
- Optional
- Data Validation

Author: Noman Rizvi
=========================================================
"""

from dataclasses import dataclass
from typing import Optional


@dataclass
class ProcessingResult:
    mean: float
    minimum: float
    maximum: float
    valid_count: int
    invalid_count: int


class DataValidator:
    def is_valid(self, value: float) -> bool:
        return 0.0 <= value <= 1000.0


class DataProcessor:
    def __init__(self, data: list[float]) -> None:
        self.data = data
        self.validator = DataValidator()

    def clean_data(self) -> list[float]:
        return [
            value
            for value in self.data
            if self.validator.is_valid(value)
        ]

    def process(self) -> Optional[ProcessingResult]:
        valid_data = self.clean_data()

        if not valid_data:
            return None

        valid_count = len(valid_data)
        invalid_count = len(self.data) - valid_count
        mean = sum(valid_data) / valid_count

        return ProcessingResult(
            mean=mean,
            minimum=min(valid_data),
            maximum=max(valid_data),
            valid_count=valid_count,
            invalid_count=invalid_count,
        )


def print_result(result: ProcessingResult) -> None:
    print(f"Mean          : {result.mean:.2f}")
    print(f"Minimum       : {result.minimum:.2f}")
    print(f"Maximum       : {result.maximum:.2f}")
    print(f"Valid Count   : {result.valid_count}")
    print(f"Invalid Count : {result.invalid_count}")


def main() -> None:
    print("=== Test 1: Mixed Data ===")

    data: list[float] = [
        100.0,
        -50.0,
        250.0,
        1500.0,
        500.0,
        750.0,
    ]

    processor = DataProcessor(data)
    result = processor.process()

    if result is not None:
        print_result(result)
    else:
        print("No valid data.")

    print("\n=== Test 2: All Invalid Data ===")

    invalid_data: list[float] = [
        -100.0,
        -5.0,
        1500.0,
        2500.0,
    ]

    processor = DataProcessor(invalid_data)
    result = processor.process()

    if result is not None:
        print_result(result)
    else:
        print("No valid data.")


if __name__ == "__main__":
    main()