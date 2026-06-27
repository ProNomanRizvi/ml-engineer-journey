# ENCAPSULATION

class Account:
    def __init__(self, balance):
        self.balance = balance      # public - anyone can touch this
        self._balance = balance     # "protected" - convention only, just a hint
        self.__balance = balance    # "private" - name mangling kicks in


# @Property
class Account:
    def __init__(self, balance):
        self._balance = balance

    @property
    def balance(self):
        return self._balance
    
    @balance.setter
    def balance(self, value):
        if value < 0:
            raise ValueError("Balance Cannot be 0")
        
        self._balance = value

    