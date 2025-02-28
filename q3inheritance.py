class BankAccount:
    def __init__(self,account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance
    def deposit(self,amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount}. New balance:{self.balance}")
        else:
         print("Deposit amount must be positive.")
    def display_balance(self):
        print(f"Account holder:{self.account_holder}, Balance:{self.balance}")

class SavingsAccount(BankAccount):
    def add_interest(self, rate):
        if rate > 0:
            interest = self.balance * (rate / 100)
            self.balance += interest
            print(f"Interest added:{interest}. New balance:{self.balance}")
        else:
         print("Interest amount must be positive.")

