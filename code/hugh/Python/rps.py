#make a function to play rock paper scissors with the computer
import random
#define the choices
rpschoices = ['rock','paper','scissors']
#funky function time
def rpsfunktion(user_input,rps_choice):
    rps_choice = random.choice(rpschoices)
    if user_input == 'rock':
        if rps_choice == 'paper':
            print('You lost')
        elif rps_choice == 'rock':
            print('Tie!')
        elif rps_choice == 'scissors':
            print('You won!')
        else:
            print('You lost!')
    elif user_input == 'paper':
        if rps_choice == 'sciccors':
            print('You lost')
        elif rps_choice == 'rock':
            print('You won!')
        elif rps_choice == 'paper':
            print('Tie!')
        else:
            print('You lost!')
    elif user_input == 'scissors':
        if rps_choice == 'paper':
            print('You won!')
        elif rps_choice == 'rock':
            print('You lost!')
        elif rps_choice == 'scissors':
            print('Tie!')
        else:
            print('You lost!')
def main():
    print('Welcome to the rock paper scissors game.')
    rps_choice = input('Please enter rock, paper, or scissors')
    rpsfunktion(rps_choice)

main()