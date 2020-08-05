

def card_validator():
    """
    Verfiies if a credit card number is valid

    """

    print('Please enter a number to vaildate!')
    card_digits = input('Enter card number (16 Digits): ').replace(' ',"")
    while not card_digits.isdigit() or len(card_digits) != 16:
        print('Example: 4556 7375 8689 9855 ')
        card_digits = input('Enter card number (16 Digits): ').replace(' ','')
    
    

    # Converts the input string into a list of ints
    num_list = list(map(int,card_digits))

    # Slices off the last digit. That is the check digit.
    check_digit = num_list.pop(-1)

    # Reverses the list
    num_list = num_list[::-1]
    
    # Loop that doubles every other number in the list and subtracts 9 if > 9
    for x in range(len(num_list)):
        if x % 2 == 0:
            num_list[x] = num_list[x] * 2 
            
            if num_list[x] > 9:
                num_list[x] = num_list[x] - 9 

    # Sums the final answer and converts it to a string 
    num_sum = str(sum(num_list))

    # compares the check digit and the last digit in the sum to determine
    # validity    
    print(num_sum[-1] == str(check_digit))

    
      



if __name__ == "__main__":
    card_validator()