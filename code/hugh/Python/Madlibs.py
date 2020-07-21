'''This python code will execute a game of madlibs on repeat'''
# first import the random module
import random
# initialize your user inpout list for the madlib to use
userlist = [print(f'Please enter a noun: {input()}'),
print(f'Please enter a pronoun: {input()}'),
print(f'Please enter an adverb: {input()}'),
print(f'Please enter a verb: {input()}')
]
while print(f'Hello and welcome to madlibs! Please follow the instructions or enter done at any time to leave: {input()}') != 'done':
    print(f'Hello TotallyNotEvilCorp is looking for a {random.choice(userlist)} evasion inspector. Must be willing to relocation to {random.choice(userlist)} for work or pay for travel expenses out of pocket. Please be aware any aversion to {random.choice(userlist)} will result in extreme discomfort but no additional job aids.')
    while print(input('Type done to leave, update to change your words, and enter to shake up the madlib')) != 'done':
        for words in userlist:
            userlist = input()