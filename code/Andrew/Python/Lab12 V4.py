import random

# Main function
def num_guesser():

    print("Welcome friend! Let's play a game!")
    print('I\'m going to pick and number between 1 and 10! Guess what it is!') 
    print("let's play!")

    # Instantiates the count
    count = 0

    # Chooses the computer's number
    compy = str(random.randint(1,10))

    # Creates list to allow comparison of previous values
    picked_last = []

    # Main loop
    user_is_a_loser = 1
    while user_is_a_loser:
        user_guess = input(f'Enter a number! You have made {count} guesses.\n')
        
        # Verifies that is is a number
        if not user_guess.isdigit():
            print('That doesn\'t count. Pick a number. \n')
            continue
        

        # Inserts how far away the guess was from the correct answer
        picked_last.append(abs(int(user_guess)-int(compy)))


        # Loop Breaker
        if user_guess == compy:
            count += 1        
            print(f'Good guess! It was {compy}!\n')
            print(f"It only took you {count} tries!\n")
            break
        
        else:

            # Checks to see if the previous difference is greater than or less
            # than the most recent difference after there has been at least 
            # one guess.
            if len(picked_last) >1:
                
                # Uses the counter as the list index
                if picked_last[count-1] > picked_last[count]:
                    print('You\'re getting closer!')
                elif picked_last[count-1] == picked_last[count]:
                    print('You\' the same distance away as last time!')
                else:
                    print("looks like you're getting further away!")
                    
            # Comparison to see if the guess was too high or low
            if int(user_guess) > int(compy):
                print('You guessed too high!')

            else:
                print('Too low bro!')
            count += 1

    





if __name__ == "__main__":
    num_guesser()