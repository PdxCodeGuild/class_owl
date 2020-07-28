#The computer will ask the user for their choice (rock, paper, scissors)
import random

options = [
    'rock',
    'paper',
    'scissors'
]


def replay():
    rematch = input('Do you want a rematch? Yes or No')
    if rematch == 'yes': 
        game()
    elif rematch != 'yes':
        print('Deuces Ma-Guces Battle Buddy')
            
    
def game():
    print('\nWelcome to the End Times Baby!!\n   Rock Paper Scissors')
    print('\tPick Your Battle Weapon')
    user_choice = input('\t\tType in Rock, Paper, or Scissors\n')
    pc_choice = random.choice(options)
    outcomes = user_choice + ' vs ' + pc_choice
    print(outcomes)
    if outcomes == 'rock vs rock':
        print('it was a tie, you live to fight another day')
    elif outcomes == 'rock vs paper':
        print('You got swamped by thin tree slices, you lose')
    elif outcomes == 'rock vs scissors':  
        print('You slaughtered Edward Scissor Hands, you win')
    elif outcomes == 'paper vs rock':
        print('Suffocated Your Foe, You Win')
    elif outcomes == 'paper vs paper':
        print('Tie Browski')
    elif outcomes == 'paper vs scissors':
        print('got shredded, you lose')
    elif outcomes == 'scissors vs rock':
        print('manufactured metal doesn\'t beat mother nature, you lose')
    elif outcomes == 'scissors vs paper':
        print('shred it, you win')
    elif outcomes == 'scissors vs scissors':
        print('alot could be said about this tie')
    replay()

game()
