# import random module
import random

# define a list of predictions
predictions = [
    "it will rain tomorrow",
    "thunder, thunder, thunder cats, hooo",
    "better call saul",
    "yes",
    "no",
    "maybe",
    "without a doubt",
    "sure",
    "why would you ask that"
]

# display a welcome message
print("Welcome to madam maxine's magic 8 ball...")

# ask the user for their question
while True:
    user = input("You know how this works: ")

    # if input is 'done' exit
    if user == 'done':
        print("Goodbye")
        break
    if len(predictions) < 1:
        print("Ran out of predictions")
        break
    elif len(user) > 1:
        # display prediction to the user
        chosen_prediction = random.choice(predictions)
        print(chosen_prediction)
        predictions.remove(chosen_prediction)

