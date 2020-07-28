



"""
This function creates the nums list 
"""
def makelist(nums):

    while True:
        num1 = input('Please enter a number to add to the list, enter done when finished adding numbers: ')
        if num1 == 'done':
            print('You have finished entering numbers.')
            break
        else:
            num1 = int(num1)
            nums.append(num1)
            
"""
This function grabs the  length of the nums list
"""
def getlength(nums):

    number1 = 0
    for i in range(len(nums)):
        number1 = number1 + 1
    print(f'The length of your list is {number1} numbers.')
    return number1

"""
This function counts the numbers in the list.
"""
def count(nums):
    listtotal = 0
    for num in nums:
        listtotal = listtotal + int(num)
    print(f'The total of your list is: {listtotal}')
    return listtotal


"""
This function handles all the mathmetical functions for the program
"""
def calc(listtotal, length):   
    averagenumber = listtotal / length
    return averagenumber

def main():
    nums = []   
    makelist(nums)
    length = getlength(nums)
    print('Here is your finished list: ')
    print(nums)
    listtotal = count(nums)
    print('The average number from your list is: ')
    print(calc(listtotal, length))
    


main()