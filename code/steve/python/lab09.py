# Version 1

# distance = float(input('Please enter the distance in ft that you would like to convert: '))
# answer = distance * 0.3048
# print(f'{distance} is equal to {answer} meters.')

# Version 2 & 3

# unit = {
#     "ft": 0.3048,
#     "mi": 1609.34,
#     "m": 1,
#     "km": 1000,
#     "yd": 0.9144,
#     "in": 0.0254,
# }

# start_measuring_system = input("What is the beginning measurment type? Please enter ft, mi, m, km, yd, in: ")
# distance = float(input(f'Please enter the distance in {start_measuring_system} that you would like to convert: '))
# answer = distance * unit[start_measuring_system]
# print(f'{distance} {start_measuring_system} equals {answer} meters')


# Version 4



def conversion(beg_unit, number_distance, last_unit):
    '''
    This defines the conversion dictionary and returns the answer
    '''
    converted_unit = {
        'ft': 0.3048, 
        'mi': 1609.34,
        'm': 1,
        'km': 1000
    }
    to_meters = number_distance * converted_unit[beg_unit]
    answer = to_meters / converted_unit[last_unit]
    return answer

def distance():
    '''
    This defines the user input distance
    '''
    number_distance = int(input("Please enter the distance you want converted: "))
    return number_distance

def start_unit():
    '''
    This defines the user input unit
    '''
    beg_unit = input("please enter the beginning unit. i.e. ft, mi, m, km: ")
    return beg_unit

def end_unit():
    '''
    defining the end unit
    '''
    last_unit = input("please enter the ending unit. i.e. ft, mi, m, km: ")
    return last_unit


def main():
    '''
    Define main function

    '''
    beg_unit = start_unit()
    number_distance = distance()
    last_unit = end_unit()
    answer = conversion(beg_unit, number_distance, last_unit)

    print(f"You total distance is {answer}{last_unit}")

main()