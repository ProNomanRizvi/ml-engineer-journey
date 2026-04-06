"""
Topic: Decorators
Phase: 1 — Python Complete Mastery
Week: 1
Description: Practice creating and using decorators to modify function behavior
"""

import functools
import time

def decorator_basic(func):
    def wrapper():
        # do something before
        print("Before the function call")
        func()
        # do something after
        print("After the function call")
    return wrapper

def greet_basic():
    print("Hello")

def shout_uppercase(func):          # 1. takes a function
    def wrapper():
        result = func()   # 3. calls the original
        return result.upper() if result else None
    return wrapper        # 2. returns a new function

@shout_uppercase
def greet_shout():
    return "hello"

def decorator_with_kwargs(func):
    def wrapper(*args, **kwargs):
        print("Before")
        result = func(*args, **kwargs)
        print("After")
        return result
    return wrapper

@decorator_with_kwargs
def add_basic(a, b):
    return a + b

@decorator_with_kwargs
def greet_with_docstring():
    """Says hello"""
    pass

def decorator_with_wraps(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper


def repeat(n):              # outer — takes decorator argument
    def decorator(func):    # middle — takes the function
        @functools.wraps(func)
        def wrapper(*args, **kwargs):  # inner — runs each call
            for _ in range(n):
                func(*args, **kwargs)
        return wrapper
    return decorator


def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__}")
        result = func(*args, **kwargs)
        print(f"Done {func.__name__}")
        return result
    return wrapper

@log
def add_logged(a, b):
    return a + b



def timer(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} took {end - start:.4f}s")
        return result
    return wrapper

@timer
def slow_function():
    time.sleep(1)

def shout_decorator(func):
    @functools.wraps(func)
    def wrapper():
        result = func()
        return result.upper() if result else None
    return wrapper

@shout_decorator
def greet_task01():
    return "hello"

def log_call(func):
    @functools.wraps(func)
    def wrapper(*args, **kargs):
        print(f"Calling {func.__name__}")
        result = func(*args, **kargs)
        print(f"Done {func.__name__}")
        return result
    return wrapper

@log_call
def greet_task02():
    return "Hello, World"

def validate_positive(func):
    @functools.wraps(func)
    def wrapper(*args):
        for arg in args:
            if arg <= 0:
                raise ValueError(f"Argument {arg} must be positive")
        result = func(*args)
        return result
    return wrapper

@validate_positive
def add_validated(a, b):
    return a + b
def cache(func):
    store = {}
    @functools.wraps(func)
    def wrapper(*args):
        if args in store:
            print("cached")
            return store[args]
        result = func(*args)
        store[args] = result
        return result
    return wrapper

@cache
def data(n):
    print("Computing...")
    return [i for i in range(n)]

def repeat_decorator(n):              
    def decorator(func):   
        @functools.wraps(func)
        def wrapper(*args, **kwargs): 
            for _ in range(n):
                func(*args, **kwargs)
        return wrapper
    return decorator

@repeat_decorator(2)
def say_hi_task05():
    print("Hi")

def retry(n):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            last_exception = None
            for _ in range(n):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    last_exception = e
            raise last_exception
        return wrapper
    return decorator


def make_test():
    counter = 0
    @retry(3)
    def test_func():
        nonlocal counter
        counter += 1
        if counter < 3:
            raise ValueError("Failed")
        return "Success"
    return test_func


def main():
    """Execute all decorator examples and tasks"""
    # ======== BASIC EXAMPLES ========
    print("\n======== BASIC EXAMPLES ========")
    
    # Example 1: Basic decorator
    decorated_greet = decorator_basic(greet_basic)
    decorated_greet()
    
    # Example 2: Using @decorator syntax
    @decorator_basic
    def greet_alt():
        print("Hello")
    greet_alt()
    
    # Example 3: Shout decorator
    print(greet_shout())  # HELLO
    
    # Example 4: Decorator with args/kwargs
    print(add_basic(3, 5))  # Before\n8\nAfter
    
    # Example 5: Checking __name__ with and without @functools.wraps
    print(f"greet_with_docstring.__name__ = {greet_with_docstring.__name__}")
    
    # Example 6: Repeat decorator
    say_hi_task05()
    
    # Example 7: Log decorator
    print(add_logged(3, 4))  # Calling add_logged\nDone add_logged\n7
    
    # Example 8: Timer decorator
    slow_function()
    
    # ======== TASKS SECTION ========
    print("\n======== TASKS SECTION ========")
    
    # Task 01: Shout decorator
    print("\n--- Task 01 ---")
    print(greet_task01())
    
    # Task 02: Log call decorator
    print("\n--- Task 02 ---")
    print(greet_task02())
    
    # Task 03: Validate positive decorator
    print("\n--- Task 03 ---")
    print(add_validated(2, 4))
    
    # Task 04: Cache decorator
    print("\n--- Task 04 ---")
    print(data(5))
    print(data(5))  # Should print "cached"
    
    # Task 05: Repeat decorator
    print("\n--- Task 05 ---")
    say_hi_task05()
    
    # Task 06: Retry decorator
    print("\n--- Task 06 ---")
    test_func = make_test()
    print(test_func())


if __name__ == "__main__":
    main()