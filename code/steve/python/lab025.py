

#transactions = ()

class Balance_properties:
    def __init__(self):
        self.balance = 0
        self.tranactions = ()

    def check_balance(balance, self):
        print(f'Your current balance is: ${balance}. ')


    def deposit(amount, balance, self):
        balance = balance + amount
        return balance
        
        

    def check_withdrawal(amount, balance, self):
        if balance >= amount:
            return True    
            # else:
            #     return ''

    def withdraw(amount, balance, self, transactions): 
        if check_withdrawal() == True:
            balance = balance - amount      
            return balance, transactions.append(f'User withrew ${amount}. New balance is, ${balance}. ')
        else:
            print(f'Transaction would overdraw your account by ({balance} - {amount})')     
                    
            
    def menu():

        print("Welcome to the ATM")
        while True:
            menu_display = """
            1) Check your Balance
            2) Make a Deposit
            3) Make a withdrawal
            4) view Transactions
            """
            choice = input(menu_display)
        return choice



def main():
    while True:
        choice = menu()
        if choice == 1:
            check_balance(balance)
        elif choice == 2:
            amount = int(input('How much would you like to deposit today?'))
            deposit(balance, amount)

        


main()

