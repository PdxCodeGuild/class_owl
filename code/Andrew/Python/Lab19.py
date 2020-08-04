
# Global dictionary

cards =     {'A': 1, 
             '2': 2,
             '3': 3,
             '4': 4,
             '5': 5,
             '6': 6,
             '7': 7,
             '8': 8,
             '9': 9,
             '10': 10,
             'J': 10,
             'Q': 10,
             'K': 10
             }

def liar(c_num):
    # Checks to see if the user is a liar about their cards
    # (A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, or K)
    
    while True:
        card = input(f'What\'s your {c_num} card? ').upper()
        if card not in cards:
            print('That\'s not a real card.')
        
        else:
            return card



def jacks_on_jacks_on_jacks():
    # Let's write a python program to give basic blackjack 
    # playing advice during a game by asking the player for cards.

    print('I hear you need som help with your hand!')
    
    # Asks the user for their cards and verifies they are real
    cd_1 = cards[liar('first')]
    cd_2 = cards[liar('second')]
    cd_3 = cards[liar('third')]

    # Adds the cards together
    choice = cd_1 + cd_2 + cd_3
    
    # Prints the result and suggestion

    if choice < 17:
        print(f'{choice}, I\'d hit.')
    elif choice < 21 :
        print(f'{choice}, I\'d stay.')
    elif choice == 21:
        print(f"{choice}, BLACKJACK!")
    else:
        print(f'{choice}, looks like you already busted! ')
        print('Better luck next round')
    
  


if __name__ == "__main__":
    jacks_on_jacks_on_jacks()