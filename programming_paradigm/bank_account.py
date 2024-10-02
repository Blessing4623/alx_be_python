class BankAccount:
    def __init__(self, account_balance: float, initial_balance = 0):
        self.account_balance = account_balance
        self.initial_balance = initial_balance
    def deposit(self, amount):
        self.account_balance = self.account_balance + amount
    def withdraw(self, amount):
        
        if amount <= self.account_balance:
            return True
            self.account_balance = self.account_balance - amount
        else:
            return False
    def display_balance(self):
        print(f"Current Balance: ${self.account_balance:.2f}")