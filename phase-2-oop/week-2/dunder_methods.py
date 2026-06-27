# # DUNDER METHODS

# # '__repr__' AND '__str__'
# class Account:
#     def __init__(self, owner, balance):
#         self.owner = owner
#         self.balance = balance

#     def __repr__(self):
#         return f"Account(owner={self.owner!r}, balance={self.balance!r})"

#     def __str__(self):
#         return f"{self.owner}'s account — balance: {self.balance}"
    
# a = Account("Rizvi", 500)
# print(a)        # uses __str__  -> Rizvi's account — balance: 500
# print([a])      # uses __repr__ -> [Account(owner='Rizvi', balance=500)]

# __len__

class Classroom:
    def __init__(self):
        self.students = []

    def add_student(self, name):
        self.students.append(name)

    def __len__(self):
        return len(self.students)
    
c = Classroom()
c.add_student("Noman")
c.add_student("Iqbal")

print(len(c))