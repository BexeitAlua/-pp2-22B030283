class Bank_Account:
    def __init__(self):
        self.balance=0
 
    def deposit(self):
        amount=float(input())
        self.balance += amount
        print(amount)
 
    def withdraw(self):
        amount = float(input())
        if self.balance>=amount:
            self.balance-=amount
            print(amount)
        else:
            print("\n Insufficient balance  ")
 
    def display(self):
        print(self.balance)
 

s = Bank_Account()
  

s.deposit()
s.withdraw()
s.display()
    