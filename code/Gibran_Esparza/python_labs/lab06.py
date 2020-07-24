#Generate a Passwird  of n lenght using a while loop and random.choice

#importing module

import random
import string
#Setting a variable for my password characters
password_characters = string.ascii_letters + string.digits + string.punctuation

#Askibng the user for the desired lenght of the password

lenght = int(input("What is your password desired lenght: "))

#Joined all the random characters with no space for the users desired lenght

password = ''.join(random.choices(password_characters, k=lenght))

x = 1
while x == 1:
    print (password)
    x += 1


