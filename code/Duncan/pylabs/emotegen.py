# lab 5 emoticon generator
import random

eyes = [":",";",".","^",]
nose = ["c","<","B",]
mouth = [")","/","|","(",">",]

face = random.choice(eyes) + random.choice(nose) + random.choice(mouth)
print(f"{face}")