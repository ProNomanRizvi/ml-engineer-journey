# MRO(Method Resolution Order)

class A:
    def greet(self):
        return "Hello from A"

class B(A):
    def greet(self):
        return "Hello from B"

class C(A):
    def greet(self):
        return "Hello from C"

class D(B, C):
    pass

# ====================

class A:
    def greet(self):
        return "A"

class B(A):
    def greet(self):
        return "B->" + super().greet()

class C(A):
    def greet(self):
        return "C->" + super().greet()

class D(B, C):
    def greet(self):
        return "D->" + super().greet()

print(D().greet())
# D->B->C->A