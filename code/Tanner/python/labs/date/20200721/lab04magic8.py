import random

choices = ["It is certain", "Yes", "My reply is no", "who knows"]

question = input("Would you like to ask a question?: ")


while question == "yes":
    print("Ask your question.")
    response = random.choice(choices)
    print("Loading...")
    print(response)
    break

if question == "no":
    print('Goodbye')





