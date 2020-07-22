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
face = [random.choice(eyes) + random.choice(nose) + random.choice(mouth)]
print(face)