def wordy_nums():
    """
    convert numbers to their word equivalent
    """
    
    # Reference dictionaries
    base_list = {'0': 'zero', '1': 'one', '2': 'two', '3':'three',
    '4': 'four', '5': 'five', '6': 'six', '7': 'seven', '8': 'eight', '9': 'nine' }
    
    teen = {'10': 'ten', '11': 'eleven', '12': 'twelve', '13': 'thirteen', '14': 'fourteen', '15': 'fifteen', 
    '16': 'sixteen', '17': 'seventeen', '18': 'eighteen', '19': 'nineteen' }
    
    tens_list = {'1': 'ten','2': 'twenty','3': 'thirty','4': 'fourty','5': 'fifty',
    '6': 'sixty','7': 'seventy','8': 'eighty','9': 'ninety'}
    
    # Welcome screen and resultant string
    result = ''    
    print('Welcome to the Wordilizer!')
    print('Enter a number you wish to convert to word form!')
    
    # User input and verification
    user_input = input("Enter a number between 0 and 999: ").strip()
        
    while not user_input.isdigit():
        print('Whole numbers only!')
        user_input = input("Enter a number between 0 and 999: ").strip()
        
    # Prevent the user from inputting a zero in front 
    user_input = str(int(user_input))
    
    if  int(user_input) > 999:
        print("That's outside of my range!")
        print('Goodbye person who can\'t follow directions!')
        
        

        
    # Counts the length of the input string
    digits = len(user_input)
    
    # Returns the string if it is in the dictionary
    if user_input in base_list:
        result = base_list[user_input]

    # 0 - 99 converter
    elif digits == 2:
        if user_input in teen:
            result = teen[user_input]

        elif user_input in tens_list:
            result = tens_list[user_input]
            
        else:
            tens= tens_list[user_input[0]]
            ones= base_list[user_input[1]] if user_input[1] != '0' else ""
            result += tens + " " + ones

    # 100 - 999 converter
    elif digits == 3:

        hun= base_list[user_input[0]]
            
        # prevents the result from being a weird combo 
        # (e.g. one hundred eleven one)
        if user_input[1] == '1':
            tens = teen[user_input[1::]]
            ones = ''
        
        else:    
            tens= tens_list[user_input[1]] if user_input[1] != '0' else ''
            ones= base_list[user_input[2]] if user_input[2] != '0' else ''

        result +=  hun + ' hundred ' + tens + " " + ones


    print('\n', result.replace('  '," ").title())



if __name__ == "__main__":
    wordy_nums()