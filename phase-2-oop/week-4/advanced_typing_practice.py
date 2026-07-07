"""
=========================================================
Project: Advanced Type Hints Practice
Concepts:
- Protocol
- Generic
- TypeVar
- Annotated
- Type Aliases

Author: Noman Rizvi
=========================================================
"""

from typing import Annotated, Generic, Protocol, TypeVar
import math


class Shape(Protocol):
    def area(self) -> float:
        ...


class Circle:
    def __init__(self, radius: float) -> None:
        self.radius = radius

    def area(self) -> float:
        return math.pi * self.radius ** 2


class Square:
    def __init__(self, side: float) -> None:
        self.side = side

    def area(self) -> float:
        return self.side ** 2


def print_area(shape: Shape) -> None:
    print(f"Area: {shape.area():.2f}")


T = TypeVar("T")


class Container(Generic[T]):
    def __init__(self) -> None:
        self._items: list[T] = []

    def add_item(self, item: T) -> None:
        self._items.append(item)

    def get_items(self) -> list[T]:
        return self._items


Percentage = Annotated[float, "Value between 0 and 100"]


def apply_discount(price: float, discount: Percentage) -> float:
    return price - (price * discount / 100)


def main() -> None:
    print("=== Protocol Example ===")
    circle = Circle(radius=5.0)
    square = Square(side=4.0)

    print_area(circle)
    print_area(square)

    print("\n=== Generic Example ===")
    int_container: Container[int] = Container()
    int_container.add_item(10)
    int_container.add_item(20)
    print(f"Integers: {int_container.get_items()}")

    str_container: Container[str] = Container()
    str_container.add_item("Python")
    str_container.add_item("ML")
    print(f"Strings: {str_container.get_items()}")

    print("\n=== Annotated Example ===")
    original_price = 1000.0
    final_price = apply_discount(original_price, 15.0)

    print(f"Original Price : {original_price}")
    print(f"Final Price    : {final_price}")


if __name__ == "__main__":
    main()