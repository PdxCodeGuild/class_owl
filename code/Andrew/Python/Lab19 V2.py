# Global dictionary

cards =     {'A': (1,10), 
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
    # Verifies the cards are in the dicitonary
    
    while True:
        card = input(f'What\'s your {c_num} card? ').upper()
        if card not in cards:
            print('That\'s not a real card.')
        
        else:
            return card



def jacks_on_jacks_on_jacks():
    # Let's write a python program to give basic blackjack 
    # playing advice during a game by asking the player for cards.

    print('I hear you need some help with your hand!')
    
    # creates the result variable and a card counter
    choice = 0
    cd_left = 3

    # Asks the user for their cards
    cd_1 = liar('first')
    cd_2 = liar('second')
    cd_3 = liar('third')

    # creates a temp list to determine amount of acess
    hand = [cd_1, cd_2, cd_3]

    # Sums the cards that aren't aces
    for x in hand:
        if x != 'A':
            choice += cards[x]       
            cd_left -= 1


    # For each ace in the hand it will either sum the A value tuple
    # or it will add one based on the value of the choice variable

    if cd_left != 0:
        for x in range(cd_left):
            if choice < 11 and cd_left == 1:
                choice += sum(cards['A'])
            if choice < 10:
                choice += sum(cards['A'])
            else:
                choice += cards['A'][0]
    


    # compares results and returns suggestion
    if choice < 17:
        print(f'{choice}, I\'d hit.')
    elif choice < 21:
        print(f'{choice}, I\'d stay.')
    elif choice == 21:
        print(f"{choice}, BLACKJACK!")
    else:
        print(f'{choice}, looks like you already busted! ')
        print('Better luck next round')
    
  



if __name__ == "__main__":
    jacks_on_jacks_on_jacks()