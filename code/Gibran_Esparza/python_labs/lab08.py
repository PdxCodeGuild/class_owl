#Get amount from user

amount = float(input("Enter the amount: "))

#convert amount to the total number of pennies

pennies = amount * 100
#Calculate quarters
quarters = pennies//25
pennies -= quarters * 25
#Calculate Dimes
dimes = pennies // 10 
pennies -= dimes *10
#Calculate Nickels
nickels = pennies //5
pennies -= nickels *5

print(f'Quarters: {quarters}, Dimes:{dimes}, Nickels{nickels},Pennies{pennies}')