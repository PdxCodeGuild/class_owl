import string
import random



def get_int(prompt):
    while True:
        num = input(prompt)
        if num.isdigit():
            return int(num)
        print("Enter a valid integer.")

def generate_password(letters, digits, punctuation):
    password = ''
    for i in range(letters):
        password += random.choice(string.ascii_letters)
    for i in range(digits):
        password += random.choice(string.digits)
    for i in range(punctuation):
        password += random.choice(string.punctuation)

    # password = list(password)
    # random.shuffle(password)
    # password = "".join(password)

    # One line string shuffle
    password = "".join(random.sample(password, len(password)))
    
    return password


def main():
    num_letters = get_int("Enter the number of letters: ")
    num_digits = get_int("Enter the number of digits: ")
    num_punctuation = get_int("Enter the number of punctuation: ")

    password = generate_password(num_letters, num_digits, num_punctuation)

    print(password)
    # print(num_letters, num_digits, num_punctuation)

main()