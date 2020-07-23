import random
print("Welcome to Madame Maxine's Magic Ball")

predictions = [
    "It is certain",
    "Without a doubt",
    "You may rely on it",
    "Yes definitely",
    "It is decidedly so",
    "As I see it, maybe",
    "Most likely not happenin browski",
    "Yes",
    "No",
    "If the Thundercats is on tonight, then no, not happening",
    "Better Call Saul",
]

while True:
    question = input("Ask the Magic 8 Ball a Question, any will do! ")
    
    if question == 'done':
            break

    print("You asked " + question + "?")
    answer = random.choice(predictions)
    print("Maxine was all shook up and says  " + answer)