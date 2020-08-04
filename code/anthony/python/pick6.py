import random

# Generate a list of 6 random numbers representing the winning tickets
# Start your balance at 0
# Loop 100,000 times, for each loop:
# Generate a list of 6 random numbers representing the ticket
# Subtract 2 from your balance (you bought a ticket)
# Find how many numbers match
# Add to your balance the winnings from your matches
# After the loop, print the final balance


def pick6():
    ticket = []
    x = 0
    while x < 6:
        ticket.append(random.randint(0, 99))
        x += 1

    return ticket

def count_match(winning_ticket, current_ticket):
    count = 0
    for x in range(len(winning_ticket)):
        if winning_ticket[x] == current_ticket[x]:
            count += 1

    return count



def main():
    no_of_tickets = 100000
    balance = 0
    earnings = 0
    winning_ticket = pick6()

    results = {
        0: 0,
        1: 0,
        2: 0,
        3: 0,
        4: 0,
        5: 0,
        6: 0
    }


    x = 0
    while x < no_of_tickets:
        x += 1
        current_ticket = pick6()
        balance -= 2

        matches = count_match(winning_ticket, current_ticket)

        if matches == 1:
            balance += 4
            earnings += 4
            results[1] += 1
        elif matches == 2:
            balance += 7
            earnings += 7
            results[2] += 1
        elif matches == 3:
            balance += 100
            earnings += 4
            results[3] += 1
        elif matches == 4:
            balance += 50000
            earnings += 50000
            results[4] += 1
        elif matches == 5:
            balance += 1000000
            earnings += 1000000
            results[5] += 1
        elif matches == 6:
            balance += 25000000
            earnings += 25000000
            results[6] += 1
        else:
            results[0] += 1

    expenses = no_of_tickets * 2
    ROI = (earnings - expenses) / expenses
    print(f"Ending balance is ${balance}")
    print(f"{ROI=}")
    print(f"""
    No Match: {results[0]}
    1 Match: {results[1]}
    2 Match: {results[2]}
    3 Match: {results[3]}
    4 Match: {results[4]}
    5 Match: {results[5]}
    6 Match: {results[6]}
    """)
main()

    
