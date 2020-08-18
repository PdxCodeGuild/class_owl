import time


class Car:
    def __init__(self, color, doors, style):
        self.color = color
        self.doors = doors
        self.style = style
        self.fuel = 75

    def fill_tank(self):
        self.fuel = 100

    def use_fuel(self):
        if self.fuel > 0:
            self.fuel -= 2

    def __str__(self):
        return f"{self.color} {self.style}"



my_car = Car("green", 2, "truck")
your_car = Car("purple", 4, "suv")
# print(my_car.color)
# print(my_car.doors)
# print(my_car.style)

# print(your_car.color)
# print(your_car.doors)
# print(your_car.style)

# while True:
#     time.sleep(.5)
#     my_car.use_fuel()
#     if my_car.fuel < 25:
#         my_car.fill_tank()

#     print(my_car.fuel)

# print(my_car)
# print(your_car)


class Person:

    def __init__(self, f_name, l_name, hair_color, eye_color, age):
        self.f_name = f_name
        self.l_name = l_name
        self.hair_color = hair_color
        self.eye_color = eye_color
        self.age = age
        self.is_married = False

    def birthday(self):
        self.age += 1

    def get_married(self):
        self.is_married = True

    def get_divorced(self):
        if self.is_married:
            self.is_married = False

    def fake_age(self, new_age):
        self.age = new_age

    def __str__(self):
        return f"""first name: {self.f_name}
    last name: {self.l_name}
    age: {self.age}
    married: {self.is_married}
    """


# first = input("Enter your first name: ")
# last = input("Enter your last name: ")
# hair = input("Enter your hair color: ")
# eye = input("Enter your eye color: ")
# age = input("Enter your age: ")

person1 = Person("Cindy", "Peterson", "Red", "Green", 28)

# person2 = Person(first, last, hair, eye, age)

print(person1)

person1.get_married()

person1.fake_age(22)

print(person1)


person1.get_divorced()

print(person1)