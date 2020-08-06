#Convert the input string into a list of ints
#Slice off the last digit. That is the check digit.
#Reverse the digits.
#Double every other element in the reversed list.
#Subtract nine from numbers over nine.
#Sum all values.
#Take the second digit of that sum.
#If that matches the check digit, the whole card number is valid.
carD = input("Whats the digits?: ")
carD = [int(i) for i in carD]
v = carD.pop(-1)
carD = list(reversed(carD))

for x in range(0, len(carD), 2):
    carD[x] = carD[x] * 2
    if carD[x] > 9:
        carD[x] = carD[x] - 9
numD = sum(carD)
numD = str(numD)
numD = list(numD)

s = numD.pop(-1)

if s == v:
    print("these match")
elif s != v:
    print('nope')

print(s)
print(v)






