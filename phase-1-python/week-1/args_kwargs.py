# Topic: *args and **kwargs
# Phase: 1 — Python Complete Mastery
# Week: 1
# Description: Practice using *args and **kwargs with real examples

# ── *args SECTION ─────────────────────────────────────────

def show_args(*args):
    for arg in args:
        print(f"- {arg}")

def count_args(*args):
    return len(args)

def first_and_last(*args):
    if len(args) == 0:
        print("No arguments provided.")
        return
    if len(args) == 1:
        print(f"Only one argument: {args[0]}")
        return
    print(f"First argument: {args[0]}")
    print(f"Last argument: {args[-1]}")

def multiply_all(*args):
    total = 1
    for num in args:
        if not isinstance(num, (int, float)):
            raise TypeError(f"Expected number, got {type(num).__name__}")
        total *= num
    return total

def smart_summary(*args):
    total = len(args)
    numbers = []
    non_numbers = []
    for arg in args:
        if isinstance(arg, (int, float)):
            numbers.append(arg)
        else:
            non_numbers.append(arg)
    print(f"Total: {total}")
    print(f"Numbers: {numbers}")
    print(f"Non-numbers: {non_numbers}")


# ── **kwargs SECTION ──────────────────────────────────────

def show_kwargs(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

def count_kwargs(**kwargs):
    return len(kwargs)

def build_profile(name, **kwargs):
    profile = {"name": name}
    profile.update(kwargs)
    for key, value in profile.items():
        print(f"{key}: {value}")

def merge_configs(default, override):
    return {**default, **override}

def strict_profile(**kwargs):
    required_keys = {"name", "age", "email"}
    allowed_keys = {"name", "age", "email", "city", "country"}
    provided_keys = set(kwargs.keys())
    missing = required_keys - provided_keys
    if missing:
        raise ValueError(f"Missing required fields: {', '.join(missing)}")
    extra = provided_keys - allowed_keys
    if extra:
        raise ValueError(f"Disallowed fields provided: {', '.join(extra)}")
    for key, value in kwargs.items():
        print(f"{key}: {value}")

def mixed(name, *args, **kwargs):
    print(f"Name: {name}")
    print(f"Positional extras: {args}")
    print(f"Keyword extras: {kwargs}")


# ── main() ────────────────────────────────────────────────

def main():
    # *args demos
    print("===== *args Section =====")

    print("\nQuestion 01:")
    show_args("Ali", "Noman", "Iqbal")

    print("\nQuestion 02:")
    print(f"Number of arguments: {count_args('Ali', 'Noman', 'Iqbal')}")

    print("\nQuestion 03:")
    print(f"Product of numbers: {multiply_all(2, 3, 4)}")

    print("\nQuestion 04:")
    first_and_last("Ali", "Noman", "Iqbal")

    print("\nQuestion 05:")
    smart_summary(1, 2, 3, "hello", "world")

    # **kwargs demos
    print("\n===== **kwargs Section =====")

    print("\n1. Displaying Keyword Arguments:")
    show_kwargs(name="Alice", age=30, city="New York")

    print("\n2. Counting Keyword Arguments:")
    print(f"Number of keyword arguments: {count_kwargs(name='Bob', profession='Developer')}")

    print("\n3. Building a User Profile:")
    build_profile("Charlie", age=25, hobby="Photography", language="Python")

    print("\n4. Merging Configuration Dictionaries:")
    default_config = {"host": "localhost", "port": 8080, "debug": False}
    override_config = {"port": 9090, "debug": True}
    merged_config = merge_configs(default_config, override_config)
    for key, value in merged_config.items():
        print(f"{key}: {value}")

    print("\n5. Strict Profile with Validation:")
    try:
        strict_profile(name="Diana", age=28, email="noman@example.com")
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()