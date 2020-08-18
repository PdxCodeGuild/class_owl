''' create a simple calulator that can perform addition, subtraction,
multiplication, and division

Ask the user for an operator and each operand. Don't forget that input returns a string, which you can convert to a float using float(user_input) where user_input is the string you got from input. Below is some sample input/output.

> What is the operation you'd like to perform? +
> What is the first number? 5
> What is the second number? 12
> 5 + 12 = 17
Version 2
Allow the user to keep performing operations until they say 'done'. Use while True and break. Below is some sample input/output.

> what is the operation you'd like to perform? +
> what is the first number? 5
> what is the second number? 12
> 5 + 12 = 17
> what is the operation you'd like to perform? done
> goodbye! 
Version 3 (optional)
Allow the user to enter a full arithmetic expression and use eval to evaluate it.

'''
num1 = float(input('First number:  '))
operator = str(input('Operator:  '))
num2 = float(input('Next number:  '))
def adder(x,y):
    return x + y
def subtract(x,y):
    return (x - y)
def divide(x,y):
    return (x / y)
def multi(x,y):
    return (x * y)

def input_figurer(operator):
    if operator == '+':
        added = float(adder(num1,num2))
        return added
    elif operator == '-':
        sub = float(subtract(num1,num2))
        return sub
    elif operator == '/':
        div = float(divide(num1,num2))
        return div
    else:
        m = float(multi(num1,num2))
        return m
print('Welcome to the calculator, please enter a number first then an operation: +, -, /, *  ')

while input('Press enter to get result or break to leave') != 'break':
    try:
        print(input_figurer(operator))
        num1 = float(input('Enter a new first number:  '))
        operator = input('Input a new operator:  ')
        num2 = float(input('Enter a new second number:  '))
    except:
        print('You broke it!')
        break