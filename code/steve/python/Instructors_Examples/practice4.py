# Problem 1
# Given a the two lists below, combine them into a dictionary.

def combine(a, b):
    # c = {}

    # for i in range(len(a)):
    #     c.update({a[i]: b[i]})

    # return c
    return {a[i]:b[i] for i in range(len(a))}


fruits = ['apple', 'banana', 'pear']
prices = [1.2, 3.3, 2.1]
# print(combine(fruits, prices)) # {'apple':1.2, 'banana':3.3, 'pear':2.1}


# Problem 2
# Using the result from the previous problem, iterate through the dictionary and calculate the average price of an item.

def average(d):
    return round(sum(d.values()) / len(d), 1)
    

combined = {'apple':1.2, 'banana':3.3, 'pear':2.1}
# print(average(combined)) # 2.2

# Problem 3
# Average numbers whose keys start with the same letter. Output a dictionary containing those letters as keys and the averages.
def unify(e):
    f = {}
    for key in e:
        char = key[0]
        if char not in f:
            f[char] = [e[key]]
        else:
            f[char].append(e[key])

    for key in f:
        f[key] = round(sum(f[key]) / len(f[key]))

    return f



d = {'a1':5, 'a2':2, 'a3':3, 'b1':10, 'b2':1, 'b3':1, 'c1':4, 'c2':5, 'c3':6, 'g1': 8}
# print(unify(d)) # {'a':3, 'b':4, 'c':5}

# Problem 3
# Write a dictionary comprehension to swap keys and values of a given dictionary. So {'a': 1, 'b': 2} would become {1: 'a', 2: 'b'}.

dict1 = {'a': 1, 'b': 2}
dict2 = {value: key for key, value in dict1.items()}
# print(dict2)

# Problem 4
# Write a dictionary comprehension to print each letter of the alphabet and its correstponding ASCII code (check out ord)

# {'a': 97, 'b': 98, 'c': 99, 'd': 100, 'e': 101, 'f': 102, 'g': 103, 'h': 104, ...}
from string import ascii_lowercase as lowercase
alpha_codes = {char: ord(char) for char in lowercase}
print(alpha_codes)