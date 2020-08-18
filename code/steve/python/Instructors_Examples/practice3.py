import random
import string
from typing import Collection

# Problem 1
# Write a function using random.randint to generate an index, use that index to pick a random element of a list and return it.

def random_element(a):
    # return a[random.randint(0, len(a) - 1)]

    index = random.randint(0, len(a) - 1)
    element = a[index]
    return element

fruits = ['apples', 'bananas', 'pears']
# print(random_element(fruits))


# Problem 2
# Write a REPL which asks users for a list of numbers, which they enter, until they say 'done'. Then print out the list.

def get_numbers():
    numbers = []

    num = input("Enter a number or 'done': ")
    while num.isdigit():
        num = int(num)
        numbers.append(num)
        num = input("Enter a number or 'done': ")

    print(numbers)

def get_numbers_adv():
    hot_mess = input("Enter some numbers, press 'enter' when done: ")
    for char in hot_mess:
        if char in string.punctuation:
            hot_mess = hot_mess.replace(char, " ")
    mess = hot_mess.split()

    clean_nums = [int(element) for element in mess if element.isdigit()]
    print(clean_nums)

# get_numbers_adv()

# Problem 3
# Write a function that takes a list of numbers, and returns True if there is an even number of even numbers.

def even_even_old(numbers):

    count = 0
    for num in numbers:
        if num % 2 == 0:
            count += 1

        # if not num % 2:
        #     count += 1

        # if num % 2:
        #     continue
        # else:
        #     count += 1

    return not count % 2

def even_even(numbers):
    # even_numbers = [num for num in numbers if not num % 2]
    # return not len(even_numbers) % 2
    return not len([num for num in numbers if not num % 2]) % 2


# print(even_even([2, 3, 4, 5, 6, 7, 8]))
# print(even_even([0, 9, 8, 7, 6]))

# Problem 4
# Print out every other element of a list, first using a while loop, then using a for loop.

def every_other(stuff):

    count = 0
    length = len(stuff)
    while count < length:
        print(stuff[count])
        count += 2

    for i in range(0, length, 2):
        print(stuff[i])


# every_other(["A", "B", "C", "D", "E"])

# Problem 5
# Write a function that returns the reverse of a list.

def reverse(things):
    reversed_list = [things[i] for i in range(len(things) -1, -1, -1)]

    # return things[::-1]
    return reversed_list

# print(reverse(["A", "B", "C", "D", "E"]))

# Problem 6
# Write a function to move all the elements of a list with value less than 10 to a new list and return it.

def extract_less_than_ten(nums):
    less_than_ten = [num for num in nums if num < 10]
    # for num in nums:
    #     if num < 10:
    #         less_than_ten.append(num)

    return less_than_ten


numbers = list(range(0,20))
random.shuffle(numbers)

# print(extract_less_than_ten(numbers))

# Problem 9
# Given a list of numbers, and a target number, find a pair of numbers from the list that sum to a target number

def find_pairs(numbers, target):

    pairs = []
    # for i in range(len(numbers)):
    #     sublist = numbers[i:]
    #     for num in sublist:
    #         if numbers[i] + num == target:
    #             pairs.append([numbers[i], num])

    # pairs = [[numbers[i], num] for i in range(len(numbers)) for num in numbers[i:] if numbers[i] + num == target]

    # for i, number in enumerate(numbers[:-1]):  # note 1
    #     complementary = target - number
    #     if complementary in numbers[i+1:]:  # note 2
    #         pairs.append([number, complementary])

    for i in range(len(numbers)):
        complementary = target - numbers[i]
        sublist = numbers[i:]
        if complementary in sublist:
            pairs.append([numbers[i], complementary])

    return pairs

print(find_pairs([1, 2, 3, 5, 6, 4], 7))


stuff = ["A", "B", "C", "D", "E"]

# for i, thing in enumerate(stuff):
#     print(i, thing)