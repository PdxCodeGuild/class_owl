# Problem 1
# Get a string from the user, print out another string, doubling every letter.

def double_letter(single_string):
    doubled_string = ""
    for x in single_string:
        doubled_string += x*2

    return doubled_string

# print(double_letter("hello"))
# print(double_letter("goodbye"))

# Problem 2
# Write a function that takes a string, and returns a list of strings, each missing a different character.

def missing_char(string):
    missing_list = []

    for x in range(len(string)):
        subset = string[:x] + string[x+1:]
        missing_list.append(subset)

    return missing_list


# print(missing_char("kitten"))
# print(missing_char("python is fun"))

# Problem 3
# Return the letter that appears the latest in the english alphabet.
def latest_letter2(string):
    last_character = sorted(string)
    return last_character[-1]

def latest_letter3(string):
    last_character = string[0]
    for char in string:
        if char > last_character:
            last_character = char

    return last_character

def latest_letter(string):
    working_list = list(string)

    while True:
        sorted = False
        for i in range(len(working_list) -1):
            if working_list[i] > working_list[i+1]:
                # Use a temp variable to aid in swaping characters
                # temp = working_list[i]
                # working_list[i] = working_list[i + 1]
                # working_list[i + 1] = temp

                # Use tuple packing/unpacking to swap characters
                working_list[i], working_list[i + 1] = working_list[i + 1], working_list[i]
                sorted = True
        if not sorted:
            break
    return working_list[-1]




# print(latest_letter("ksihcosigefuijskdzlcml"))


# Problem 4
# Write a function that returns the number of occurances of 'hi' in a given string.

def count_hi2(string):
    return string.count("hi")

def count_hi(string):

    count = 0
    for x in range(len(string)):
        if "hi" in string[x:x+2]:
            count += 1

    return count

# print(count_hi("hihihihi"))
# print(count_hi("hellohisomethinghi"))

# Problem 5
# Write a function that returns True if a given string contains the same number of 'cat' as it does 'dog'

def count_phrase(string, phrase):
    count = 0
    for x in range(len(string)):
        if phrase in string[x:x+len(phrase)]:
            count += 1

    return count

def cat_dog(string):
    cats = count_phrase(string, "cat")
    dogs = count_phrase(string, "dog")
    return cats == dogs

# print(cat_dog('catdog')) # True
# print(cat_dog('catcat')) # False
# print(cat_dog('catdogcatdog')) # True

# Problem 6
# Return the number of letter occurances in a string.

# print(count_phrase('antidisestablishmentterianism', 'i'))
# print(count_phrase('pneumonoultramicroscopicsilicovolcanoconiosis','p'))

# Problem 7
# Convert input strings to lowercase without any surrounding whitespace.
def lower_case2(string):
    string = string.lower()
    string = string.strip()
    return string

def lower_case(string):
    return string.lower().strip()

print(lower_case("SUPER!"))
print(lower_case("        NANNANANANA BATMAN        "))