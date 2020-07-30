print("Welcome to Calvin's Calculated Calculater")

def add(num1, num2):
        return num1 + num2
def subtract(num1, num2):
        return num1 - num2
def multiply(num1, num2):
        return num1 * num2
def divide(num1, num2):
        return num1 / num2





        
def calculator():
    while True:
        num1 = input("Enter Number or type done: ")
        if num1 == str("done"):
            break
        else:
            num1 == float(num1)
        num1 = float(num1)
        num2 = float(input("Enter Another Number: "))
        print('Select either + - * / ?   ')
        selection = input("+, -, *, /")
        if selection == '+':
            result = add(num1, num2)
        elif selection == '-':
            result = subtract(num1, num2)
        elif selection == '*':
            result = multiply(num1, num2)
        elif selection == '/':
            result = divide(num1, num2)
        else:
            result = print("invalid input")
        print(result)
        
calculator()
    