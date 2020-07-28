
# Get amount from user
amount = input("Enter the amount: ")

while True:
    try:
        amount = float(amount)
    except ValueError:
        amount = input("Enter a valid dollar amount: ")
    else:
        break


# Convert amount to total number of pennies
# pennies = amount * 100

# # Calculate quarters
# quarters = pennies // 25
# pennies -= quarters * 25

# # Calculate dimes
# dimes = pennies // 10
# pennies -= dimes * 10

# # Calculate nickels
# nickels = pennies // 5
# pennies -= nickels * 5

# Calculate quarters
quarters = amount // .25
amount -= quarters * .25

# Calculate dimes
dimes = amount // .10
amount -= dimes * .10

# Calculate nickels
nickels = amount // .05
amount -= nickels * .05

pennies = amount // .01
amount -= pennies * .01


# Display coins to user
print(f"Quarters: {quarters} Dimes: {dimes} Nickels: {nickels} Pennies: {pennies} Remaining: {amount}")