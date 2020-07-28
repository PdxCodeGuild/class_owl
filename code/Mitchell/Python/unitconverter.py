print("Eugene's UniBrow Ready Unit Converter")



def converter():
    units = {'foot': 0.3048, 'mile': 1609.34, 'meter': 1, 'kilometer': 1000, 'yard': 0.9144, 'inch': 0.0254}
    distance = input('what is the distance  ')
    while not distance.isdigit():
        print('\tWrite a Number')
        distance = input('what is the distance  ')
    distance = int(distance)
        
    
    u_from = input("What unit are you converting from ? Choose foot, mile, meter, kilometer, yard, inch  ")
    while u_from not in units:
        print("\tPlease write a listed option")
        u_from = input("What unit are you converting from ? Choose foot, mile, meter, kilometer, yard, inch  ")

    u_to = input("What unit are you converting to? Choose Foot Mile Meter Kilomenter Yard or Inch  ")
    while u_to not in units:
        print("\tPlease write a listed option")
        u_to = input("What unit are you converting to? Choose Foot Mile Meter Kilomenter Yard or Inch  ")

    result1 = distance / units[u_from] * units[u_to]
    print(result1)

step1 = converter()
     