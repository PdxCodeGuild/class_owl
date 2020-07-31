import random


'''
this function takes generates the winning ticket for the computer, and generating a player ticket.
it does this by generating a ticket with 6 random numbers between 1 - 99. 
'''
def ticket_generator():
    ticket = []
    i = 0
    while i <= 5:
        ticket.append(random.randint(1, 99))
        i = i + 1
        
    return ticket
'''
This function compared the computer ticket with the 100k player tickets one number at a time
to make sure that the order between the two tickets stays the same. for example. 
comp ticket:(3, 45, 23, 68, 1, 98) then we want to make sure that the player ticket matches in the same ticket index.
plyr ticket:(54, 45, 23, 87, 2, 3) would win on number 45, but not on number 3.

'''
def compare_tickets(computer_ticket, player_ticket):

    winning_number = 0
    if computer_ticket[0] == player_ticket[0]:
        winning_number = winning_number + 1
    elif computer_ticket[1] == player_ticket[1]:
        winning_number = winning_number + 1
    elif computer_ticket[2] == player_ticket[2]:
        winning_number = winning_number + 1
    elif computer_ticket[3] == player_ticket[3]:
        winning_number = winning_number + 1
    elif computer_ticket[4] == player_ticket[4]:
        winning_number = winning_number + 1    
    elif computer_ticket[5] == player_ticket[5]:
        winning_number = winning_number + 1
    
    return winning_number

'''
this function calculates the winnings for each iteration of the loop in main. then returns the winning amount. 
'''
def payout(result):
    if result == 1:
        winnings = 4
    elif result == 2:
        winnings = 7
    elif result == 3:
        winnings = 100
    elif result == 4:
        winnings = 50000
    elif result == 5:
        winnings = 1000000
    elif result == 6:
        winnings = 25000000
    else:
        winnings = 0

    return winnings

'''
This main function will track all the earnings/expenses and ROI. It has the loop to play
the game 100000 times. It's responsible for calling the other functions,
and printing the output. 
'''
def main():
    balance = 0
    expenses = 0
    earnings = 0
    i = 0 
    computer_ticket = ticket_generator()
    while i <= 99999:
            balance = balance - 2
            expenses = expenses - 2
            player_ticket = ticket_generator()
            result = compare_tickets(computer_ticket, player_ticket)
            winnings = payout(result) 
            earnings = earnings + winnings
            balance = balance + winnings
            i = i + 1

    roi = (earnings - expenses) / expenses   
    print(f'This is your final balance after playing: {balance}')
    print(f'You total earnings for the game is ${earnings}. Your total expenses ${expenses}.')
    print(f'Making your ROI for the game ${roi}.')
    print('Please play a better game!')


main()