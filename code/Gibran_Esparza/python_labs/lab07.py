

#Determine who won and tell the user

#Imported Module

import random

computer_choices = ['Rock', 'Paper', 'Scissor']


#The computer will ask the user for their choice (rock, paper, scissors)
def game():
    user_input = input('What is your choice Rock, Paper,  or Scissor: ').capitalize()

        #The computer will randomly choose rock, paper or scissors
    computer_pick = random.choice(computer_choices)

    print (f' The computer picks {computer_pick}')

        #Determine who won and tell the user

    if user_input == computer_pick:
        print ('Tie')
    elif user_input == 'Rock' and computer_pick == 'Paper':
        print ("Computer Won")
    elif user_input == 'Rock' and computer_pick == 'Scissor':
        print ("You Won")
    elif user_input == 'Scissor' and computer_pick == 'Paper':
        print ("You Won")
    elif user_input == 'Paper' and computer_pick == 'Scissor':
        print ("Computer Won")
    elif user_input == 'Paper' and computer_pick == 'Rock':
        print ("You Won")
    elif user_input == 'Scissor' and computer_pick == 'Paper':
        print ("You Won")
    elif user_input == 'Scissor' and computer_pick == 'Rock':
        print ("Computer Won")

game()

while True:
    play_again = input("Would you like to play again?").lower()

    if play_again ==  "yes":
        game()
    elif play_again == "no":
        break