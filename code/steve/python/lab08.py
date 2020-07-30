
print("let/'s make change!")
enter_dollar_amt = float(input('Please enter the amount to make change: (x.xx)'))
whole_number = enter_dollar_amt * 100

quarters = 25
dimes = 10
nickles = 5
pennies = 1
quarters_output = whole_number // quarters
quarters_remainder = whole_number % quarters
dimes_output = quarters_remainder // dimes
dimes_remainder = quarters_remainder % dimes
nickels_output = dimes_remainder // nickles
nickels_remainder = dimes_remainder % nickles
if nickels_remainder = 0:
    pennies_output = dimes_remainder
else:
pennies_output = nickels_remainder


if quarters_output > 0:
    print(f'{int(quarters_output)} Quarters')
if dimes_output > 0:
    print(f'{int(dimes_output)} Dimes')
if nickels_output > 0:
    print(f'{int(nickels_output)} Nickles')
if pennies_output > 0:
    print(f'{int(pennies_output)} Pennies')






# def start():
#     print("let/'s make change!")
#     enter_dollar_amt = float(input('Please enter the amount in pennies to make change: (x.xx)'))
#     whole_number = enter_dollar_amt * 100
#     return whole_number

# def calc_pennies(whole_number):
#     pennies = whole_number * 1
#     pennies = int(pennies)
#     return pennies




# def main():

#     whole_number = start()
#     answer = "Your change in pennies is: " + str(calc_pennies(whole_number))
    
#     print(answer)

# main()