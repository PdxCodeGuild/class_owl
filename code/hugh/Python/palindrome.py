'''

Let's write a palindrome and anagram checker.

Palindrome
A palindrome is a word that's the same forwards or backwards, e.g. racecar. Another way to think of it is as a word that's equal to its own reverse.

Write a function check_palindrome which takes a string, and returns True if the string's a palindrome, or False if it's not.

>>> enter a word: racecar
>>> 'racecar' is a palindrome

>>> enter a word: palindrome
>>> 'palindrome' is not a palindrome
Anagram
Two words are anagrams of eachother if the letters of one can be rearranged to fit the other. e.g. anagram and nag a ram.

Write another function check_anagram that takes two strings as parameters and returns True if they're anagrams of eachother, False if they're not. The procedure for comparing the two strings is as follow:

Convert each word to lower case (lower)
Remove all the spaces from each word (replace)
Sort the letters of each word (sorted)
Check if the two are equal
>>> enter the first word: anagram
>>> enter the second word: nag a ram
>>> 'anagram' and 'nag a ram' are anagrams

'''

#Take in two strings, sort them alphabetically, see if they are equal

# string 1 will store the initial input and sort it alphabetically
string1 = sorted(input('Please enter the first string to detect anagram: '))

#storage will store the second string but not sort
storage = input('Please enter a new string)')

#sorted storage will sort the second string, leaving the original data intact
sortedstorage = sorted(storage)
#main will check for exit conditions first to prevent forever loop
def main():
    while storage != 'done':
        #if loop will compare SORTED strings
        if string1 == sortedstorage:
            print("IT'S AN ANAGRAM!")
            #storage2 acts as a breakout point
            storage2 = input('Would you like to continue? ')
            if storage2 == 'done':
                break
            else:
                continue
        else:
            print('It is not an anagram, reenter or type done to leave: ')
            break
main()