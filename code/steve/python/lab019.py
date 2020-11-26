''' 
Let's write a python program to give basic blackjack playing 
advice during a game by asking the player for cards. First, 
ask the user for three playing cards 
(A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, or K). 
Then, figure out the point value of each card individually. 
Number cards are worth their number, all face cards are worth 10. 
At this point, assume aces are worth 1. 
Use the following rules to determine the advice:
Less than 17, advise to "Hit"
Greater than or equal to 17, but less than 21, advise to "Stay"
Exactly 21, advise "Blackjack!"
Over 21, advise "Already Busted"
Print out the current total point value and the advice.
What's your first card? Q
What's your second card? 2
What's your third card? 3
15 Hit
What's your first card? K
What's your second card? 5
What's your third card? 5
20 Stay
What's your first card? Q
What's your second card? J
What's your third card? A
21 Blackjack!
Version 2 (optional)
Aces can be worth 11 if they won't put the total point value of both 
cards over 21. Remember that you can have multiple aces in a hand. 
Try generating a list of all possible hand values by doubling 
the number of values in the output whenever you encounter an ace. 
For one half, add 1, for the other, add 11. 
This ensures if you have multiple aces that you account for 
the full range of possible values.
'''

# card dictionary

card_values = {'A': (1,11), 
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

def blackjack_advice():
    # This gives basic blackjack advice during a game. 
    # this asks the player for 3 valid cards.

    print('Let me give you some Blackjack advice!')

    # create the hand total and hoe many cards left = (Aces)
    cards_total = 0
    cards_left = 3

    # Asks the user for their cards
    x = False
    y = False
    z = False
    while x is False:
        card1 = input(f'What\'s your first card? ').upper()
        if card1 in card_values.keys():
            x = True
        else:
            print('Please enter a valid card 1-10, or J-A')
    while y is False:
        card2 = input(f'What\'s your second card? ').upper()
        if card2 in card_values.keys():
            y = True
        else:
            print('Please enter a valid card 1-10, or J-A')
    while z is False:
        card3 = input(f'What\'s your third card? ').upper()
        if card3 in card_values.keys():
            z = True
        else:
            print('Please enter a valid card 1-10, or J-A')

    # creates a list to determine amount of ace's
    player_hand = [card1, card2, card3]

    # Total of the cards that aren't aces
    for card_value in player_hand:
        if card_value != 'A':
            cards_total += card_values[card_value]       
            cards_left -= 1
            print(cards_total)


    # For each ace in the hand it will determine whether the Ace is 11 or or 1. 
    # For 2 Aces in hand it will determine the add-on total of 12 since 11x2 
    # would automactically bust the player.


    if cards_total < 11 and cards_left == 1:
        cards_total = cards_total + 11
        print(cards_total)
    if cards_total < 11 and cards_left == 2:
        cards_total = cards_total + 12
        print(cards_total)
    else:
        cards_total = cards_total + int(cards_left)
        print(cards_total)


    # using determined cards_total the software will return a suggestion
    if cards_total < 17:
        print(f'{cards_total}, I\'d hit.')
    elif cards_total < 21:
        print(f'{cards_total}, I\'d stay.')
    elif cards_total == 21:
        print(f"{cards_total}, BLACKJACK!")
    else:
        print(f'{cards_total}, Dude! You busted! ')
        print('Not everyone\'s a winner')
    
  
def main():
    blackjack_advice()


main()