#Creating ATM Class
class ATM:
    def __init__(self):
        #Started balance at 0
        self.balance = 0
        #Empty List to add Transactions
        self.transactions = []

#Check Balance Class Method
    def check_balance(self):
       b
        self.transactions.append(f"You checked balance: balance is: ${self.balance}")
        return self.balance
#Deposti Class Method
    def deposit(self,amount):
         #adding to transactions list
        self.transactions.append(f"You deposited ${amount}")
         #Adding deposit amount to balance
        self.balance += amount
#Check Withdrawal Class MEthod
    def check_withdrawal(self,amount):
        return self.balance > amount
#Withdraw Class Method       
    def withdraw(self,amount):
        if self.check_withdrawal(amount):
             #adding to transactions list
            self.transactions.append(f"You withdrew S{amount}")
            #Subtracting withdraw amount from balance
            self.balance -= amount
            return amount
        else:
            return "Not in enough money in account"
#Print List Method            
    def print_transactions(self):
        #Printing each transaction in transactions
        for x in self.transactions:
            print(x)
def main():
    atm = ATM()
    choices = ['deposit','withdraw','checkbalance','history','done']

    while True:
        while True:
            option = input(f"Enter your choice from {choices}").lower().strip()
            if option in choices:
                break
            elif option not in choices:
                print ("Invalid Entry try again")
        if option == "done":
            print ("Thank you come again")
            break
        elif option == "deposit":
            amount = int(input("Enter the amount to deposit: "))
            atm.deposit(amount)
        elif option == "checkbalance":
            print(f"Your balance is ${atm.balance}")
        elif option == "history":
            atm.print_transactions()
        elif option == "withdraw":
            amount = int(input("How much would you like to withdraw?: "))
            print(f"You are withdrawing: {atm.withdraw(amount)}")

main()
