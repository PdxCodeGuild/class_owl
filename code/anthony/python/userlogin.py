
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
    if is_valid(username, password):
        print(f"Welcome {username}.")
    else:
        print("Invalid username or password.")

# Function for signing up
def signup():
    username = input("Select a username: ")
    while username in users:
        print("Username already exists")
        username = input("Select a username: ")
    
    password = input("Enter a password: ")
    password2 = input("Re-enter your password: ")

    if password != password2:
        print("The passwords do not match")
        return
    else:
        question = input("Enter a security question: ")
        answer = input("Answer: ")

        users[username] = {
            "password": password,
            "question": question,
            "answer": answer
        }

        print("Signed up successfully.")
    



# Function to check if username/password is valid
def is_valid(username, password):
    if username in users:
        if password == users[username]["password"]:
            return True
    return False

# Function for forgotten password
def reset():
    username = input("Enter your username: ")
    if username in users:
        answer = input(users[username]["question"])

        if answer == users[username]["answer"]:
            password = input("Enter a new password")
            password2 = input("Verify your password: ")

            if password != password2:
                print("The passwords do not match")
                return
            else:
                users[username]["password"] = password
                print("Password updated!")
        else:
            print("Answer does not match security question.")
            return
    else:
        print("User does not exist")

# Menu
def menu():
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
    while True:
        choice = menu()
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