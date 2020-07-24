def make_dat_change():
    """ Convert pennies into a dollar amount
    """
    # Print a welcome screen
    print('''Hello! I am COMPUTRON!
Please allow me to convert your pennies into a dollar amount!
    ''')
    # Request amount of pennies
    penny_amt = input('Please input the amount of pennies you wish to convert: ')

    # Verify it is a number
    while not penny_amt.isdigit():
        print('ERROR! Please insert the number of pennies only.\n')
        penny_amt = input('Please input the amount of pennies you wish to convert: ')
    
    #  COnvert to int
    penny_amt = int(penny_amt)

    print('Processing...\n')
    # define resultant variables

    dol = 0 
    amt = 0
    
    # Loop and convert by subtacting 100 from the amount per cycle and adding one to the dollar amount
    while penny_amt != 0:
        if penny_amt > 100:
            penny_amt -= 100
            dol += 1
        else:
            amt = penny_amt/ 100
            penny_amt = 0

    # Print results
    print(f'Your total is: ${round((dol + amt),2)}')

    
if __name__ == "__main__":
    make_dat_change()
    