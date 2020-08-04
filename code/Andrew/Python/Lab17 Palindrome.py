
def palin_around():
    """
    Checks to see if user input is a palindrome
    """

    print("Hey there buddy! Let's pal around with palindromes!")

    # ASk for user input and verify it is a word
    pals = input("Enter a word and I'll see if it is one! ").strip()

    while not pals.isalpha():
        print('Well, buddy. That\'s not a word!')
        print('Can you try again?')

        pals = input("Enter a word and I'll see if it is one! ").strip()
    
    # reverse the word
    slap = pals[::-1]

    # Compare the reverse word and the input word
    if pals == slap and len(pals) == 1:
        print(f'I mean I guess {pals} is a palindrome, but it\'s only one letter...')

    elif pals == slap:
        print(f'Yep {pals} is a palindrome!')
    
    else:
        print(f'Nope! {pals} is not a palindrome!')

    









if __name__ == "__main__":
    palin_around()