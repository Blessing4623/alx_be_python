class BankAccount:
    def __init__(self, account_balance, initial_balance):
        self.account_balance = account_balance
        self.initial_balance = initial_balance
    def deposit(self, amount):
        self.amount = int(input("Enter the amount you want to deposit: "))
        self.account_balance = self.account_balance + self.amount
    def withdraw(self, amount):
        self.amount = int(input("Enter the amount you want to withdraw: "))
        if self.amount <= self.account_balance:
            return True
            self.account_balance = self.account_balance - self.amount
        else:
            return False
    def display_balance(self):
        print(f"Your current account balance is {self.account_balance}")
