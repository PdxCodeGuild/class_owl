# lab 11 calculator




def user():
    user = input("Which function would you like to use +, -, *, /, or exit :  ")
    return user
    
        
def subtract():
    
    num1 = int(input("Enter a number you want to subtract: "))
    num2 = int(input("Enter a number you want to subtract: "))
    print(f"Answer: {num1 - num2}") 
        

    

def add():
    num1 = int(input("Enter the first number you would like to add: "))
    num2 = int(input("enter the number you would like to add by: "))
    print(f"Answer: {num1 + num2}")
                

def multiplication():
    num1 = int(input("Enter a number you want to multiply: "))
    num2 = int(input("Enter a number you want to multiply: "))
    print(f"Answer: {num1 * num2}") 

def division():
    num1 = int(input("Enter a number you want to divide: "))
    num2 = int(input("Enter a number you want to divide by: "))
    print(f"Answer: {num1 / num2}")
        

def main():
    print("Welcome to the most awesomest calculator")

    operand = user()

    if operand == "+":
        add()
    elif operand == "-":
        subtract()
    elif operand == "*":
        multiplication()
    elif operand == "/":
        division()
    elif operand == "exit":
        print("Thank you for using calc")
           

            
main()