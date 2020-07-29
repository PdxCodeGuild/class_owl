import random

# Defines the main function
def num_guesser():

    # Welcome message
    print("Welcome friend! Let's play a game!")
    print('I\'m going to pick and number between 1 and 10\
 and you have 10 guesses to get it!')
    print("let's play!")
    
    # Instantiate the counter
    count = 0
    # Creates the computer's number
    compy = str(random.randint(1,10))
    
    # Main loop
    while count <10:
        user_guess = input(f'Enter a number! You have {10-count} guesses left.\n')
        if not user_guess.isdigit():
            print("Way to waste a guess, scrub.\n")
            count +=1
            continue
        
        # Increasing the counter
        count += 1        

        # Breaks the loop
        if user_guess == compy:
            print(f'Good guess! It was {compy}!')
            print(f"It only took you {count} tries!")
            break
        else:
            print('Nope!')

    if count == 10:
        print(f"Looks like I win, sucker! I chose {compy}!")












if __name__ == "__main__":
    num_guesser()