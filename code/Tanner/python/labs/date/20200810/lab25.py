import math
import time
import random


class acct:
    def check_balance(self):
        return self.balance 
    
    def deposit(self, amount):  
        self.balance += amount
        

    def check_withdrawal(self, howmuch):
        if howmuch > self.balance:
            return False
        elif howmuch <= self.balance:
            return True

    def withdraw(self, howmuch):
        input("how much should we withdraw?: ")
        if self.check_withdrawal(howmuch) is True:
            self.balance -= howmuch
#A newly created account will default to a balance of 0
    def __init__(self):
        self.balance = 0

newacct = acct()
print(newacct.balance)

newacct.deposit(500)

    
print(newacct.balance)