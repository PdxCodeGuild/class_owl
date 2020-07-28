# Welcome the User and ask them how many characters they want the password to generate
print("Howdy do yaaalll, Welcome to Popsicle Polly's Password Pro-generator-nater")


# import the stuff#
import random, string

# create a function that generates the password

def password_generator(): 
    length = int(input("Golly Gee How long should that password be?"))
    letters = string.ascii_lowercase
    password = ''.join(random.choice(letters) for i in range(length))
    print("Your password is " + password)

password_generator()