'''
Convert a given number into its english representation. For example: 67 becomes 'sixty-seven'. Handle numbers from 0-99.

Hint: you can use modulus to extract the ones and tens digit.

x = 67
tens_digit = x//10
ones_digit = x%10
Hint 2: use the digit as an index for a list of strings OR as a key for a dict of digit:phrase pairs.

Version 2
Handle numbers from 100-999.

Version 3 (optional)
Convert a number to roman numerals.

Version 4 (optional)
Convert a time given in hours and minutes to a phrase.
'''
numdic{
    1:'one',
    2:'two',
    3:'three',
    4:'four',
    5:'five',
    6:'six',
    7:'seve',
    8:'eight',
    9:'nine",
    10:'ten'
}
userinput = int(input('Enter a number'))

def converter(userinput):
