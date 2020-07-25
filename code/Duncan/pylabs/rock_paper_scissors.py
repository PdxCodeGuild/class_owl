#rock paper scissors
#import mods
import random
#welcome message
print("Lets play a game")
# def variables
rps = ["rock", "paper", "scissors"]
#get input
player = input("Choose your weapon 'rock, paper, scissors' ")

spr = random.choice(rps)

print(f"I chose {spr}")

if spr == player:
    print("Tied")
if spr == "rock" and player == "paper":
    print("you won this time.")
if spr == "rock" and player == "scissors":
    print("I am invincable")
if spr == "paper"and player == "rock":
    print("I am invincable")
if spr == "paper" and player == "scissors":
    print("you have defeated me.")
if spr == "scissors" and player == "rock":
    print("you have passed this test")
if spr == "scissors" and player == "paper":
    print("I cannot be defeated")
