# Guess the number
import random


'''
Version 1
'''

# comp_number = random.randint(1, 10)
# i = 0
# while i < 10:
#     player_input = int(input('Please select a number between 1-10:'))
#     if player_input == comp_number:
#         print('Congratulations, you guessed the correct number!')
#         break
#     else:
#         print('You guessed incorrectly')
#         i = i + 1


# print(comp_number)

'''
Version 2
'''


# comp_number = random.randint(1, 10)
# guess = 0
# while True:
#     player_input = int(input('Please select a number between 1-10:'))
#     if player_input == comp_number:
#         print('Congratulations, you guessed the correct number!')
#         guess = guess + 1
#         print(f'You guessed {guess} many times.')
#         break
#     else:
#         print('You guessed incorrectly')
#         guess = guess + 1

'''
Version 3
'''

comp_number = random.randint(1, 10)
guess = 0
while True:
    player_input = int(input('Please select a number between 1-10:'))
    if player_input == comp_number:
        print('Congratulations, you guessed the correct number!')
        guess = guess + 1
        print(f'You guessed {guess} many times.')
        break
    else:
        if player_input < comp_number:
            print('You guessed You guessed too low')
        else:
            print('You guessed too high')
        guess = guess + 1