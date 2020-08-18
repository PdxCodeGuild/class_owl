

transactions = ()

class Balance_properties:
    def __init__(self):
        self.balance = 0
        
    
    def check_balance(balance, self):
        print(f'Your current balance is: ${balance}. ')


    def deposit(amount, balance, self):
        balance = balance + amount
        return balance
        
        

    def check_withdrawal(amount, balance, self):
        if balance >= amount:
            return True  
        else:
            return False  
            # else:
            #     return ''

    def withdraw(amount, balance, self, transactions): 
        balance = balance - amount      
        return balance, transactions.append(f'User withrew ${amount}. New balance is, ${balance}. ')
           
                    
            
    def menu(self):

        print("Welcome to the ATM")
        while True:
            menu_display = """
            1) Check your Balance
            2) Make a Deposit
            3) Make a withdrawal
            4) View Transactions
            5) Exit
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
            balance = deposit(balance, amount)
            print(f'This is your new balance: ${balance}')
        elif choice == 3:
            amount = int(input('How much would you like to withdraw today?'))
            if check_withdrawal == True:
                balance = withdraw(amount, balance, transactions)
            else:
                print(f'Transaction would overdraw your account by ({balance} - {amount})')  
        elif choice == 4:
            print(f'here is your transaction history \n {transactions}')
        elif choice == 5:
            Break



        


main()

