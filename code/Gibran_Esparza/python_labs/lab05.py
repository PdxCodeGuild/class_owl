import random

eyes = [":","=",";","x"]
nose = [",","^"]
mouth = ["(",")","O"]

r_eyes = random.choice(eyes)
r_nose = random.choice(nose)
r_mouth = random.choice(mouth)

x = 0
while x < 5:
    print (r_eyes + r_nose + r_mouth)
    x += 1