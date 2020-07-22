print("Welcome to Grady's Grading Grader Calc!")
numberGrade = input("What was your numerical grade? Enter 0 - 100  ")
intGrade = int(numberGrade)
print("Your grade was: " + numberGrade + "!")

if intGrade < 60:
    print('You got an F') 
elif intGrade >= 90 < 100:
    print('You got a A')
elif intGrade >= 80 < 89:
    print('You got a B')
elif intGrade >= 70 < 79:
    print('You got a C')
elif intGrade >= 60 < 69:
    print('You got an D')
else:
    print("Dunno Browski!")