'''
Instructions
Print a welcome screen to the user.
Use the random module's random.choice() to choose a prediction.
Prompt the user to ask the 8-ball a question "will I win the lottery tomorrow?"
Display the result of the 8-ball.
Below are some example 'predictions':

Version 2
Using a while loop, keep asking the user for a question, if they enter 'done', exit
'''

# Hugh Fraser Magic 8 Ball Lab
print('Welcome to the amazing Magic 8 Ball!')
userinput1 = input('What is your question? ')
import random

predictions = ('''It is certain
It is decidedly so
Without a doubt
Yes definitely
You may rely on it
As I see it yes
Most likely
Outlook good
Yes
Signs point to yes
Reply hazy try again
Ask again later
Better not tell you now
Cannot predict now
Concentrate and ask again
Don't count on it
My reply is no
My sources say no
Outlook not so good
Very doubtful
Do you actually believe a piece of plastic can tell you the future
Hi!
Eggplant
Ello!
Banana!
''')
ball8 = predictions.split('\n')

userinput2 = 'yes'
while userinput2 == 'yes':
    print(random.choice(ball8))
    userinput2 = input('Would you like to continue? ')
    userinput1 = input('Next Question? ')
else:
    'Bye!'  