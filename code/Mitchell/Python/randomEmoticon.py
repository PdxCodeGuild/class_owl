eyes = [
    ";",
    ":",
    "=",
    '8',
    'X'

]

nose = [
    '-',
    '^',
    '',
    'o',
    '.',
    '*',
]

mouth = [
    'P',
    'D',
    ']',
    'J',
    'O',
    'V'
]

import random

face = random.choice(eyes) + random.choice(nose) + random.choice(mouth)
count = int(input("How many faces do you want to generate?"))
while count > 0:
    face = random.choice(eyes) + random.choice(nose) + random.choice(mouth)
    print(face)
    count -= 1