import math, random 

#Generate a list of 6 random numbers representing the winning tix

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

def main():
    no_of_tickets = 100000
    earnings = 0
    balance = 0
    winning_ticket = pick6()

    results = {
        1: 0,
        2: 0,
        3: 0,
        4: 0,
        5: 0,
        6: 0,
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
        elif matches == 1:
                balance += 7
                earnings += 7
                results[2] += 1
        elif matches == 3:
                balance += 100
                earnings += 100
                results[3] += 1
        elif matches == 4:
                balance += 5000
                earnings += 5000
                results[4] += 1
        elif matches == 5:
                balance += 1000000
                earnings += 1000000
                results[5] += 1
        elif matches == 6:
                balance += 250000000
                earnings += 250000000
                results[6] += 1
    expenses = no_of_tickets * 2
    Returnoninvestment = (earnings - expenses) / expenses
    print(balance)
    print(Returnoninvestment)
    print(
        results
    )

main()