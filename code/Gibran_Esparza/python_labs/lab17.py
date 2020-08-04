
def anagram():

    word1 = input("enter a word: ").lower().replace(" ","")
    word2 = input("enter a word: ").lower().replace(" ","")

    word1_list = list(sorted((word1)))
    word2_list = list(sorted((word2)))

    if word1_list == word2_list:
        print (f"{word1} and {word2} are anagrams !!!")
    else:
        print (f'{word1} and {word2}  are not anagrams!!!')   

def check_palindrome():
    phrase = input("enter a word: ").lower()

    if list(phrase) == list(reversed(phrase)):
        print(f'{phrase} is a palindrome')
    else:
        print(f'{phrase} is not a palindrome')


anagram()

check_palindrome()

