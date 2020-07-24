# generate a password of length n using a while loop and random.choice
# ill be a string of random characters
import random
import string

def password_gen():
    """Generates a random password
    """
    
    # Build a list to choose from 
    chars = string.ascii_letters + string.punctuation
    
    # Print a welcome screen
    print("Welcome to the P.a.s.s.w.o.r.d Gen 5000.")
    
    # Ask the user to define the length of the password
    pass_len = input("Enter how long you would like your password: ")
    
    # verify it is a number
    while not pass_len.isdigit() or pass_len == '0':
        print("ERR: Please enter a NUMBER greater than 1 (INT)\n")
        pass_len = input("Enter how long you would like your password: ")
    # Convert to an integer
    pass_len = int(pass_len)    
    
        

    password = ''
    # Use a loop to create the password
    while len(password) < pass_len:
        password += random.choice(chars)

    print(f" Congrats! Your new password is \'{password}\'.")
    
if __name__ == "__main__":
    password_gen()