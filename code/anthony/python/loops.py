import time



count = 0
while count < 5:
    time.sleep(1)
    print(f"{count} Hello Class")
    if count == 3:
        break
    count += 1

else:
    print("We finished the loop")

print('done')
print(count)



fruits = ['apples', 'bananas', 'pears', 'cherries', 'pineapple']

for fruit in fruits:
    print(fruit)

fruit = fruits[0]
print(fruit)
fruit = fruits[1]
print(fruit)


nums = []
while True:
    num = input('enter number: ')
    if num == 'done':
        break
    nums.append(int(num))
print(nums)