# lab4 magic 8 ball
import random

answers = ["maybe", "It's possible","I'm not sure","Why would you ask that","probably","Sure why not","I dont know ","of all the questions that's what you want to ask"]

print("Welcome to the most magical 8 ball. I'll tell your future, but you might not like it.")

input("Ask me a question if you dare")

response  = random.choice(answers)

print(f"{response}")