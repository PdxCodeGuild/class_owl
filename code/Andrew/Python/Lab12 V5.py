import random

# Main function
def num_guesser():

    print("Welcome friend! Let's play a game!")
    print('Pick and number between 1 and 10 and I\'ll guess what it is!') 
    

    user_guess = input(f'Enter a number! I promise not to peek!')
    while not user_guess.isdigit():
        print('It has to be a whole number!')
        user_guess = input(f'Enter a number! I promise not to peek!')
    
    user_guess = int(user_guess)

    compy = -1
    count = 0

    while user_guess != compy:
        if user_guess >10 or user_guess < 1:
            print("Hmm. It looks like you're not interested in playing fair")
            print("Goodbye!")
            break
        
        compy = random.randint(1,10)       

        if user_guess == compy:
            count += 1        
            print(f'I got it right! It was {compy}!\n')
            print(f"It only took me {count} tries!\n")

        else:

            count += 1

    





if __name__ == "__main__":
    num_guesser()