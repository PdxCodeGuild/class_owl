# black jack advice




card1 = input("what is your first card?: ").capitalize()
card2 = input("what is your second card?: ").capitalize()
card3 = input("what is your third card?: ").capitalize()


if card1 == "A":
    card1 = 1
elif card1 == "K" or card1 == "J" or card1 == "Q":
    card1 = 10
elif card1.isdigit():
    card1 = int(card1)    

if card2 == "A":
    card2 = 1
elif card2 == "K" or card2 == "J" or card2 == "Q":
    card2 = 10
elif card2.isdigit():
    card2 = int(card2)        

if card3 == "A":
    card3 = 1
elif card3 == "K" or card3 == "J" or card3 == "Q":
    card3 = 10
elif card3.isdigit():
    card3 = int(card3)                

hand_value = card1 + card2 + card3


print(f"your hand value is {hand_value}")

if hand_value < 17:
    print("Hit")
elif 17 < hand_value < 21:
    print("stay")
elif hand_value == 21:
    print("thats blackjack you win")
elif hand_value > 21:
    print("you've busted sorry ")            
    

