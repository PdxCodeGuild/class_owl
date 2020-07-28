x = input("Would you like to avg some numbers?: ")

if x == "yes":
    print("righteous")
elif x == "no":
    print("You shall not pass!")
nums = []
num = int(input("what is your number?: "))
nums.append(num)

while num != "done":
    num = input("add another number?: ")
    if num == "done":
        break
    num = int(num)
    nums.append(num)
    print(nums)

for num in nums:
        num = sum(nums)
        num = num / len(nums)
print(num)



