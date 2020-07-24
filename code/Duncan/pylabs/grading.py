# Lab3 grading

num =  input("What is your number grade?")
num = int(num)

if num <= 100 and num >= 90:
    print("Congradulations you have an A!!")

elif num <= 89 and num >= 80:
    print("Congradulations you have a B.")

elif num <= 79 and num >=70:
    print("Yay you have a C")

elif num <= 69 and num >=60:
    print("ehh you have a D")    

else:
    print("Uh oh you have an F")    