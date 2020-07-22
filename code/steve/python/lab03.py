
def get_grade():
    user_score = int(input('Please enter a grade number between 0-100: ')) 
    return user_score

def grade_letter(user_score):
    punct = user_score % 10     
    
    if user_score <= 59: 
        grade = 'F'
    elif user_score <= 69:
        grade = 'D'
    elif user_score <= 79:
        grade = 'C'
    elif user_score <= 89:
        grade = 'B'
    elif user_score < 100:
        grade = 'A'
    elif user_score == 100:
        grade = 'A+'

    if punct == 0:
        grade1 = ''
    elif punct < 5:
        grade1 = '-'
    elif punct == 5:
        grade1 = ''
    elif punct > 5:
        grade1 = '+'

    final_grade = f""" Your final grade is {grade}{grade1}"""



    return final_grade 

def main():
    user_score = get_grade()
    print(grade_letter(user_score))

main()