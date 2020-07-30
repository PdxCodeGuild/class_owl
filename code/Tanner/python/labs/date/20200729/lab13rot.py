import string

def encyrpt(message, shift):
    message = message.lower()
    for letter in message:
        index = string.ascii_lowercase.find(letter)
        newL= string.ascii_lowercase[(index + shift) % 26]
        message = message.replace(letter, newL)

    print(message)
def main():
    message = input("What would you like to encrypt?: ")
    shift = int(input("how many letters should we shift?: "))
    encyrpt(message, shift)

main()



