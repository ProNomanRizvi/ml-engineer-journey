# Topic: Nested Functions
# Phase: 1 — Python Complete Mastery
# Week: 1
# Description: Practice defining and using nested functions, understanding scope, and creating closures

# -- Defining a nested function---
def demo_basic_nested_function():
    def inner():
        print("I am inner")
    inner()


def demo_enclosing_scope():
    x = 10          # enclosing scope variable
    def inner():
        print(x)    # accesses enclosing scope — valid
    inner()


def demo_nonlocal_modification():
    count = 0
    def increment():
        nonlocal count   # tells Python: use the enclosing one
        count += 1
    increment()
    increment()
    print(count)  # 2


def make_multiplier(factor):
    def multiply(x):
        return x * factor   # factor is remembered
    return multiply         # returning the function itself


# TASKS 

def demo_simple_nested():
    def inner():
        print("Hello from inner")

    inner()


def make_adder(n):
    def inner(x):
        return x + n
    return inner


def make_counter():
    count = 0
    def inner():
        nonlocal count
        count += 1
        return count
    return inner


def apply_twice(func, value):
    result = func(value)
    return func(result)


def make_validator(min_val, max_val):
    def validate(value):
        if min_val <= value <= max_val:
            return "Valid"
        elif value < min_val:
            return "Too Low"
        elif value > max_val:
            return "Too High"
    return validate


def make_pipeline(*funcs):
    def pipeline(value):
        for func in funcs:
            value = func(value)
        return value
    return pipeline


def main():
    # Initial demonstrations
    demo_basic_nested_function()  # I am inner

    demo_enclosing_scope()  # 10

    demo_nonlocal_modification()  # 2

    # Multiplier example
    double = make_multiplier(2)
    triple = make_multiplier(3)

    print(double(5))   # 10
    print(triple(5))   # 15

    # Task examples
    demo_simple_nested()

    add_5 = make_adder(5)
    print(add_5(10))

    counter = make_counter()
    print(counter())
    print(counter())
    print(counter())

    doub = apply_twice(lambda x: x**2, 5)
    print(doub)

    child_age = make_validator(0, 12)
    teen_age = make_validator(13, 17)
    adult_age = make_validator(18, 120)
    print(child_age(5))   # Valid
    print(child_age(15))  # Too High
    print(teen_age(12)) # Too High
    print(teen_age(15))
    print(adult_age(10))
    print(adult_age(45))

    pipeline = make_pipeline(
        lambda x: x * 2,
        lambda x: x + 10,
        lambda x: x ** 2,
    )
    print(pipeline(3))  # ((3 * 2) + 10) ** 2 = 256


if __name__ == "__main__":
    main()