def wordy_nums():
    """
    convert numbers to their roman numeral equivalent
    """
   
    result = ''

    print('Welcome to the Romanizer!')
    
    print('Enter a number you wish to convert to roman numerals!')
    
    user_input = input("Enter a number between 0 and 1000: ")
    
    while not user_input.isdigit():
        print('Whole numbers only!')
        user_input = input("Enter a number between 0 and 100: ")
    
    
    if  int(user_input) > 100:
        print("That's outside of my range!")
        print('Goodbye person who can\'t follow directions!')

    
    user_input = int(user_input)
    if user_input == 0:
        result = 'Nulla'

    while user_input != 0:

        if user_input >= 1000:
            result += "M"
            user_input -= 1000
        elif user_input >= 500:
            result += "D"
            user_input -= 500
        elif user_input >= 100:
            result += 'C'
            user_input -= 100
        elif user_input > 50:
            result += 'L'
            user_input -= 50

        elif user_input >= 10:
            result +=  'X'
            user_input -= 10

        elif user_input >= 5:
            result += 'V'
            user_input -= 5
        elif user_input >= 1:
            result += '1'
            user_input -= 1

    print(result)


if __name__ == "__main__":
    wordy_nums()