def make_dat_change():
    """
    Convert a dollar amount into change. e.g 1.25 to 5 quarters"""


    # Print welcome message
    print('''Hello! I am COMPUTRON!
Please allow me to convert your money!
    ''')

    # request a value and strip periods and dollar signs
    penny_amt = input('Please input the amount you wish to convert to quarters, dimes, nickles and pennies ($1.36 or 1.36): ')
    penny_amt = penny_amt.replace('$',"")
    penny_amt = penny_amt.replace('.',"")

    # verify it can be converted to an int
    while not penny_amt.isdigit():
        print('ERROR! Please insert the amount only.\n')
        penny_amt = input('Please input the amount you wish to convert to quarters, dimes, nickles and pennies: ')
        penny_amt = penny_amt.replace('$',"")
        penny_amt = penny_amt.replace('.',"")

    # Convert it to an int

    penny_amt = int(penny_amt)

    print('Processing...\n')

    # Declare resultant variables

    qt,dime,nickles,pennies = 0,0,0,0
     
    
    # Loop and convert to different coins

    while penny_amt != 0:
        if penny_amt >= 25:
            penny_amt -= 25
            qt += 1
        elif penny_amt >= 10:
            penny_amt -= 10
            dime += 1
        elif penny_amt >= 5:
            penny_amt -= 5
            nickles += 1
        else:
            pennies = penny_amt
            penny_amt = 0
    
    # Output results
    print(f'It looks like you have {qt} quarter(s), {dime} dime(s), {nickles} nickle(s) and {pennies} pennies\n')
    

if __name__ == "__main__":
    make_dat_change()
      
