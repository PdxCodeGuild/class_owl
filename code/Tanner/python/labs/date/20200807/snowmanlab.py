import random

def load_words():
    with open("english.txt") as file:
        data = file.read().split('\n')
    words = random.choice(data)
    #print(words)
    while len(words) < 5:
        words = random.choice(data)
    return words
    
def main():
    while True:
        playagain = input("would you like to play a game? Y/N: ").lower()
        if playagain in ("n", "no"):
            print("beat it nerd")
            break

        word = load_words()
        list1 = []
        for char in word:
            list1.append("_")
    #print(word)
    #print(list1)
        guesses = int(len(word) * 1.5)
        guesscount = 0
        guessed = ""
        print(f'you have {guesses} guesses for this game.')
        
        while guesscount < guesses:
            guessletter = input("Guess a letter?: ").lower()
            guesscount += 1
            guessletter = guessletter[0]
            guessed += guessletter
            print(guessed)
            if guessletter in word:
                for i in range(len(word)):
                    if guessletter == word[i]: 
                        list1[i] = guessletter
            print(f""" {list1}
            number of guesses remaining {guesses - guesscount}
            already guessed: {guessed}""")

            if "_" not in list1:
                print("you made it rain!")
                break
        else:
            print(f'get lost the word was {word}')
        
                    

    







main()


