
# Create dictionary for username: {password: , security question: , answer: }
users = {
    "bradpitt57": {
        "password": "password123",
        "question": "What is Brad's last name?",
        "answer": "Pitt"
    },
    "soccervansarecool2": {
        "password": "owen87",
        "question": "Year of birth?",
        "answer": "1987"
    }
}

# Function for logging in
def login():
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    # Calls the is_valid function to return true if valid username, false if not
    if is_valid(username, password):
        print(f"Welcome {username}.")
    else:
        print("Invalid username or password.")

# Function for signing up
def signup():
    username = input("Select a username: ")

    # If the username exists, ask for a new username
    while username in users:
        print("Username already exists")
        username = input("Select a username: ")
    
    password = input("Enter a password: ")
    password2 = input("Re-enter your password: ")

    # Verify the user entered in the same password twice, if not return(leave function)
    if password != password2:
        print("The passwords do not match")
        return
    else:
        question = input("Enter a security question: ")
        answer = input("Answer: ")

        # Add the newly created user to the users dictionary
        users[username] = {
            "password": password,
            "question": question,
            "answer": answer
        }

        # Display a success message to the user
        print("Signed up successfully.")
    



# Function to check if username/password is valid
def is_valid(username, password):
    '''Function to check if a valid username and password has been entered'''
    if username in users:
        if password == users[username]["password"]:
            return True
    return False

# Function for forgotten password
def reset():
    username = input("Enter your username: ")

    # If a valid username is entered continue, else print user does not exist
    if username in users:
        answer = input(users[username]["question"])

        # Check to see if answer entered matches answer in dictionary
        if answer == users[username]["answer"]:
            password = input("Enter a new password")
            password2 = input("Verify your password: ")

            # Verify password was entered correctly
            if password != password2:
                print("The passwords do not match")
                return
            else:
                users[username]["password"] = password
                print("Password updated!")
        # If answer does not match, tell the user and return (leave function)
        else:
            print("Answer does not match security question.")
            return
    else:
        print("User does not exist")

# Menu
def menu():
    '''Reusable menu'''

    print("""Choose one of the following: 
    1) login
    2) signup
    3) reset password
    4) Exit""")
    choice = input(">")
    return choice.lower()

# Main function
def main():
    print("Welcome to SuperSecure Bank Co.")

    # while True loop to keep the program running
    while True:
        choice = menu()

        # Check to see what the user entered and call the appropriate function
        if choice == "1" or choice == "login":
            login()
        elif choice == "2" or choice == "signup":
            signup()
        elif choice == "3" or choice == "reset":
            reset()
        elif choice == "4" or choice == "exit":
            break
        else:
            print(f"Invalid choice: {choice}.")

main()