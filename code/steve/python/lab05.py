import random


def emoticon():
    eyes = [';', ':', '>', '%', '!', 'O']
    nose = ['>', '-', '+', '=', '@', '<', '~']
    mouth = ['>', 'X', 'S', ')', '(', 'D', 'Z']
    print(random.choice(eyes) + random.choice(nose) + random.choice(mouth))

def main():
    play = 0
    while play < 5:
        emoticon()
        play = play + 1


main()