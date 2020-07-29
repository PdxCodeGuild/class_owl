
while True:
    try:
        user = input("Enter a number: ")
        user = int(user)
    except ValueError:
        print("That is not a valid number")
    else:
        print(f"Successfully converted {user} to an integer")
        break
    