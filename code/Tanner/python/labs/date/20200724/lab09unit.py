def converter():
    units = {
        #feet to meters
        'ft': .3048,
        #km to meters
        "km": 1000,
        #miles to meters
        "mi": 1609,
        #yards to meters
        "yd": .9144,
        #inch to meters
        "in": .0254
    }
    mixit = input("first unit of measurement?: ")

    print('you chose: ', mixit)

    #mix2it = input("what is unit of measurement being converted to?: ")

    d1 = float(input("what is the distance?: "))

    conversion = d1 * units.get(mixit)

    print("your converted distance is: ", conversion, 'meters')

converter()