#Lab10 Average Numbers

#list of numbers
nums = [5,0,8,3,4,1,6]
#sum prior to looping and adding a total 
sumtotal = 0
#looping through each element in list and keeping a running total
for num in nums:
    sumtotal += num
#Dividing our Sum by the lenght of our list  
result = (sumtotal/ len(nums)).__round__(2)

print(result)

#Version 2

#Setting an Empty List
numlist =[]
#Looping 
while True:
    #Getting User input and appending to list
    
    number = input("enter a number or 'done' to calculate average: ")
    if number != 'done':
        try:
           number = int(number) 
        except ValueError:
            print("Enter a valid message")
        else:
            numlist.append(number)
    #Breaking loop and Calculating Average
    elif number == 'done':
        total = 0
        for num in numlist:
            total += num
        print(f"The average of numbers is {total/len(numlist)}")
        break
       
    
   
       




                