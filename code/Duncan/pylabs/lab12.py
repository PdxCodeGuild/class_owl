# lab 12 guess the number


import random
comp = random.randint(0, 10)

user = int(input("Enter a number from 1 - 10 "))
count = 0

while True:

    if user > comp:
        print(f"{user}")
        user = int(input("too high try again: "))
        count += 1
    elif user < comp:
        print(f"{user}")
        user = int(input("too low try again: "))
        count += 1
    elif user == comp:
        print("You guessed my number grats!!")
        count += 1
        print(f"You guessed {count} times")
        break       
        
      
            