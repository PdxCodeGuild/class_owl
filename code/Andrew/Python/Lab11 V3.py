



def simp_calc():
    """
    User defines the function and runs calculator
    """
    
    print("Welcome to the simple calculator!")

    # Main loop
    while True:
        
                      
        # Asking user for numbers and verifying ability to convert
        while True:
            x = input("Enter the first value: ")
            y = input('Enter the second value: ')
            try:
                x = int(x)
                y = int(y)
                break
            except ValueError:
                print("Error! Please ensure both values are integers")

            
        
        # Evaluation loop
        while True:
                       
            print(f"x: {x} , y: {y}")        
            user_equation = input('Please enter the equation you wish to perform using X and Y:\n ').lower()
            
            # Ensure they use the correct variables
            if "x" not in user_equation or "y" not in user_equation:
                print("Please use the defined variables (x,y")
                continue
            
            # Catches the divide by zero error and name error if somehow the previous loop doesn't
            try:
                result = eval(user_equation)
                print(result)
                break
            except (NameError,ZeroDivisionError):
                if y == 0:
                    print("Zero Division Error: Cannot perform task")
                    break   
                else:    
                    print("Ensure you use the correct variable names!(x, y)")
        
        # Breaks the loop when required
        br = input("Enter 'done' to exit. Enter anything else to keep using the calculator: \n\t ").lower()
        if br =='done':
            break

        
        


if __name__ == "__main__":
    simp_calc()