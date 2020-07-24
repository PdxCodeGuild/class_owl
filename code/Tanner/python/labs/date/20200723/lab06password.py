import string
import random
response = input("Would you like a password?: ")
while response == "y":
    characters = string.ascii_letters + string.digits + string.punctuation

    pLen = input("How many characters should it be?: ")
    npLen = int(pLen)
    for x in range(npLen):
        print(random.choice(characters))
