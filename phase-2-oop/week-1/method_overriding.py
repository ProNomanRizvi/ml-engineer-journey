# METHOD OVERRIDING

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def salary(self):
        return 0.0
    
    def info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Salary: {self.salary()}")

class Doctor(Person):

    def salary(self):
        return 40000.00

class Engineer(Person):
    def salary(self):
        return 80000.00
    
d = Doctor("Ali", 45)
e = Engineer("Noman", 21)

e.info()
print("=======")
d.info()