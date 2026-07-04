# Basic Syntax
# assert condition, "error message if condition is False."

# Simple Examples
assert 2 + 2 == 4          # Pass
assert 2 + 2 == 5           # Raise -> AssertionError

x = 10
assert x > 0, "x must be positive."   # Pass
assert x < 0, "x must be negative."   # Fail -> "AssertionError: x must be negative"



# Assert-Based Testing

def add(a, b):
    return a + b

# Assert-based tests
assert add(2, 3) == 5
assert add(-1, 1) == 0
assert add(0, 0) == 0
assert add(-5, -5) == -10

print("All tests passed! ✅")


# Exmaple with Class
class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError("Insufficient funds")
        self.balance -= amount
        return self.balance

# Assert-based tests for BankAccount
acc = BankAccount(100)

assert acc.balance == 100, "Initial balance galat hai"

acc.deposit(50)
assert acc.balance == 150, "Deposit ke baad balance galat hai"

acc.withdraw(30)
assert acc.balance == 120, "Withdraw ke baad balance galat hai"

# Test edge case
try:
    acc.withdraw(1000)
    assert False, "Insufficient funds pe error aana chahiye tha"
except ValueError:
    assert True   # yeh expected hai

print("Sab BankAccount tests pass! ✅")