#Having User input a Number

grade = int(input("Enter a number between 0 and 100: "))

#Converting User Inout into a letter grade

if grade <= 100 and grade >= 90:
    print("A")
elif grade <= 89 and grade >=80:
    print("B")
elif grade <= 79 and  grade >=70:
    print("C")
elif grade <= 69 and grade >=60:
    print("D")
else:
    print("F")