# Polymorphism

class Account:

    def __init__(self, balance):
        self.balance = balance
        
    def calculate_interest(self):
        return 0  # base, does nothing meaningful

class SavingsAccount(Account):
    def calculate_interest(self):
        return self.balance * 0.05

class CheckingAccount(Account):
    def calculate_interest(self):
        return self.balance * 0.001
    
accounts = [SavingsAccount(balance=1000), CheckingAccount(balance=1000)]

for acc in accounts:
    print(acc.calculate_interest())

# PRACTICE

class Shape:

    def calculate_area(self):
        return 0.0
    
class Rectangle(Shape):

    def __init__(self, height, width):
        self.height = height
        self.width = width

    def calculate_area(self):
        return self.height * self.width
    
class Circle(Shape):
    PI = 3.14
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return Circle.PI * (self.radius**2)
    
areas = [Rectangle(10, 10), Circle(10)]

for area in areas:
    print(area.calculate_area())