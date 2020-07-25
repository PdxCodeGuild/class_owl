#making change lab


dollar = input("Enter a dollar amount in pennies ie..$1.25 would be 125:")
dollar =int(dollar)
quarters = dollar // 25
dimes = dollar // 10
nickles = dollar // 5
pennies = dollar // 1
print(f"you would have {quarters} quarters, {dimes} Dimes, {nickles} Nickles")
