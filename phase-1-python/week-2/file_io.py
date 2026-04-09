# Topic: File I/O
# Phase: 1 — Python Complete Mastery
# Week: 2
# Description: Understanding file operations, reading and writing files, context managers, and best practices for handling files in Python

import csv
import json
import os

PATH = os.path.join(os.path.dirname(__file__), "data")


def write_file(filepath, lines):
    with open(filepath, "w", encoding="utf-8") as f:
        f.writelines(line + "\n" for line in lines)


def read_file(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        return [line.strip() for line in f]


def append_to_file(filepath, line):
    with open(filepath, "a", encoding="utf-8") as f:
        f.write(line + "\n")


def write_csv(filepath, data):
    with open(filepath, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=data[0].keys())
        writer.writeheader()
        writer.writerows(data)


def read_csv(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        return list(reader)


def update_csv(filepath, name, new_grade):
    students = read_csv(filepath)
    for student in students:
        if student["name"] == name:
            student["grade"] = new_grade
            break
    write_csv(filepath, students)


def write_json(filepath, data):
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)


def read_json(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        return json.load(f)


def update_json(filepath, key, value):
    data = read_json(filepath)
    data[key] = value
    write_json(filepath, data)


def merge_csv(file1, file2, output_file):
    with open(file1, "r", encoding="utf-8") as f1, open(file2, "r", encoding="utf-8") as f2, open(output_file, "w", newline="", encoding="utf-8") as out:
        reader1 = csv.DictReader(f1)
        reader2 = csv.DictReader(f2)
        fieldnames = reader1.fieldnames  # assuming both files have the same structure
        writer = csv.DictWriter(out, fieldnames=fieldnames)
        writer.writeheader()
        seen = set()
        for row in reader1:
            writer.writerow(row)
            seen.add(row["name"])
        for row in reader2:
            if row["name"] not in seen:
                writer.writerow(row)
                seen.add(row["name"])


def main():
    
    # Reading methods
    with open(f"{PATH}/data.txt", "r", encoding="utf-8") as f:
        content = f.read()        # entire file as one string
        lines = f.readlines()     # list of lines including \n
        line = f.readline()       # one line at a time

    with open(f"{PATH}/data.txt", "r", encoding="utf-8") as f:
        for line in f:            # one line at a time, no list built
            print(line.strip())

    # Writing methods
    with open(f"{PATH}/output.txt", "w", encoding="utf-8") as f:
        f.write("Hello\n")        # write a string
        f.writelines([
            "Sample Data\n",
            "Another Line\n"
        ])  # write multiple strings

    # Writing CSV
    with open(f"{PATH}/data.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["name", "age"])
        writer.writeheader()
        writer.writerow({"name": "Ali", "age": 25})

    # Reading CSV
    with open(f"{PATH}/data.csv", "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            print(row)  # {'name': 'Ali', 'age': '25'}

    # Json file handling
    # Writing JSON
    data = {"model": "linear_regression", "accuracy": 0.95}
    with open(f"{PATH}/config.json", "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)

    # Reading JSON
    with open(f"{PATH}/config.json", "r", encoding="utf-8") as f:
        config = json.load(f)
        print(config["accuracy"])  # 0.95

    print("======== End of File I/O Examples =======\n\n")
    print("\n======== TASKS =======\n")

    print("--- Task 01 ---")

    FilePath = f"{PATH}/task_output.txt"
    Lines = ["Line 1", "Line 2", "Line 3"]
    write_file(FilePath, Lines)
    read_lines = read_file(FilePath)
    print(read_lines)  # ['Line 1', 'Line 2', 'Line 3']

    append_to_file(FilePath, "Line 4")
    print(read_file(FilePath))  # ['Line 1', 'Line 2', 'Line 3', 'Line 4']

    print("\n--- Task 02 ---")

    students = [
        {"name": "Ali", "grade": 88, "city": "Lahore"},
        {"name": "Sara", "grade": 95, "city": "Karachi"},
        {"name": "Umar", "grade": 73, "city": "Islamabad"},
    ]
    csv_path = f"{PATH}/students.csv"
    write_csv(csv_path, students)
    students_data = read_csv(csv_path)
    for student in students_data:
        print(student)  # {'name': 'Ali', 'grade': '88', 'city': 'Lahore'} ...

    print("\n--- Task 03 ---")
    print("Update CSV file to add a new student record")

    update_csv(csv_path, "Ali", 90)
    students_data = read_csv(csv_path)
    for student in students_data:
        print(student)  # {'name': 'Ali', 'grade': '90', 'city': 'Lahore'} ... {'name': 'Ayesha', 'grade': '91', 'city': 'Multan'}

    print("\n--- Task 04 ---")
    print("Work with JSON files - Write and Read a JSON file")

    config_data = {
        "model": "random_forest",
        "parameters": {
            "n_estimators": 100,
            "max_depth": 10
        },
        "accuracy": 0.92
    }
    json_path = f"{PATH}/model_config.json"
    write_json(json_path, config_data)
    loaded_config = read_json(json_path)
    print(loaded_config)

    update_json(json_path, "accuracy", 0.93)
    updated_config = read_json(json_path)
    print(updated_config)  # accuracy should be updated to 0.93

    file1 = f"{PATH}/students.csv"
    file2 = f"{PATH}/additional_students.csv"
    output_file = f"{PATH}/merged_students.csv"
    merge_csv(file1, file2, output_file)
    merged_students = read_csv(output_file)
    for student in merged_students:
        print(student)  # prints all students from both files


if __name__ == "__main__":
    main()