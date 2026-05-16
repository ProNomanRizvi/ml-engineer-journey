# Topic: Modules & the Import System
# Phase: 1 — Python Complete Mastery
# Week: 2
# Description: This module contains practice tasks for working with Python modules and the import system. Each task demonstrates different ways to import and use modules in Python.

# ── Imports at Module Level ───
import os
import sys
import math
import math as m
import random
import random as rnd
from math import sqrt, pi
from os import getcwd
from mypackage import add, multiply
from string_utils import reverse_string, capitalize_words


# ── Task 1: Multiple Imports ───
def task_01():
    print("Current Directory:", os.getcwd())
    print("Python Version:", sys.version)
    print("Value of Pi:", math.pi)
    print("Random Integer (1-10):", random.randint(1, 10))


# ── Task 2: Aliased Imports ───
def task_02():
    print("Value of Pi (using alias m):", m.pi)
    print("Random Integer (1-10):", rnd.randint(1, 10))


# ── Task 3: Direct Imports ───
def task_03():
    print("Square Root of 16:", sqrt(16))
    print("Value of Pi (imported directly):", pi)
    print("Current Directory (imported directly):", getcwd())


# ── Task 4: Inspecting Module Attributes ───
def task_04():
    print(dir(math))
    print("Math Module Name:", math.__name__)
    print("Math Module File:", getattr(math, '__file__', 'Built-in module (no file)'))


# ── Task 5: Custom Package (mypackage) ───
def task_05():
    result_add = add(10, 5)
    result_multiply = multiply(10, 5)
    
    print("Using mypackage.add():", result_add)
    print("Using mypackage.multiply():", result_multiply)


# ── Task 6: Custom Module (string_utils) ───
def task_06():
    sample_string = "hello world"
    print("Original String:", sample_string)
    print("Reversed String:", reverse_string(sample_string))
    print("Capitalized Words:", capitalize_words(sample_string))


def main():
    print("=== Task 1: Standard Library Imports ===")
    task_01()
    print("\n=== Task 2: Aliased Imports ===")
    task_02()
    print("\n=== Task 3: Direct Imports ===")
    task_03()
    print("\n=== Task 4: Inspecting Module Attributes ===")
    task_04()
    print("\n=== Task 5: Custom Package (mypackage) ===")
    task_05()
    print("\n=== Task 6: Custom Module (string_utils) ===")
    task_06()


if __name__ == "__main__":
    main()