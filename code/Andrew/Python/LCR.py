# When the program starts, it should ask for the names of the players, until the user enters 'done'. 
# Then it should run the simulation, tell the user who won, and ask the player whether they'd like to play again.

# Each player receives at least 3 chips. Players take it in turn to roll three six-sided dice, each of which is marked with "L", "C", "R" on one side, and a single dot on the three remaining sides. For each "L" or "R" thrown, the player must pass one chip to the player to his left or right, respectively. A "C" indicates a chip to the center (pot). A dot has no effect.

# If a player has fewer than three chips left, he/she is still in the game but his number of chips is the number 
# of dice he/she rolls on his/her turn, rather than rolling all three. When a player has zero chips, he/she passes 
# the dice on his turn, but may receive chips from others and take his next turn accordingly. The winner is 
# the last player with chips left. He/she does not roll the dice, and wins the center pot. 
# If he/she chooses to play another round, he/she does not roll 3, he/she keeps his pot and plays with that.


import random

LCR_DIE = ['L','C','R','1','2','3']

class LCR_player:
    def __init__(self,name):
        self.player = name
        self.chips = 3

    def __str__(self):
        return f'Name: {self.player}, Chips: {self.chips}'


    def roll_em(self):
        die_results = []
        
        dice = self.chips if self.chips <=3 else 3
        
        for x in range(dice):
            die_results.append(random.choice(LCR_DIE))

        return die_results


    def out(self):
        if self.chips == 0:
            return True

        else:
            return False
    
    

def lcr_game():
    pot = 0
    players = []
    class_players = []
    while True:
        player_name = input('Enter player\'s name or "done" to start game: ')
        if player_name == 'done':
            break
        elif player_name in players:
            print('Name already taken.')
        else:
            players.append(player_name)

    for x in players:
        y = LCR_player(x)
        class_players.append(y)
        
    # out = 0
    ender = True
    while ender:
        out = 0
        main_out = 0
        # if pot == 3*len(class_players):
        #     break

        for x in range(len(class_players)):
            
            for z in class_players:
                if z.out():
                    out += 1
            
                if out == len(class_players)-1:
                    print('End')
                    ender = False
                    break 
            if ender == False:
                break    
                    
            
            elif class_players[x].out():
                main_out +=1
                continue
            
            else:
                y = class_players[x].roll_em()

                for die in y:
                    if class_players[x].out():
                        # out += 1
                        break
                    elif die == 'C':
                        class_players[x].chips -= 1
                        pot += 1

                    elif die == 'L':
                        class_players[x].chips -= 1
                        class_players[x-1].chips += 1 

                    elif die == 'R':
                        class_players[x].chips -= 1
                        class_players[(x+1)%len(class_players)].chips += 1 

                if class_players[x].out():
                    out +=1
                
            
            # if out == len(players)-1:
            #     print(out)
            #     ender = False
            #     break

            
            print(class_players[x],y)       
            print(f'Pot: {pot}')
            # print(y)

            # input()
    
            for x in class_players:
                print(x)
            print(out)
            # input()
    for x in class_players:
        if x.out():
            continue

        else:
            print(f'Winner: {x}')
        
        









if __name__ == "__main__":
    lcr_game()