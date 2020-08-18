import string

apple_bottom = "Shawty had them Apple Bottom Jeans (jeans) Boots\
with the fur (with the fur) The whole club was lookin' at her\
She hit the floor (she hit the floor)"

apple_bottom_len = len(apple_bottom)

# print(apple_bottom[68:len(apple_bottom)])

# apple = apple_bottom[3:50]
# print(apple)

start = apple_bottom.find("the")
# print(apple_bottom[start:len(apple_bottom):3])


apple_bottom_list = apple_bottom.split(" ")

apple_bottom_list = "🍎".join(apple_bottom_list)
# print(apple_bottom_list)


for char in apple_bottom:
    if char in string.punctuation:
        apple_bottom = apple_bottom.replace(char, "")

print(apple_bottom)