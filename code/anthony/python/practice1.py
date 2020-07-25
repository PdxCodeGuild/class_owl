

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


print(opposite(10, -1)) # True
print(opposite(2, 3)) # False
print(opposite(-1, -1)) # False
print(opposite(-1, 4)) # True

