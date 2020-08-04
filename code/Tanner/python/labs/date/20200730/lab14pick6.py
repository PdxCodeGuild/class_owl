import random

def pick6():
    ticket =[]
    x = 0
    while x < 6:
        ticket.append(random.randint(0,99))
        x += 1
    return ticket

def count_match(winning_ticket, current_ticket):
    for num in range(len(winning_ticket)):
        if winning_ticket[x] == current_ticket[x]:
            count += 1
    return count

def main():
    balance = 0
    winning_ticket = pick6()
    x = 0
    while x < 100000:
        current_ticket = pick6()
        balance -= 2

        matches = count_match()

        if matches == 1:
            balance += 4
        elif matches == 2:
            balance += 7
        elif matches == 3:
            balance += 100
        elif matches == 4:
            balance += 50000
        elif matches == 5:
            balance += 1000000
        elif matches == 6:
            balance += 25000000
    print(f'{balance}')

main()