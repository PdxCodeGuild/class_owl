x = input("Turn on Calc?: ")

while True:
    
    num1 = float(input("Enter first number: "))
    op = input("Enter operator: ")
    num2 = float(input("Enter second number: "))


    if op == "+":
        print(num1 + num2)
    elif op == "-":
        print(num1 - num2)
    elif op == "*":
        print(num1 * num2)
    elif op == "/":
        print(num1 / num2)

    x = input("go again?: ")
    if x == "done":
        print("bye")
        break
    else:
        continue

