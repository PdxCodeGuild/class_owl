#credit card validation

# get number
cc_num = []
check_digit = []
summed = []

cc_num = input("Enter your card number: ")
cc_num = [int(i) for i in cc_num]




print(cc_num)

check_digit = cc_num.pop()
print(cc_num)
cc_num.reverse()
print(cc_num)
cc_num = [i + i for i in cc_num]
print(cc_num)
for i in range(0,len(cc_num)):
    if cc_num[i] > 9:
        cc_num[i] = cc_num[i] - 9  
print(cc_num)
cc_num = sum(cc_num)
cc_num = str(cc_num)


print(cc_num)
summed = [int(i) for i in cc_num]
print(summed)
print(check_digit)
if check_digit == summed[1]:
    print("your card is valid")
else:
    print("Invalid card number")    




