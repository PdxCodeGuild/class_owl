
import random

def pick_n_loop(balance, winners):
    """
    Draws random numbers and sees if there are any matches
    """
    # Determines prizes
    prizes = [0,4,7,100,50000,1000000,25000000]
    
    # Defines amt of matching numbers and running balance
    amt = 0
    balance -= 2

    # Builds 'ticket' array
    played_nums = []
    for _ in range(6):
        played_nums.append(random.randint(1,99))
    
    # checks to see if any numbers match
    for x in played_nums:
        if x in winners and played_nums.index(x) == winners.index(x):
            amt += 1
            
    # returns balance to other function with any winnings        
    balance += prizes[amt]
    return balance

    

    

def pickr():
    """
    Simulates the depressing odds of winning the lottery
    """
    # Builds winning number array
    winning_nums = []
    for _ in range(6):
        winning_nums.append(random.randint(1,99))
    
    print('Let\'s play:')
    print('SOMEONE\'S GOTTA WIN!!!')

    balance = 0
    
    # Runs the loop 100,000 to see if you won
    for _ in range(100000):
        balance = pick_n_loop(balance, winning_nums)

    roi = (balance - 200000) / 200000
    
    print(f'Your new balance is ${balance} and you ROI is {roi}')
    


if __name__ == "__main__":
    pickr()
