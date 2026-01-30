class BankAccount:
    def __init__(self, balance,):
        self.balance = balance  
    
    def __add__(self, other):
        if not isinstance(other, BankAccount):
            return NotImplemented
        return BankAccount(self.balance + other.balance)
    
    def __sub__(self, other):
        if not isinstance(other, BankAccount):
            return NotImplemented
        return BankAccount(self.balance - other.balance)
    
    def __str__(self):
        return f"BankAccount Balance: {self.balance:,.2f}"
    