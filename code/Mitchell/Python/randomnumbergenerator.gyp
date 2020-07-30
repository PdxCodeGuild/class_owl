import random

'''
Read 
Evaluate
Print 
Loop
''' 
while True:
    random_choice = random.randint(0, 99)
    #print(random_choice)
    user_guess = int(input('Enter a number between 0-99'))


    if user_guess == random_choice:
        print("You Guessed the number {random_choice} correctly")
    elif user_guess < random_choice:
        print("Too Low")
    elif user_guess > random_choice:
        print("too high")

    play_again = input("Would you like to play again? ").lower()
    if play_again in ["no", "nah", "nope"]:
        break