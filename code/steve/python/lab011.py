# Simple Calculator

def user_input(operation):
    # operation = input('Which math operation you wouldmlike to perform? ( +, -, *, /,): ')
    firstnumber = float(input('What is the first number for your operation?: '))
    secondnumber = float(input('What is the second number for your operation?: '))
    answer = math(operation, firstnumber, secondnumber)
    return answer

def math(operation, firstnumber, secondnumber):
    if operation == '+':
        answer = firstnumber + secondnumber
    elif operation == '-':
        answer = firstnumber - secondnumber
    elif operation == '*':
        answer = firstnumber * secondnumber
    elif operation == '/':
        answer = firstnumber / secondnumber
    else:
        answer = ''
    return answer
    
def main():
    while True:
        operation = input('Which math operation you would like to perform? ( +, -, *, /,): ')
        if operation == 'done':
            print('You have selected to quit. Have a nice day!')
            break
        answer = user_input(operation)
        
        if answer != '':
            print(f'The answer to your operation is: {answer}. ')
        else:
            print(f'Your operation {operation} was invalid.')

main()