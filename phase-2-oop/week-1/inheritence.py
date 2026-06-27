# INHERITENCE
# Types of Inheritence

# 01- Single Heritence
class Animal:

    @staticmethod
    def hello():
        print("Welocom in Animal Class")

class Dog(Animal):
    @staticmethod
    def voice():
        print("Dogs Barks...")

animal1 = Dog()
animal1.hello()
animal1.voice()



# 02- Multi-level Heritence
class ComputerScience:
    
    @staticmethod
    def info():
        print("Duration: 4 Years")

class SoftwareEngineering(ComputerScience):

    @staticmethod
    def info():
        ComputerScience.info()
        print("Department : ComputerScience")

class SoftwareDevelopment(SoftwareEngineering):

    @staticmethod
    def info():
        print("Degree Name: SoftwareEngineering")
        SoftwareEngineering.info()
        print("Software Development Started...")


s1 = SoftwareDevelopment()

s1.info()


# 03- Multiple Heritence
class Father:
    father_name = "Ali"

class Mother:
    mother_name = "Fatima"

class Son(Father, Mother):
    name = "Hassan"
    

son = Son()
print(son.name)
print(son.father_name)
print(son.mother_name)