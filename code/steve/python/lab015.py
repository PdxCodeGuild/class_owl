'''
The number conversion dictionary
'''

numbers_dict = {
    "single" : 
    {1 : "one",
     2 : "two",
     3 : "three",
     4 : "four",
     5 : "five",
     6 : "six",
     7 : "seven",
     8 : "eight",
     9 : "nine",
     10 : "ten",
     11 : "eleven",
     12 : "twelve",
     13 : "thirteen",
     14 : "fourteen",
     15 : "fifteen",
     16 : "sixteen",
     17 : "seventeen",
     18 : "eighteen",
     19 : 'nineteen'

    }, "double" : {
        20 : "twenty",
        30 : "thirty",
        40 : "forty",
        50 : "fifty",
        60 : "sixty",
        70 : "seventy",
        80 : "eighty",
        90 : "ninety"

    },
    "triple" :{
        100 : "hundred"
        
    }}


def build_num(number):
    hundreds = number // 100
    tens_rem = number % 100
    ones_rem = tens_rem % 10
    tens = number // 10
    ones = number % 10
    answer = ''
    hundreds_txt = ''
    tens_rem_txt = ''
    ones_rem_txt = ''
    tens_txt = ''
    ones_txt = ''

    if hundreds <= 0:
        hundreds = ''
    else:
        hundreds_txt = numbers_dict.get("triple").get(100)
    if tens_rem > 19 < 30:
        tens_rem_txt = numbers_dict.get("double").get(20)
    elif tens_rem > 29 < 40:
        tens_rem_txt = numbers_dict.get("double").get(30)
    
    answer = tens_rem_txt
    return answer




def main():
    # while True:
    #     number = input('Please enter an integer number between 1 and 999 or type done to end: ')
    #     if number == 'done':
    #         break
    #     number = int(number)
    #     answer = build_num(number)
    #     print(answer)
    number = input('Please enter an integer number between 1 and 999 or type done to end: ')
    if number == 'done':
        #break
        print('Thanks for playing')
    number = int(number)
    answer = build_num(number)
    print(answer)
    



main()