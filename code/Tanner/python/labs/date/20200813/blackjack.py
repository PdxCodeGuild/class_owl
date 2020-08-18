import random

# card class
class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit
        
    def __repr__(self):
        return f"{self.value} of {self.suit}"

    def __eq__(self, card):
        return self.value == card.value

    def equals(self, card):
        return (self.value == card.value) and (self.suit == card.suit)


# deck class
class Deck:
    def __init__(self):
        values = ["A"] + list(range(2, 11)) + ["JQK"]
        suits = ["clubs", "spades", "hearts", "diamonds"]

        self.cards = []
        for suit in suits:
            for value in values:
                card = Card(value, suit)
                #appending to list
                self.cards.append(card)

    def __str__(self):
        return str(self.cards)

    def __getitem__ (self, i):
        return self.cards[i]

    def __len__(self):
        return len(self.cards)

    def cut(self, i):
        self.cards = self.cards[i:] = self.cards[:i]

    def shuffle(self):
        random.shuffle(self.cards)

    def draw(self):
        return self.cards.pop()

    


# deck = Deck()
# deck.shuffle()
# print(deck)


# hand class
class Hand:
    def __init__(self, card1, card2):
        self.cards = [card1, card2]

    def add(self, card):
        self.cards.append(card)

    def __repr__(self):
        return str(self.cards)

    def score(self):
        points = 0
        aces = None 

        for card in self.cards:
            if type(card.value) == int:
                points += card.value
            elif card.value in "JQK":
                points += 10
            else: 
                aces = True
                points += 1

        if points <= 11 and aces:
            points += 10

# deck = Deck()
# deck.shuffle()

# hand = Hand(deck.draw(), deck.draw())
# print(hand)
# print(hand.score())
# hand.add(deck.draw())
# print(hand)
# print(hand.score())




# dealer class
#inheriting all methods from Hand class
class Dealer(Hand):
    def __init__(self, card1, card2):
        super().__init__(card1, card2)

    def face_down(self):
        hidden = Card("Hidden", "Hidden")
        return [hidden] + self.cards[1:]
    
    def visible_score(self):
        values = {"A":1, 2:2, 3:3, 4:4, 5:5, 6:6, 7:7, 8:8, 9:9, 10:10, "J":10, "Q":10, "K":10}
        hidden_card = self.card[0]
        return self.score() - values.get(hidden_card.value)

deck = Deck()
deck.shuffle()
dealer = Dealer(Card)
print(dealer.face_down())
print(dealer.score())
dealer.add(deck.draw())
print(dealer.face_down())
print(dealer.score())




# game class