import random

rps = ["r", "p", "s"]

play = "true"

while play == "true":
    cmove = random.choice(rps)
    pmove = input("What is your choice?")
    print("the computer chose..", cmove)
    if pmove == cmove:
        print("tie")
    if pmove == "r" and cmove == "s":
        print("you win")
    if pmove == "s" and cmove == "r":
        print("you lose")
    if pmove == "p" and cmove == "s":
        print("you lose")
    if pmove == "s" and cmove == "p":
        print("you win")
    if pmove == "p" and cmove == "r":
        print("you win")
    elif pmove == "r" and cmove == "p":
        print("you lose")
    else:
        pmove == 'done'
        print("come again")
        break
