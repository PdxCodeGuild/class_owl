'''This python code will execute a game of madlibs on repeat'''
# first import the random module
import random
# initialize your user inpout list for the madlib to use
userlist = []

print('Hello and welcome to madlibs! Please follow the instructions or enter done at any time to leave:')
while input('Hit enter to continue, done to exit') != 'done':
    userlist = [
            input('Please enter a noun: '),
            input('Please enter a pronoun: '),
            input('Please enter an adverb: '),
            input('Please enter a verb: ')
            ]
    print(f'''Hello TotallyNotEvilCorp is looking for a {random.choice(userlist)} evasion inspector. 
    Must be willing to relocation to {random.choice(userlist)} for work or pay for travel expenses out of pocket. 
    Please be aware any aversion to {random.choice(userlist)} will result in extreme discomfort but no additional job aids.''')
    while input('Play again? ') != 'done':
        userlist = [
            input('Please enter a noun: '),
            input('Please enter a pronoun: '),
            input('Please enter an adverb: '),
            input('Please enter a verb: ')
            ]
        print(f'Hello TotallyNotEvilCorp is looking for a {random.choice(userlist)} evasion inspector. Must be willing to relocation to {random.choice(userlist)} for work or pay for travel expenses out of pocket. Please be aware any aversion to {random.choice(userlist)} will result in extreme discomfort but no additional job aids.')