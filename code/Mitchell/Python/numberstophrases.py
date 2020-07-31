# Input a number
phrase = {
    1: "teen",
    2: 'twenty-',
    3: 'thirty-',
    4: 'forty-',
    5: 'fifty-',
    6: 'sixty-',
    7: 'seventy-',
    8: 'eighty-',
    9: 'ninety-',
}
ones_digit_phrase = {
    1: "one",
    2: 'two',
    3: 'three',
    4: 'four',
    5: 'five',
    6: 'six',
    7: 'seven',
    8: 'eight',
    9: 'nine',
}

teens = {
    10: 'ten',
    11: 'eleven',
    12: 'twelve',
    13: 'thirteen',
    14: 'fourteen',
    15: 'fifteen',
}

hundred_digit_phrase = {
    1: "one hundred ",
    2: 'two hundred ',
    3: 'three hundred ',
    4: 'four hundred ',
    5: 'five hundred ',
    6: 'six hundred ',
    7: 'seven hundred ',
    8: 'eight hundred ',
    9: 'nine hundred ',
}

digit = int(input('Enter the number to convert to its written counterpart:  '))
if digit >= 1 and digit <= 9:
    print(' Your number is written as ' + ones_digit_phrase[digit])
    
elif digit >= 10 and digit <= 15:
    print(' Your number is written as ' + teens[digit])

elif digit >= 100 and digit <= 999:
    hundred_digit = int(digit // 100)
    tens_digit = int(digit // 10) // 10
    ones_digit = int(digit % 10) 
    
    def digitreturnhundred():
        hundred_half = hundred_digit_phrase[hundred_digit]
        first_half = phrase[tens_digit]
        second_half = ones_digit_phrase[ones_digit]
        print('Your number is written as ' + hundred_half + first_half + second_half)
    digitreturnhundred()

else: 
    tens_digit = int(digit // 10)
    ones_digit = int(digit % 10)

    def digitreturn():
        first_half = phrase[tens_digit]
        second_half = ones_digit_phrase[ones_digit]
        print( 'Your number is written as ' + first_half + second_half)
    digitreturn()