class ATM:
    def __init__(self, balance = 0):
        self.balance = balance
        self.transactions = []


    def check_balance(self):
        #print(self.balance)
        self.transactions.append(f"You checked your balance and it was:  {self.balance}")
        return self.balance

    def deposit(self, amount):
        self.balance += amount
        self.transactions.append(f"You deposited:  ${amount}")
        return self.balance
        
        
        
    def check_withdrawal(self, amount):
        if self.balance > amount:
            print("You have enough dolla dolla bills")
            return amount
        

    def withdrawal_amount(self, amount):
        if self.check_withdrawal(amount):
            self.balance -= amount
            self.transactions.append(f"You withdrew  ${amount}")
        else:
            print("You have insufficient funds")

    def transaction_history(self):
        result = self.check_balance()
        print(self.transactions)
    

def main():
    The_Atm = ATM()    
    while True:
        choice = input("\n\n\t\tWhat would you like to do?\n\n\t\t Deposit, Withdrawal, Check Balance, or History?\n\n\t\t=  ").lower()
        print(choice)
        if choice == "deposit":
            amount = int(input("How much would you like to deposit?"))
            The_Atm.deposit(amount)
        elif choice == "withdrawal":
            amount = int(input("How much do you wish to withdrawal"))
            The_Atm.withdrawal_amount(amount)
        elif choice == "check balance":
            print(The_Atm.balance)          
        elif choice == "history":
            The_Atm.transaction_history()
        


main()