# write a program to simulate the classic "Magic Eight Ball"
# Use the random module's random.choice() to choose a prediction.
import random
def magic_eight():
    user_finished =''
    while user_finished != 'done':

        resp = ['It is certain', 'It is decidedly so',
        'Without a doubt','Yes, definitely', 'You may rely on it',
        'As I see it, yes', 'Most likely', 'Outlook good', 'Yes',
        'Signs point to yes', 'Reply hazy try again', 'Ask again later',
        'Better not tell you now', 'Cannot predict now', 'Concentrate and ask again',
        'Don\'t count on it', 'My reply is no', 'My sources say no',
        'Outlook not so good', 'Very doubtful']
        
        # Print a welcome screen to the user.

        print('Welcome to the Magic Eight Simulator!')

        # Prompt the user to ask the 8-ball a question "will I win the lottery tomorrow?"
        user = input('Please ask a question so I may divine an answer! ')

        print('Interesting question!\nLet me see...\n')

        # Display the result of the 8-ball.
        print(f"{random.choice(resp)}")

        user_finished = input('\nType \'done\' if you\'ve had enough,\nUnless you\'d\
 like to ask another question? ')
        











if __name__ == "__main__":
    magic_eight()
