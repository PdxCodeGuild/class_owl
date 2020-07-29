#create a blank dictionary to hold Users
users = {
    "bradpitt57": {
        "password": "password123", 
        "question": "What is Brad's Last Name?",
        "answer": "Pitt",
    },
    "mitchell": {
        "password": "owen87",
        "quetion": "year of birth?",
        "answer": "1987"
    }
}
#function for logging in 
def login():
    username = input("Enter your username:  ")
    password = input("Enter your password:  ")
    if is_valid(username, password):
        print("welcome" + username)
    else:
        print("Invalid username or password")
#function for signing up
def signup():
    username = input("Select a username:  ")
    while username in users:
        print("username already ecists")
        username = input("select a username")
    
    password = input("input a password")
    password2 = input("re-enter your password")

    if password != password2:
        print("the passwords do not match")
        return
    else:
        question = input("What is a security question? ")
        answer = input("what is the answer? ")
        users[username] = {
            "password": password,
            "question": question,
            "answer": answer
        }
        print("Registered Successfully")
#function to check if valid
def is_valid(username, password):
    if username in users:
        if password == users[username["password"]]:
            return True
        

#forgot password
def reset():
    username = input("Enter a username:  ")
        if username in users:
            answer = input(users[username]["question"])

            
#Menu
def menu():
    print(""""Choose one of the following
        1. Login
        2. Signup
        3. reset password""")
    choice = input(">")
    return choice.lower()
#Main Function
def main():
    print("Welcome to the SuperSecure Bank Co.")
    choice = menu()
    if choice == "1" or choice == "login":
        login()
    elif choice == "2" or choice == "signup":
        signup()
    elif choice == "3" or choice == "reset password":
        reset()
    else:
        print("Invalid Choice")

main()
