
# Addition function
def addit(v1,v2):
    sum = v1 + v2
    return sum

#Subtraction function
def subit(v1,v2):
    sum = v1 - v2    
    return sum

# Division function with Div zero err
def divit(v1,v2):
    if v2 != 0:
        sum = v1/v2
        return round(sum,2)
    else:
        return '\nDivision by zero error!'

# Multiplication function 
def multit(v1,v2):
    sum = v1*v2
    return sum



def simp_calc():
    """
    Run simple addition, subraction, multiplication and division functions
    """
    # Dictionary for final f string
    oper_dict = {'+' : 'addition', '-': 'subtraction', '*': 'multiplication', '/': 'division'} 

    print("Welcome to the simple calculator!")

    # Main loop
    while True:
        
        # Asking user operator and verifiying it is in the list
        oper = input('Please select the operation you wish to perform\n+, -, *, /\t')    
        while oper not in "+-*/":
            print("That is not a valid selection!")
            oper = input('Please select the operation you wish to perform\n+, -, *, /\t') 
               
        # Asking user for numbers and verifying ability to convert
        while True:
            val1 = input("Enter the first value: ")
            val2 = input('Enter the second value: ')
            try:
                val1 = int(val1)
                val2 = int(val2)
                break
            except ValueError:
                print("Error! Please ensure both values are integers")
                
        # Goes on to specified function via 'oper' 
        if oper == "+":
            result = addit(val1,val2)
        elif oper == "-":
            result = subit(val1,val2)
        elif oper == '*':
            result = multit(val1,val2)
        elif oper == '/':
            result = divit(val1,val2)
        
        # Result string
        print(f"Your operation of {oper_dict[oper]} resulted in: {result}", end="\n\n")

        # loop breaker
        leave_loop = input("Enter 'done' if you're finished.\
 Enter anything else to continue using the calculator.\n ").lower()

        if leave_loop == 'done':
            print("Goodbye!")
            break



if __name__ == "__main__":
    simp_calc()