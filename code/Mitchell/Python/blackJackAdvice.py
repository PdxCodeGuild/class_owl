deck = {
    "A": 1,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "10": 10,
    "J": 10,
    "Q": 10,
    "K": 10,

}

print("\n\t Welcome to Bob's Blistering BlackJack Adivce Bouy")
print(deck.keys())


cards1 = input("\t\t Choose the First Card from above:     ")
cards1 = cards1.upper()
while cards1 not in deck:
    cards1 = input("\t\t Choose the First Card from above:     ")
    cards1 = cards1.value()
else:
    cards1 in deck
    firstCard = deck[cards1]

cards2 = input("\t\t Choose the Second Card from above:    ")
cards2 = cards2.upper()
while cards2 not in deck:
    cards2 = input("\t\t Choose the Second Card from above:    ")
    cards2 = cards2.upper()
else:
    cards2 in deck
    secondCard = deck[cards2]

cards3 = input("\t\t Choose the Third Card from above:     ")
cards3 = cards3.upper()
while cards3 not in deck:
    cards3 = input("\t\t Choose the Third Card from above:     ")
    cards3 = cards3.upper()
else:
    cards3 in deck
    thirdCard = deck[cards3]

cardValue = (firstCard) + (secondCard) + (thirdCard)
print(cardValue)


if cardValue < 17:
    print("is Less than 17, I advise you Hit It Sista")
elif cardValue >= 17 and cardValue < 21:
    print("is greater than or equal to 17, but less htan 21, better Stay It Mister!")
elif cardValue == 21:
    print(" is on the money! BLACKJACK! WOOT WOOT")
elif cardValue > 21:
    print(" is a bust browski, you've lost the dolla bills")
