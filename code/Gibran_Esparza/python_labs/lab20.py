#Input String
credit_cardnum = input("Enter a creditcard number: ")
#Convert Input String into a lis of integers
list_num = list(credit_cardnum)
for x in range(0, len(credit_cardnum)):
    list_num[x] = int(list_num[x])
#Slice of the last digit
list_num =list_num[:-1]
check_digit = list_num[-1]
#reverse the digtis
rlist = list(reversed(list_num))
#double every other element of reverse list
for x in range(0,len(rlist),2):
    rlist[x] *= 2
#Subtract nine from numbers over 9
for x in range(len(rlist)):
    if rlist[x] > 9:
        rlist [x] -= 9
#Sum all values
sumnum = sum(rlist)
#Take the second digit of sum
seconddigit = int(list(str(sumnum))[1])
#If that matches check digit, the whole card number is valid
if seconddigit == check_digit:
    print ("the number is valid")

