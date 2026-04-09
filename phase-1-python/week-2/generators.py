# Topic: Generators
# Phase: 1 — Python Complete Mastery
# Week: 2
# Description: Understanding generators, yield keyword, lazy evaluation, memory efficiency, and practical applications 

import sys


def my_gen():
    yield 1
    yield 2
    yield 3


def countdown(n):
    while n > 0:
        yield n
        n -= 1


def chain(*iterables):
    for it in iterables:
        yield from it


def even_numbers(limit):
    n = 0
    while n <= limit:
        yield n
        n += 2


def integers_from(n):
    while True:
        yield n
        n += 1


def count_up(start, end):
    """Generator that counts from start to end (inclusive)"""
    n = start
    while n <= end:
        yield n
        n += 1


def squares(num):
    """Generator that yields squares of numbers from 0 to n (inclusive)"""
    n = 1
    while n <= num:
        yield n ** 2
        n += 1


def fibonacci(limit):
    """Generator that yields Fibonacci numbers up to a given limit"""
    a, b = 0, 1
    while a <= limit:
        yield a
        a, b = b, a + b


def odd_squares(limit):
    """Generator that yields squares of odd numbers up to a given limit"""
    n = 1
    while n <= limit:
        yield n ** 2
        n += 2


def read_in_chunks(lst, chunk_size):
    """Generator that yields chunks of a list"""
    for i in range(0, len(lst), chunk_size):
        yield lst[i:i + chunk_size]


def pipeline(data, *funcs):
    """Generator that applies a series of functions to data"""
    for item in data:
        result = item
        for func in funcs:
            result = func(result)
        yield result


def main():
    g = my_gen()   # nothing runs yet
    print(next(g)) # 1 — runs until first yield, pauses
    print(next(g)) # 2 — resumes, runs until second yield
    print(next(g)) # 3 — resumes, runs until third yield
    # print(next(g)) # StopIteration — nothing left

    print("====== ======")

    for num in countdown(5):
        print(num, end=" ")
    # 5, 4, 3, 2, 1

    print("==========")

    # List comprehension — builds entire list in memory
    squares_list = [x ** 2 for x in range(1000000)]
    print(squares_list[2])

    # Generator expression — produces one value at a time
    squares_gen = (x ** 2 for x in range(1000000))
    print(next(squares_gen))

    print("=========")

    for val in chain([1, 2], [3, 4], [5]):
        print(val)  # 1 2 3 4 5

    print("===========")

    list_comp = [x ** 2 for x in range(10000)]
    gen_exp = (x ** 2 for x in range(10000))

    print(f"List Size: {sys.getsizeof(list_comp)}")  # ~87624 bytes
    print(f"Generators Size: {sys.getsizeof(gen_exp)}")    # ~112 bytes

    print("========")

    for num in even_numbers(9):
        print(num, end=" ")  # 0 2 4 6 8 10

    print("\n=====")

    gen = integers_from(1)
    print(next(gen))  # 1
    print(next(gen))  # 2
    print(next(gen))  # 3
    # runs forever — you control when to stop

    print("=======")
    total = sum(x ** 2 for x in range(1000000))
    print(f"Total Sum: {total}")  # computed without building a list

    print("\n\n====== TASKS LEVEL =======")
    print("\nTASK 01: ")

    for num in count_up(3, 7):
        print(num, end=" ")  # 3 4 5 6 7

    print("\n\nTASK 02: ")

    for sq in squares(5):
        print(sq, end=" ")  # 1 4 9 16 25

    print("\n\nTASK 03: ")

    for fib in fibonacci(20):
        print(fib, end=" ")  # 0 1 1 2 3 5 8 13

    print("\n\nTASK 04: ")
    # From 1 to 20, yield odd squares

    for sq in odd_squares(20):
        print(sq, end=" ")  # 1 9 25 49 81 121 169 225 289 361

    print("\n\nTASK 05: ")

    my_list = [1, 2, 3, 4, 5, 6, 7]
    for chunk in read_in_chunks(my_list, 3):
        print(list(chunk), end=" ")  # [[1, 2, 3], [4, 5, 6], [7]]

    print("\n\nTASK 06: ")

    p = list(pipeline([1, 2, 3, 4, 5],
        lambda x: x * 2,
        lambda x: x + 10
    ))

    print(p)  # [12, 14, 16, 18, 20]


if __name__ == "__main__":
    main()