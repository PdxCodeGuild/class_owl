# Have the user enter a grade
print("Welcome to the grading calculator!")
# grade = int(input("Enter your number grade: "))

grades = []
while True:
    grade = input("Enter your number grade or 'done' to quit: ").lower()

    if grade == "done":
        average = sum(grades) / len(grades)
        print(f"Your GPA is {average / 25}")
        print("goodbye")
        break

    # Convert the grade to an integer
    while not grade.isdigit():
        grade = input("Enter your number grade: ")

    grade = int(grade)
    grades.append(grade)

    # Determine + or - grade
    modifier = ""
    ones_digit = grade % 10
    if ones_digit > 5 or grade == 100:
        modifier = "+"
    elif ones_digit < 5:
        modifier = "-"



    # Check grade against ranges
    if 90 <= grade <= 100:
        print(f"You got an A{modifier} broski")
    elif 80 <= grade < 90:
        print(f"You got a B{modifier}")
    elif 70 <= grade < 80:
        print(f"You got a C{modifier}")
    elif 60 <= grade < 70:
        print(f"You got a D{modifier}")
    elif 0 <= grade < 60:
        print("You got an F, step it up!")
    else:
        print("Invalid input")

    average = sum(grades) / len(grades)
    print(f"Your average is {average}")