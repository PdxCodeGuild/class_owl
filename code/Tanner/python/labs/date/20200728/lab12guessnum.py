import random

x = random.randint(1, 10)
user = int(input("Guess a number?: "))
count = 1


while user != x:
    print("nope")
    user = int(input("Guess again?: "))
    print(user)
    count += 1
    print(f'your count is {count}.')
    if user == x:
        print("guessed it!")
        break
    elif user >= x:
        print("too high")
        count += 1
    elif user <= x:
        print("too low")

    count += 1
    print(count)
