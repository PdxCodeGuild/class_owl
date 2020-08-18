''' Have the user enter a number representing the grade (0-100)
Convert the number grade to a letter grade
Numeric Ranges
90-100: A
80-89: B
70-79: C
60-69: D
0-59: F
Version 2 (Optional)
Find the specific letter grade (A+, B-, etc). 
You can check for more specific ranges using if statements, or use modulus % to get the ones-digit to set another string to '+', '-', or ' '. 
Then you can concatenate that string with your grade string.'''

print('Welcome to the grade translator')

originaluserinput = float(input('Please enter a number '))
userinput = originaluserinput
# Letter Converter - takes any float and gives the letter grade
if userinput % 10 <5:
    gradeaug = '-'
else:
    gradeaug = '+'

if originaluserinput >= 90:
    userinput = 'A' + gradeaug
    print(userinput)
elif originaluserinput >= 80 and originaluserinput <= 89 :
    userinput = 'B' + gradeaug
    print(userinput)
elif originaluserinput >= 70 and originaluserinput <= 79  :
    userinput = 'C' + gradeaug
    print(userinput)
elif originaluserinput >= 60 and originaluserinput <= 69   :
    userinput = 'D' + gradeaug
    print(userinput)
else:
    print('F')


import random
rivalscore = random.randint(0,100)
if originaluserinput > rivalscore:
   print(f'You are better than your rival, who scored a {rivalscore}')
else:
    print('Time to hit the books! You did worse than your rival who score a {rivalscore}')