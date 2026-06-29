
class AccountFactory:

    @staticmethod
    def create_account(acc_type, owner, balance=0.0):
        if acc_type == 'current':
            return CurrentAccount(owner, balance)
        elif acc_type == 'savings':
            return SavingsAccount(owner, balance)
        else:
            raise ValueError(f'This Accont "{acc_type}" is Unknown.')

class SavingsAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

class CurrentAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

# --------
# Valid accounts
curr_acc = AccountFactory.create_account("current", "Noman Rizvi", 50000.00)
print(type(curr_acc))  # <class '__main__.CurrentAccount'> expect karo

svg_acc = AccountFactory.create_account("savings", "Noman Zahid", 45000.00)
print(type(svg_acc))   # <class '__main__.SavingsAccount'> expect karo

# Invalid type
try:
    unk_acc = AccountFactory.create_account("Account", "Noman", 45000)
except ValueError as e:
    print(f"Caught expected error: {e}")