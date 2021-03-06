# Version 1 Palindrome
# Verion 2 is also included
import string

'''
The palindrome function takes the word, makes sure it's lower case
then reverses the word in another variable. Finally it compares 
them. If they match. Then 
'''
def palindrome(word):
    word1 = word.lower()
    
    word2 = word1[::-1]

    if word1 == word2:
        answer = True
    else:
        answer = False
    
    return answer

'''
This function breaks down the 2 words into lowercase words, taking out any spaces
then creating a list out of each word. Finally it sorts the word and compares them, 
returning the answer.
'''
def breakdown(word_check1, word_check2):
    word_check_one = word_check1.lower().replace(' ', '')
    word_check_two = word_check2.lower().replace(' ', '')
    list_one = list(word_check_one)
    list_two = list(word_check_two)
    list_one = sorted(list_one)
    list_two = sorted(list_two)


    if list_one == list_two:
        answer = f'the two words \'{word_check1}\' and \'{word_check2}\' are anagrams'
    else:
        answer = f'the two words \'{word_check1}\' and \'{word_check2}\' are NOT anagrams'

    return answer

'''
gets the first word to check 
'''
def user_input1():
    word_check1 = input("Please enter the word you\'d like to check as an anagram: ") 
    return word_check1


'''
gets the second word to check 
'''
def user_input2():
    word_check2 = input("Please enter the second word you\'d like to check as an anagram: ") 
    return word_check2

'''
This is the main function def. It asks for the word to compare for the anagram, and prints
the answer. Then it leads into the palidrome check, calling functions to get the words,
then printing whether it's a palindrome or not. 
'''
def main():
    word = input('Please enter a word to check if it\'s a palindrome: ')
    answer1 = palindrome(word)
    if answer1 == True:
        print (f'Your word \'{word}\', is a palindrome.')
    else:   
        print (f'Your word \'{word}\', is NOT palindrome.')

    print('Now let\'s see if two words are anagrams.')
    word_check1 = user_input1()
    word_check2 = user_input2()
    answer2 = breakdown(word_check1, word_check2) 
    print(answer2)

main()