import random

# Define a list of eyes
eyes = [";", ":", "=", "X", "x", "8"]
# Define a list of noses
noses = ["", " ", "-", "~", "^", "*", "o", "+", "."]
# Define a list of mouths
mouths = ["|", ")", "]", "O", "P", "D", "3"]
# Randomly pick a set of eyes
count = int(input("How many faces? "))
while count > 0:
    eye = random.choice(eyes)
    # Randomly pick a nose
    nose = random.choice(noses)
    # Randomly pick a mouth
    mouth = random.choice(mouths)
    # Assemble and display the emoticon
    face = eye + nose + mouth
    # face = random.choice(eyes) + random.choice(noses) + random.choice(mouths)

    print(face)
    count -= 1