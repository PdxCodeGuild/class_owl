

# Ask user for input
# numbers = []
# while True:
#     number = input("Enter a number or 'done' to calculate average: ")


#     # Add input to list
#     if number != 'done':
#         try:
#             number = int(number)
#         except ValueError:
#             print("Enter a valid number")
#         else:
#             numbers.append(number)
#     elif number == 'done':
#         # Calculate average of list
#         total = 0
#         for num in numbers:
#             total += num

#         print(f"The average of numbers entered is {total / len(numbers)}")
#         break


numbers = []
while True:
    number = input("Enter a number or 'done' to calculate average: ")
    # Add input to list
    numbers.append(number)
    
    # Calculate average of list
    if number == 'done':
        total = 0
        count = 0 
        for num in numbers:
            if num.isdigit():
                num = int(num)
                total += num
                count += 1
        print(f"The average of numbers entered is {total / count}")
        break