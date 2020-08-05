creditcard = list(map(int, input("\n\t\t Enter Your 16 digit Credit Card Number:  ")))
finalnumber = creditcard.pop(15)
creditcard = list(reversed(creditcard))

for i in range(1, len(creditcard), 2):
    creditcard[i] = creditcard[i] * 2