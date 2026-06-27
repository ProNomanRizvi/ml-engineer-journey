# Learn Constructor 

class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.email = name.lower() + "@email.com"
        self.salary = salary

    def bounus(self):
        bounus = self.salary * 0.1
        total_salary = self.salary + bounus
        return total_salary

def main():

    print("Get Information")

    name = input("Enter Your Name: ").strip().title()
    salary = float(input("Enter Your Salary: "))


    emp1 = Employee(name, salary)
    print(emp1.name)
    print(emp1.email)
    print(emp1.salary)
    print(emp1.bounus())

if __name__ == "__main__":
    main()