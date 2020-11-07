import random


# Card class
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


# card1 = Card(4, "hearts")
# card2 = Card(4, "hearts")

# print(card1 == card2)
# print(card1.equals(card2))
# Deck class
class Deck:
    def __init__(self):
        values = list(range(2, 11)) + list("AJQK")
        suits = ["clubs", "spades", "hearts", "diamonds"]

        self.cards = []
        for suit in suits:
            for value in values:
                card = Card(value, suit)
                self.cards.append(card)

    def __str__(self):
        return str(self.cards)

    def __getitem__(self, i):
        return self.cards[i]

    def __len__(self):
        return len(self.cards)

    def cut(self, i):
        self.cards = self.cards[i:] + self.cards[:i]

    def shuffle(self):
        random.shuffle(self.cards)

    def draw(self):
        return self.cards.pop()


# deck = Deck()
# deck.shuffle()
# deck.draw()
# deck.draw()
# print(len(deck))

# Hand class
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

        return points

# deck = Deck()
# deck.shuffle()

# hand = Hand(Card("A", "hearts"), Card("A", "clubs"))
# print(hand)
# print(hand.score())
# hand.add(deck.draw())
# print(hand)
# print(hand.score())


# Dealer class
class Dealer(Hand):

    def __init__(self, card1, card2):
        super().__init__(card1, card2)

    def face_down(self):
        hidden = Card("Hidden", "Hidden")
        return [hidden] + self.cards[1:]

    def visible_score(self):
        values = {'A': 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7,
                  8: 8, 9: 9, 10: 10, 'J': 10, 'Q': 10, "K": 10}
        hidden_card = self.cards[0]
        return self.score() - values.get(hidden_card.value)

# deck = Deck()
# deck.shuffle()
# dealer = Dealer(Card("A", "hearts"), Card("A", "clubs"))
# print(dealer.face_down())
# print(dealer.visible_score())
# dealer.add(deck.draw())
# print(dealer.face_down())
# print(dealer.visible_score())


# Game class

class Game:

    def __init__(self, players, cut):
        self.deck = Deck()
        self.deck.shuffle()
        self.deck.cut(cut)

        self.players = [Hand(self.deck.draw(), self.deck.draw())
                        for i in range(players)]
        # self.players = []
        # for i in range(players):
        #     player = Hand(self.deck.draw(), self.deck.draw())
        #     self.players.append(player)

        self.dealer = Dealer(self.deck.draw(), self.deck.draw())

    def play(self):
        print(f"""Dealer's hand:
        {self.dealer.face_down()}
        Score: {self.dealer.visible_score()}
        """)

        for i, player in enumerate(self.players, start=1):
            print(f"""Player {i}'s hand:
            {player}
            Score: {player.score()}
            """)

            while player.score() < 21:

                while True:
                    move = input("Hit or Stay: ").lower().strip()
                    if move in ["hit", "h", "stay", "s"]:
                        break
                if move.startswith('h'):
                    card = self.deck.draw()
                    player.add(card)
                    print(player)
                else:
                    break

            if player.score() > 21:
                print(f'Player {i} BUSTED!')
            elif player.score() == 21:
                print(f'Player {i} BLACKJACK!!!')

        print(f"""Dealer's hand:
        {self.dealer}
        Score: {self.dealer.score()}
        """)

        while self.dealer.score() < 17:
            card = self.deck.draw()
            self.dealer.add(card)

        if self.dealer.score() < 21:
            print('Dealer Stays')
        elif self.dealer.score == 21:
            print('Dealer got blackjack!')
        else:
            print('Dealer busted!')

        for i, player in enumerate(self.players, start=1):
            print(f"""Player {i}'s hand:
            {player}
            Score: {player.score()}
            """)

            if player.score() > 21 or player.score() <= self.dealer.score() <= 21:
                print(f'Player {i} loses 😢')
            else:
                print(f'Player {i} WINS 🏆')


def main():
    print("Welcome to blackjack!!! 🎲")

    while True:
        players = int(input("Enter the number of players: "))
        cut = int(input("Where do you want to cut? "))

        blackjack = Game(players, cut)
        blackjack.play()

        play_again = input("Do you want to play again? ")
        if play_again.startswith("y"):
            continue
        else:
            break


main()
