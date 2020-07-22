
import random

def eightballanswer():

    answers = [
    'It is certain',
    'It is decidedly so',
    'Without a doubt',
    'Yes definitely',
    'You may rely on it',
    'As I see it, yes',
    'Most likely',
    'Outlook good',
    'Yes',
    'Signs point to yes',
    'Reply hazy try again',
    'Ask again later',
    'Better not tell you now',
    'Cannot predict now',
    'Concentrate and ask again',
    'Don\'t count on it',
    'My reply is no',
    'My sources say no',
    'Outlook not so good',
    'Very doubtful'
    ]
    print(random.choice(answers))

def main():
    while True:
        play = input('Ask the random 8 Ball a question (done to exit): ')
        if play == 'done':
            break
        else:
            eightballanswer()

main()