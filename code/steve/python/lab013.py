
# def cypher(alphabet, english_text):
#     encoded_text = ''

#     for char in english_text:
#         encoded_text += alphabet[(alphabet.find(char) + 13) % 26]
#     return encoded_text

# def decypher(alphabet, rot13):
#     decoded_text = ''
#     for char in rot13:
#         decoded_text += alphabet[(alphabet.find(char) - 13) % 26]
#     return decoded_text


# def main():
#     alphabet = 'abcdefghijklmnopqrstuvwxyz'
#     english_text = input(('Please enter a string: (letters only please, no numbers, spaces or punctuation) '))
#     rot13 = cypher(alphabet, english_text)
#     print(rot13)
#     unrot13 = decypher(alphabet, rot13)
#     print(unrot13)

# main()

import string

def cypher(alphabet, english_text):
    encoded_text = ''

    for char in english_text:
        encoded_text += alphabet[(alphabet.find(char) + 13) % 26]
    return encoded_text

def decypher(alphabet, rot13):
    decoded_text = ''
    for char in rot13:
        decoded_text += alphabet[(alphabet.find(char) - 13) % 26]
    return decoded_text


def main(): 
    alphabet = string.ascii_lowercase
    english_text = input('Please enter a string: (letters only please, no numbers, spaces or punctuation) ')
    english_text = english_text.lower()
    rot13 = cypher(alphabet, english_text)
    print(f'Here is your encoded string: {rot13}')
    unrot13 = decypher(alphabet, rot13)
    print(f'Here is your decoded string: {unrot13}')

main()