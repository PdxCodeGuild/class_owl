#Rot Cipher

#Write a program that prompts the user for a string, and encodes it with ROT13. 
# For each character, find the corresponding character, add it to an output string. 
# Notice that there are 26 letters in the English language, so encryption is the same as decryption.

#Import String Module
import string
#Defining my encode function 
def encode(user):
    #setting my english alphabet through ascii
    alphabet = string.ascii_lowercase
    #empty string that I will use to add the encoded message to
    rot13= ""
    # Finding Each character from User and alphabet and changing/adding it to Rot13
    for char in user:
        rot13 += alphabet[(alphabet.find(char)+ 13) % 26]
    return rot13
#Asking user for input string and formating lowercase to match variable above     

def main ():
    user = input("Enter a string: ").lower()
    print (encode(user))

main()

