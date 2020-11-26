tens = {
    1: "teen",
    2: 'twenty ',
    3: 'thirty ',
    4: 'forty ',
    5: 'fifty ',
    6: 'sixty ',
    7: 'seventy ',
    8: 'eighty ',
    9: 'ninety ',
}
singles = {
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

pre_teens = {
    10: 'ten',
    11: 'eleven',
    12: 'twelve',
    13: 'thirteen',
    14: 'fourteen',
    15: 'fifteen',


}

centuries = {
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




def main():
    number = int(input('Please enter a number between 1 and 999: '))
    if number >= 1 and number <= 9:
        print(f'The number you have chosen is {singles[number]}.')
    elif number >= 10 and number <= 15:
        print(f'The number you have chosen is {pre_teens[number]}.')
    elif number > 15 and number < 100:
        tens1 = int(number // 10)
        singles1 = int(number % 10)
        print(f'The number you have chosen is {tens[tens1]}{singles[singles1]}.')
    else:
        centuries1 = int(number // 100)
        tens1 = int(number // 10) // 10    #doesn't work
        singles1 = int(number % 10) 
        print(f'The number you have chosen is {centuries[centuries1]}{tens[tens1]}{singles[singles1]}.')


main()
