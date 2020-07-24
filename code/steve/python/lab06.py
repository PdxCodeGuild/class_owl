import random
import string


def lower_generator(pass_lower):
    x = 0
    lower = ''
    while x < pass_lower:
        lower = lower + random.choice(string.ascii_lowercase)
        x += 1
    return lower

def upper_generator(pass_upper):
    x = 0
    upper = ''
    while x < pass_upper:
        upper = upper + random.choice(string.ascii_uppercase)
        x += 1
    return upper

def number_generator(pass_number):
    x = 0
    number = ''
    while x < pass_number:
        number = number + random.choice(string.digits)
        x += 1
    return number

def special_generator(pass_special):
    x = 0
    special = ''
    while x < pass_special:
        special = special + random.choice(string.punctuation)
        x += 1
    return special

def generate_password(lower, upper, digits, special):
    
    mashup = list(lower + upper + digits + special)
    random.shuffle(mashup)
    print( ''.join(mashup))



def main():
    pass_lower = int(input('How many lower case characters do you want your password to be (1-20):  '))
    pass_upper = int(input('How many upper case characters do you want your password to be (1-20):  '))
    pass_number = int(input('How many number characters do you want your password to be (1-20):  '))
    pass_special = int(input('How many special characters do you want your password to be (1-20):  '))  
    generate_password(lower_generator(pass_lower), upper_generator(pass_upper), number_generator(pass_number), special_generator(pass_special))
   

main()