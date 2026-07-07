"""
=========================================================
Project: Person, Address, and Student
Concepts:
- Composition (Person has an Address)
- Inheritance (Student is a Person)

Author: Noman Rizvi
=========================================================
"""


class Address:
    def __init__(
        self,
        street: str,
        city: str,
        country: str,
    ) -> None:
        self.street = street
        self.city = city
        self.country = country

    def display(self) -> None:
        print(f"Address : {self.street}, {self.city}, {self.country}")


class Person:
    def __init__(
        self,
        name: str,
        age: int,
        address: Address,
    ) -> None:
        self.name = name
        self.age = age
        self.address = address

    def display(self) -> None:
        print(f"Name    : {self.name}")
        print(f"Age     : {self.age}")
        self.address.display()


class Student(Person):
    def __init__(
        self,
        name: str,
        age: int,
        address: Address,
        student_id: str,
    ) -> None:
        super().__init__(name, age, address)
        self.student_id = student_id

    def display(self) -> None:
        super().display()
        print(f"ID      : {self.student_id}")


def main() -> None:
    address = Address(
        street="Main Road",
        city="Rawalpindi",
        country="Pakistan",
    )

    student = Student(
        name="Rizvi",
        age=20,
        address=address,
        student_id="ML2026",
    )

    student.display()


if __name__ == "__main__":
    main()