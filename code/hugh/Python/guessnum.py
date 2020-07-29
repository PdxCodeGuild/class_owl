''' This code will ask the user to select a range of numbers and then
a number within that range. The computer will then randomly guess a number
and the user will respond with higher or lower. Then the computer
will guess within the range higher or lower than the last guess'''
#import random
import random
start = int()
stop = int()
userrange = [start,stop]

#welcome user
print('Hello and welcome to the number guessing game.')
#get range input
start = int(input('Please enter the first number in your range (ex. 1 to 10 = 1): '))
stop = int(input('Please enter the end of your range (ex. 1 to 10 = 10): '))
#get number within range from user
numtoguess = int(input('Please select a number from your range for the computer to guess: '))
#loop
while True:
    #have computer guess random number within range
    randomguess = random.randrange(start,stop)
    randomguess2 = str()
    #have user tell computer if number is lower or higher than guess
    print(randomguess)
    #have computer update guess to within higher or lower range
    if randomguess != numtoguess:
        helpinput = input('Please tell the computer to guess higher or lower: ')
        if helpinput == 'lower':
            randomguess2 = random.randrange(start, randomguess)
            print(randomguess2)
        elif helpinput == 'higher':
            randomguess2 = random.randrange(randomguess, stop)
            print(randomguess2)
    else:
        print(randomguess2,' and ', numtoguess, 'match!')
        break       