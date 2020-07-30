import random

# Defines the function
def num_guesser():

    print("Welcome friend! Let's play a game!")
    print('I\'m going to pick and number between 1 and 10! Guess what it is!')
    print("let's play!")

    # Instantiates the count
    count = 0

    # Creates Computer's number
    compy = str(random.randint(1,10))

    # Main loop
    user_is_a_loser = 1
    while user_is_a_loser:
        user_guess = input(f'Enter a number! You have made {count} guesses.\n')
        if not user_guess.isdigit():
            print('That still counts. \n')
            count += 1
            continue

        # Increases the count and shows the amount of guessses
        count += 1        
        
        # Taunting
        if count >10:
            print('\nHow are you still guessing...\n')

        # Loop breaker
        if user_guess == compy:
            print(f'Good guess! It was {compy}!\n')
            print(f"It only took you {count} tries!\n")
            break
        
        # Checks to see if it is too high or too low
        else:
            if int(user_guess) > int(compy):
                print('You guessed too high!')
            else:
                print('Too low bro!')

    

if __name__ == "__main__":
    num_guesser()