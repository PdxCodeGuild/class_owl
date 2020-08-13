#This code will generate a password of length n using a while loop and random.choice, this will be a string of random characters.
#First lets set up that list and import random
import random
import string
abc = string.ascii_letters
spec = '!@#$^&*()'
#lets define the function
def randompassgen(passlength):
    ''' This function will read a given number of randomly chosen characters from a list'''
    user_input=int(passlength)
    password = random.choices(abc,k=user_input)
    return password,random.choices(spec,k = user_input)

#Next lets welcome the user
#set up a loop
while True:
    user_input = input('Welcome to the password generator! Enter the desired password length or enter done to exit')
    #error checking
    if user_input == 'done':
        print('Gooodbye')
        break
    print(randompassgen(user_input))
