# Topic: Error Handling
# Phase: 1 — Python Complete Mastery
# Week: 2
# Description: Understanding error handling in Python, using try-except blocks, raising exceptions, and best practices for handling errors

import json

def basic_error_handling():
    '''Demonstrates basic error handling using try-except blocks.'''
    print("=== Basic Error Handling ===\n")
    print("Attempting to divide by zero...")
    try:
        x = 10 / 0
    except ZeroDivisionError as e:
        print(f"Caught an error: {e}")

    print("\nCatching multiple exceptions...")
    try:
        value = int("abc")
    except ValueError:
        print("Not a valid integer")
    except TypeError:
        print("Wrong type entirely")

    print("\nUse of else block in try-except...")
    try:
        result = 10 / 2
    except ZeroDivisionError:
        print("Failed")
    else:
        print(f"Success: {result}")  # only runs if try succeeded    


    print("\nUse of finally block in try-except...")
    try:
        f = open("data.txt")
    except FileNotFoundError:
        print("File missing")
    finally:
        print("This always runs — use for cleanup")    

# ======== TASKS SECTION ========

# ── Task 1: Basic Division ────────────────────────────
def divide_numbers(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        return "Error: Cannot divide by zero"
    except TypeError:
        return "Error: Invalid data type"

# ── Task 2: File Reading with Error Handling ─────────
def read_file(filepath):
    try:
        with open(filepath, "r") as file:
            content = file.read()
    except FileNotFoundError:
        return "Error: File not found"
    else:
        return content

# ── Task 3: List Indexing with Error Handling ───────
def get_element(lst, index):
    try:
        return lst[index]
    except IndexError:
        return "Error: Index out of range"
    except TypeError:
        return "Error: Invalid input type"
    except Exception as e:
        return f"General Error: {e}"

# ── Task 4: Age Validation with Custom Exception ───────
def validate_age(age):
    if age < 0 or age > 150:
        raise ValueError("Invalid age: must be between 0 and 150")
    return f"Valid age: {age}"

# ── Task 5: Withdraw Money with Custom Exception ───────
def withdraw(balance, amount):
    if amount > balance:
        raise ValueError("Withdrawal amount exceeds balance")
    return balance - amount

# ── Task 6: JSON File Processing with Multiple Exceptions ───────
def process_json_file(filepath):
    try:
        with open(filepath, "r") as file:
            data = json.load(file)

        number = data["number"]
        result = 100 / number
        return result

    except FileNotFoundError:
        return "Error: File not found"
    except json.JSONDecodeError:
        return "Error: Invalid JSON format"
    except KeyError:
        return "Error: 'number' key missing in JSON"
    except ZeroDivisionError:
        return "Error: Division by zero"
    except Exception as e:
        return f"Unexpected Error: {e}"



# =====================================================
def main():
    basic_error_handling()

    # TASK 1: 
    print("=== Task 1: Divide Numbers ===\n")
    print(f"10 / 2 = {divide_numbers(10, 2)}")
    print(f"10 / 0 = {divide_numbers(10, 0)}")
    print(f"10 / 'a' = {divide_numbers(10, 'a')}")

    # TASK 2:
    print("\n=== Task 2: Read File ===\n")
    print(read_file("data.txt"))
    print(read_file("nonexistent.txt"))

    # TASK 3:
    print("\n=== Task 3: Get Element from List ===\n")
    my_list = [1, 2, 3, 4, 5]
    print(get_element(my_list, 2))
    print(get_element(my_list, 10))
    print(get_element(my_list, "a"))

    # TASK 4:
    print("\n=== Task 4: Validate Age ===\n")
    ages = [25, -5, 200]
    for age in ages:
        try:
            print(validate_age(age))
        except ValueError as e:
            print(f"Error: {e}")

    # TASK 5:
    print("\n=== Task 5: Withdraw Money ===\n")
    try:
        print(withdraw(100, 30))  
        print(withdraw(100, 150))  
    except ValueError as e:
        print(f"Error: {e}")

    # TASK 6:
    print("\n=== Task 6: Process JSON File ===\n")
    print(process_json_file("data.json"))
    print(process_json_file("invalid.json"))
    print(process_json_file("missing_number.json"))
    print(process_json_file("nonexistent.json"))

if __name__ == "__main__":
    main()