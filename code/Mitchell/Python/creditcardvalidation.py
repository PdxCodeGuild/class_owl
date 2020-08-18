import math
#creditcard = (input("\n\t\t Enter Your Credit Card Number:  "))

creditcard = list(map(int, input("\n\n\t\t Enter Your 16 digit Credit Card Number:  ")))
finalnumber = creditcard.pop(15)
creditcard = list(reversed(creditcard))

for i in range(1, len(creditcard), 2):
    creditcard[i] = creditcard[i] * 2

for i in range(0, len(creditcard)):
    if creditcard[i] > 9:
        creditcard[i] = creditcard[i] - 9

creditcard = str(sum(creditcard))
finalsum = list(creditcard)
finalsum = finalsum.pop(1)

if finalnumber == finalsum:
        print("Credit Card Validated")
else: print("Credit Card Not Validated")
