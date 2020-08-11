
# Defines ATM class
class ATM:
    
    # Instantiates the class and creates a history list
    def __init__(self, balance = 0):
        self.balance = balance
        self.history = []
    

    # Checks balance and adds to history
    def check_balance(self):

        self.transactions('checked balance')
        pass

    # Withdraws from the balance and adds to history
    def withdraw(self, amount):
        if self.balance - amount >= 0 and amount != 0:
            self.balance -= amount
            self.transactions('withdrew', amount)
        elif amount == 0:
            self.transactions('withdrew', '0')
        else:
            print('Insufficient Funds')
            self.transactions('failed to withdraw funds due to insufficient funds.')
        



    # Deposits to the balance and adds to history
    def deposit(self, amount):
        
        self.balance += amount
        if amount == 0:
            self.transactions('deposited', '0')
        else:
            self.transactions('deposited', amount)
        

    # appends the transactions to the history list
    def transactions(self, action, value = False):
        

        if value == False:
            
            self.history.append(f'User {action}')

        else:
            self.history.append(f'User {action} ${value}')

        pass

# Main function
def atm():

    # creates the class object
    atm_object = ATM()

    print('Welcome!')
    
    while True:

        sel = input('''
Please make a selection:

1) Check Balance

2) Withdraw Funds

3) Deposit Funds

4) Transaction History

5) Exit


''')

        while not sel.isdigit():
            print('Invalid selection. Please use digits only.')

            sel = input('''
Please make a selection:

1) Check Balance
        
2) Withdraw Funds

3) Deposit Funds
        
4) Transaction History

5) Exit
        

''')


        # Determines which action the user requested and manipulates the object
        if sel == "1":
            print(f'\n\tBalance: ${atm_object.balance}')
            atm_object.check_balance()

        elif sel == '2':
            amount = input('Select amount to withdraw: ')
            while not amount.isdigit():
                print('Whole dollar amounts only!')
                amount = input('Select amount to withdraw: ')

            atm_object.withdraw(int(amount))

        elif sel == '3':

            amount = input('Select amount to deposit: ')
            while not amount.isdigit():
                print('Whole dollar amounts only!')
                amount = input('Select amount to deposit: ')

            atm_object.deposit(int(amount))

        elif sel == '4':
            
            if len(atm_object.history) == 0:
                print('No history recorded!')

            else:
                for x in atm_object.history:
                    
                    print(f'>>>{x}', end = '\n\n')

            input('Press enter to continue')

        elif sel == '5':
            print('Goodbye!')
            break





if __name__ == "__main__":
    atm()



