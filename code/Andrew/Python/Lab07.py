# play rock-paper-scissors with the computer
import random

def rock_paper_sciss():
    """ Play a game of rock, paper scissors with a computer
    """
    # Build the choices for the computer
    computer_choices = ['Rock','Paper','Scissors']
    
    # Print welcome screen
    print('\nWelcome! Let\'s play rock, paper, scissors!')


    # Ask the use for their weapon and verify it is rock, paper or scissors
    user_choice = input("\nCHOOSE! (Rock, Paper, Scissors): ").lower()

    while user_choice.capitalize() not in computer_choices:
        print('Hmmm. It looks like you didn\'t pick a viable option. Pick again!')
        user_choice = input("CHOOSE! (Rock, Paper, Scissors): ").lower()
    
    comp = random.choice(computer_choices)
    
    user_choice = user_choice.capitalize()

    # Compare the computer and user and determine who wins

    if comp == user_choice:
        print(f'\nIt\'s a tie! The computer chose {comp} and you chose {user_choice}\n')

    elif user_choice == 'Rock':
        
        if comp == 'Paper':
            print(f'\nYou won! The computer chose {comp} and you chose {user_choice}\n')
        else:
            print(f'\nYOU LOSER! I WON! The computer chose {comp} and you chose {user_choice}\n')
    
    elif user_choice == 'Paper':
        
        if comp == 'Rock':
            print(f'\nYou won! The computer chose {comp} and you chose {user_choice}\n')
        else:
            print(f'\nYOU LOSER! I WON! The computer chose {comp} and you chose {user_choice}\n')
    
    elif user_choice == 'Scissors':
        
        if comp == 'Paper':
            print(f'\nYou won! The computer chose {comp} and you chose {user_choice}\n')
        else:
            print(f'\nYOU LOSER! I WON! The computer chose {comp} and you chose {user_choice}\n')

    










if __name__ == "__main__":
    rock_paper_sciss()