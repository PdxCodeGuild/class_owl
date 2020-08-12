def get_users():
    with open("users.csv") as file:
        text = file.read().split('\n')

    headers = text[0]
    data = text[1:]

    headers = headers.split(",")

    user_data = []
    for user in data:
        user_data.append(user.split(','))

    users = []
    for user in user_data:
        current_user = {}
        for i in range(len(headers)):
            current_user[headers[i]] = user[i]
        users.append(current_user)

    return users, headers

def save_users(users, headers):
    output = ""
    output += ",".join(headers) + "\n"

    for i in range(len(users)):
        if i != len(users) - 1:
            output += ",".join(list(users[i].values())) + "\n"
        else:
            output += ",".join(list(users[i].values()))

    with open("users.csv", "w") as file:
        file.write(output)


# Function for logging in
def login(users):
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    # Calls the is_valid function to return true if valid username, false if not
    if is_valid(username, password, users):
        print(f"Welcome {username}.")
    else:
        print("Invalid username or password.")

# Function for signing up
def signup(all_users):
    username = input("Select a username: ")

    # If the username exists, ask for a new username
    users = []
    for user in all_users:
        users.append(user['username'])

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
        

        # Display a success message to the user
        print("Signed up successfully.")
    return all_users
    



# Function to check if username/password is valid
def is_valid(username, password, users):
    '''Function to check if a valid username and password has been entered'''
    # if username in users:
    #     if password == users[username]["password"]:
    #         return True
    # return False
    for user in users:
        if username == user['username']:
            if password == user['password']:
                return True
    return False

# Function for forgotten password
def reset(all_users):
    username = input("Enter your username: ")

    users = []
    for user in all_users:
        users.append(user['username'])

    # If a valid username is entered continue, else print user does not exist
    if username in users:
        index = users.index(username)
        answer = input(all_users[index]["question"])

        # Check to see if answer entered matches answer in dictionary
        if answer == all_users[index]["answer"]:
            password = input("Enter a new password")
            password2 = input("Verify your password: ")

            # Verify password was entered correctly
            if password != password2:
                print("The passwords do not match")
                return all_users
            else:
                all_users[index]["password"] = password
                print("Password updated!")
                return all_users
        # If answer does not match, tell the user and return (leave function)
        else:
            print("Answer does not match security question.")
            return all_users
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
        users, headers = get_users()
        choice = menu()

        # Check to see what the user entered and call the appropriate function
        if choice == "1" or choice == "login":
            login(users)
        elif choice == "2" or choice == "signup":
            users = signup(users)
        elif choice == "3" or choice == "reset":
            users = reset(users)
        elif choice == "4" or choice == "exit":
            save_users(users, headers)
            break
        else:
            print(f"Invalid choice: {choice}.")
        save_users(users, headers)

main()

