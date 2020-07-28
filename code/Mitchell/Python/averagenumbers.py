numbers = []

while True:
    number = input("Enter number or done to calc average   ")

    if number != 'done':
        try:
            number = int(number)
        except ValueError:
            print("Enter a valid Number")
        else:
            numbers.append(number)
    elif number == 'done':
        total = 0
        for num in numbers:
            total += num
        print(total / len(numbers))
        break
