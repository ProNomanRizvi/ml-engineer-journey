# SUPER() METHOD

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print("Show() Called")

class Doctor(Person):
    def __init__(self,name, age, pay):
        super().__init__(name, age)
        super().show()
        self.pay = pay


doc = Doctor("Ali", 45, 50000.00)
print(doc.name)
print(doc.age)
print(doc.pay)