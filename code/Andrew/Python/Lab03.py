def grading():
    """convert a number grade to a letter grade"""

    # Have the user enter a number representing the grade (0-100)
    
    user_grade= input('Please input your grade: ')
    
    # Verify it can be converted to INT then convert

    while not user_grade.isdigit():
        user_grade= input('Please input your grade: ')
    
    
    user_grade = int(user_grade)


    # Convert the number grade to a letter grade
    
    if 100 >= user_grade >= 90:
        return 'A' 
    elif 80 <= user_grade < 90:
        return 'B'     
    elif 70 <= user_grade < 80:
        return 'C'
    elif 60 <= user_grade < 70:
        return "D"
    elif 0 <= user_grade < 60:
        return "F"
    else:
        return 'ERR: INVALID GRADE!'



if __name__ == "__main__":
    print(grading())