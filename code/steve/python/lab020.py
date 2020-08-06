# Credit Card Validation

def validation(cust_input):
   
    input_list = list(cust_input)
    print(input_list)
    card_list = list(map(int, input_list))
    validator_num = card_list.pop()
    backward_num = card_list[::-1]
    print(backward_num)   # Remove?


    for i in range(0, len(backward_num), 2):
        backward_num[i] *= 2
    print(backward_num)     # Remove?

    for i in range(0, len(backward_num), 1):
        if backward_num[i] > 9:
            backward_num[i] -= 9
    
    print(backward_num)    

    total = sum(backward_num)
    print(total)   # Remove?
    total = str(total) [-1:]
    print(f'This is the totals last digit, {total} ')  # Remove?
    print(f'This is the validator number, {validator_num} ') # Remove?
    total = int(total)
    if total == validator_num:
        answer = True
    else:
        answer = False
    

    return answer


def main():
    cust_input = input('Please enter your credit card number to validate: ')

    answer = validation(cust_input)
    if answer == True:
        print('Your card is validated.')
    else:
        print('This is an invalid card.')
    

main()