units = {
"m": 1,
"mi": 1*1609.34,
"ft": 1*.3048,
"km": 1*1000,
"yd": 1*.9144,
"in": 1*.0254
}

def main():
    print ("Welcome to the Unit Converter")

    distance = int(input("What is the distance : "))
    while True:
        unit = input("What is the unit: mi, km, m ,ft, yd, in, in you want in meters? ").lower()
        
        if unit not in units:
            print('Not a valid choice')
            unit
        elif unit in units:
            calculation  = distance * units[unit]
            print (f'{distance} {unit} is {calculation} meters')
            break

main ()