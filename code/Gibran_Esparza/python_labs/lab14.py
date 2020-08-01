#Import module
import random
# Generate a list of 6 random numbers representing the winning tickets
def pick6_generate():
    ticketnums = []
    x = 0                                  
    while x < 6:
        ticketnums.append(random.randint(1,99))
        x += 1
    return ticketnums
# Check Ticket against winning nimber
def matching_nums(winner, ticketnums):
    counter = 0
    for x in range(len(ticketnums)):
        if ticketnums[x] == winner[x]:
            counter += 1                   

    return counter
#Checking Matches to Payouts
def calculatepayout(matches):
    
    payouts = {
        0: 0,
        1: 4,
        2: 7,
        3: 100,
        4: 50000,
        5: 1000000,
        6: 25000000,
    }

    return payouts[matches]

def main():
    
    winner = pick6_generate()
    ticket_cost = 2
    balance = 0
    earnings = 0

    x= 0

    # Loop 100,000 times, for each loop:
    while x < 100000:
        ticket = pick6_generate()
        balance -= 2
        x += 1
        matches = matching_nums(winner, ticket)
        
        
        #Checking our Matches to Payouts and adding it to our Earnings
        payout = calculatepayout(matches)
        earnings += payout

    expenses = x * ticket_cost
    balance = earnings - expenses
    #ROI Calculation
    roi = (f'{(earnings - expenses) / expenses* 100}%')

    print(f"Your final balance was: ${balance}")
    print(f"Your ROI was {roi}")

main()
