car_makes = ["bmw", "gmc", "porche", "kia", "subaru", "nissan", "honda", "ford"]

# print(car_makes[4::])
# print(car_makes[2:6:])
# print(car_makes[::2])
# print(car_makes[::-1])

index = car_makes.index("porche")
car = car_makes.pop(index)

print(car_makes)

print(car)