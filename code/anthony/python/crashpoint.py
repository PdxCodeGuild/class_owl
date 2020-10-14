import random
# Class Player
class Player():

    def __init__(self, balance):
        self.balance = balance
        self.current_bet = None

    def has_money(self, bet):
        return self.balance >= bet

    def get_money(self, amount):
        self.balance += amount

    def bet(self):
        self.balance -= self.current_bet

# Class Ship
class Ship():
    def __init__(self):
        self.position = 1
        self.crash_point = 0

    def set_crash_point(self):
        rand_int = random.randint(1, 101)
        if rand_int % 33 == 0:
            self.crash_point = 1
        else:
            point = (((100 * (2**10) - rand_int) / ((2**10)-rand_int)) / 100) + random.randint(1, 11)
            self.crash_point = round(point, 2)

    def takeoff(self):
        self.position += round(random.random(), 2)



player = Player(500)

# main function

def main():
    # Welcome screen
    print("Welcome to crash point!")

    purse = int(input("How much are we playing with: $"))

    player = Player(purse)
    # Game loop
    while True:
        # Get current bet
        print(f"Current balance: {player.balance}")
        bet = int(input("How much we playing for: "))
        if player.has_money(bet):
            player.current_bet = bet
            player.bet()
        
        # Create new ship
        ship = Ship()
        ship.set_crash_point()
        

        # while ship position < crash point
        while ship.position < ship.crash_point:
            # Ask if continue
            print(f"Ship is at position {ship.position}")
            keep_going = input("Do you want to continue y/n? ")
            if keep_going == 'y':
                # increase ship position
                ship.takeoff()

                # if ship position > crash point
                if ship.position > ship.crash_point:
                    # take their money
                    print(f"Ship crashed at {ship.position}")
                    break
            # else
            else:
                # multiply bet by ship position
                print(f"Cashing out at {ship.position}")
                print(f"You won {player.current_bet * ship.position}")
                player.get_money(player.current_bet * ship.position)
                print(f"Ship would have crashed at: {ship.crash_point}")
                print(f"You could have won: {ship.crash_point * player.current_bet}")
                break




main()