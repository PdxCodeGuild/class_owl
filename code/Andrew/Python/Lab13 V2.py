# prompts the user for a string, and encodes it with ROT13
import string

def rot13er():
    """
    Ciphers the user input using a ROT13 cipher
    """
    print("Welcome To the ROT13 cipher")
    
    # Main loop
    while True:
        # Ask for the message to be encrypted and how far to shift 
        user_input = input("Enter the message you wish to encrypt via ROT! ")
        rotter = input("How far did you want to rotate the string?(1-25) ").strip()

        while not rotter.isdigit() or rotter == '0' or rotter == '26':
            print("Please only input 1-25")
            rotter = input("How far did you want to rotate the string?(1-25) ")

        rotter =int(rotter)

        # Defines the final result as enpty string
        ciph = ''
        
        # Converts the message to a new value
        for letter in user_input:

            # Verifies that it is a letter
            if letter.isalpha():
                
                # Converts to an unicode integer
                c_num = ord(letter) + rotter 
                
                # Converts the letter if it is uppercase
                # then adds it to the result
                if letter.isupper():
                    c_num = chr(c_num) if c_num <= 90 else chr(c_num - 26)
                    ciph += c_num
                
                # Converts it if it is lowercase
                # then adds it to the result
                else:
                    c_num = chr(c_num) if c_num <= 122 else chr(c_num - 26)
                    ciph += c_num
            
            # Allows numbers, spaces and punctuation to be 
            # preserved in the result string
            else:
                ciph += letter

        # Prints the user's encrypted message
        print(f"""Your message of {user_input} was ciphered to:
{ciph}""")

        # Loop Breaker
        looper = input( "Cipher again?\n(yes/no) >>> ")
        if looper == "no":
            break


















if __name__ == "__main__":
    rot13er()