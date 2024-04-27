#instance method

class BankAccount:
    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance
        
    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited GBP{amount}. New balance: GBP{self.balance}")
        
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew GBP{amount}. New balance: GBP{self.balance}")
            
        else:
            print ("Insufficient funds")
            
            
#create an instance

account = BankAccount(name ="Amare")
balance = 1000
account.deposit(200)
account.withdraw(50)