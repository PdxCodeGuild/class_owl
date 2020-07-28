#Defining my functions for the operations

def addition(number1, number2):
        return number1 + number2
def subtraction(number1, number2):
        return number1 - number2
def multiplication(number1, number2):
        return number1 * number2
def division(number1, number2):
        return number1 / number2


def main ():
    while True:
        calculate = input('Would you like to calculate something yes or no:').lower()
        if calculate == 'yes':
            Operation = eval(input('What is the operation you would like to perform? Choose +, -, *, /: '))
            Fnumber = int(input('What is the first number : '))
            Snumber = int(input('What is the second number : '))
        
            if Operation == '+':
                print (f'{Fnumber} + {Snumber} = ', addition(Fnumber,Snumber))
            elif Operation == '-':
                print (f'{Fnumber} - {Snumber} = ', subtraction(Fnumber,Snumber))
            elif Operation == '*':
                print (f'{Fnumber} * {Snumber} = ', multiplication(Fnumber,Snumber))
            elif Operation == '/':
                print (f'{Fnumber} / {Snumber} = ', division(Fnumber,Snumber))
    
        elif calculate == 'no':
            print ("Thank you")
            break
        else:
            print("that is not a valid choice")
    
main()