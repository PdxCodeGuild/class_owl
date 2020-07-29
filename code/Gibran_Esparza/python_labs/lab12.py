#Imported my module
import random
#Picking a random number
x = random.randint(1,10)
#Setting guesses
guesses = 0

#Looping infinite amount until user guesses correctly
while True:
    guess= int(input('What is your guess: '))

    guesses += 1

    if guess == x:
        print (f'You guessed the number, it took you {guesses} guesses')
        break
    elif guess < x:
        print("Your guess is to low")
    elif guess > x:
        print*"Your guess is too high"