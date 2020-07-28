

# Problem 1
# Write a function that tells whether a number is even or odd (hint, compare a/2 and a//2, or use a%2)
def is_even2(num):
    if num % 2 == 1:
        return False
    else:
        return True

def is_even(num):
    return False if num % 2 else True


# print(is_even(4))
# print(is_even(5))
# print(is_even(0))
# print(is_even(-6))


# Problem 2
# Write a function that takes two ints, a and b, and returns True if one is positive and the other is negative.
def opposite2(a, b):
    if a > 0 and b < 0:
        return True
    elif b > 0 and a < 0:
        return True
    else:
        return False

def opposite3(a, b):
    if (a > 0 and b < 0) or (b > 0 and a < 0):
        return True
    else:
        return False

def opposite(a, b):
    return (a > 0 and b < 0) or (b > 0 and a < 0)


# print(opposite(10, -1)) # True
# print(opposite(2, 3)) # False
# print(opposite(-1, -1)) # False
# print(opposite(-1, 4)) # True


# Problem 3
# Write a function that returns True if a number within 10 of 100.

def near_100b(num):
    if num >= 90 and num <= 110:
        return True
    else:
        return False

def near_100(num):
    return num >= 90 and num <= 110


# print(near_100(50)) # False
# print(near_100(99)) # True
# print(near_100(105)) # True

# Problem 4
# Write a function that returns the maximum of 3 parameters.

def maximum_of_three2(a, b, c):
    z = max(a, b, c)
    return z

def maximum_of_three3(a, b, c):
    if a > b:
        if a > c:
            return a
        else:
            return c
    elif b > c:
        return b
    else:
        return c

def maximum_of_three4(a, b, c):
    z = [a, b, c]
    z.sort()
    return z[-1]

def maximum_of_three(a, b, c):
    z = [a, b, c]
    max = a
    for num in z:
        if num > max:
            max = num
    return max

print(maximum_of_three(5,6,2)) # 6
print(maximum_of_three(-4,3,10)) # 10
