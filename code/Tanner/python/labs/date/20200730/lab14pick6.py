import random

#1. A ticket contains 6 numbers, 1 to 99,
#and the number of matches between the ticket and the winning numbers determines the payoff.
#2. Order matters, if the winning numbers are [5, 10] and your ticket numbers are [10, 5] you have 0 matches.
#3. If the winning numbers are [5, 10, 2] and your ticket numbers are [10, 5, 2], you have 1 match.
#4. Calculate your net winnings (the sum of all expenses and earnings).

def winNums():
    winNums = [random.randint(1,99) for x in range(6)]
    print(winNums)

def yourNums():
    your_ticket = [int(input("what is your first number?: ")),
                   int(input("what is your second number?: ")),
                   int(input("what is your third number?: ")),
                   int(input("what is your fourth number?: ")),
                   int(input("what is your fifth number?: ")),
                   int(input("what is your sixth number?: "))]

    print(your_ticket)


def count():
    yourNums()
    winNums()
    count = 0

    for x in range(len(winNums())):
        if winNums[x] == yourNums [x]:
            print(x)
            count += 1


def prizes():
    prizes = {1 : 4,
              2 : 7,
              3 : 100,
              4 : 50000,
              5 : 1000000,
              6 : 25000000}

    for prize in prizes:
        prize[count] = prize.get(count, 0) + 1
        print(prize, prize[count])

        if count == 1:
            print("you win $4")
        elif count == 2:
            print("you win $7")
        elif count == 3:
            print("you win $100")
        elif count == 4:
            print("you win $50000")
        elif count == 5:
            print("you win $1000000")
        elif count == 6:
            print("you win 25000000")

def roi():

count()


