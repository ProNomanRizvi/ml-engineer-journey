# CLASS and STATIC METHODS

# Static Methods
class Math:

    def __init__(self, num):
        self.num = num

    def sqrt(self):
        print(f"Square of {self.num} = {self.num*self.num}")

    @staticmethod
    def multiply(num1, num2):
        print(f"Multiplication of {num1}*{num2} = {num1*num2}")
    
a = Math(5)
a.sqrt()
a.multiply(5, 6)

# Class Methods

class Team:
    team_name = "Pakistan Hockey"
    total_palyers = 11
    @classmethod
    def change_team_name(self, new_team):
        self.team_name = new_team

    def team_info(self):
        print("Total Out Players = 2")
        print(f"Team Name is {self.team_name}")


t1 = Team()
t1.team_info()
t1.change_team_name("Pakistan Football")
t1.team_info()
print(Team.team_name)
