# Now we'll ask the user for the distance, 
# the starting units, and the units to convert to.

def unit_converter(type_from,type_to, value):
    unit_dict_TO_METERS = {'feet': 0.3048, 'miles': 1609.34, 'kilometers' : 1000, 'yards': 0.9144 , 'inches': 0.0254, 'meters': 1}

    meter_conv = unit_dict_TO_METERS[type_from] * value
    
    full_conv = meter_conv * (1/unit_dict_TO_METERS[type_to])

    return full_conv

def unit_choice(message):
    while True:
        choice_dict = ['feet','miles', 'kilometers', 'yards', 'inches','meters']
        print('\nSelect one of the following')
        print(choice_dict)
        user_type = input(message).lower()
        if user_type in choice_dict:
            return user_type

def main():
    
    print('Welcome to the unit converter')
    user_type_from = unit_choice('Select the type of unit to convert from: ')
    
    user_type_to = unit_choice('Select the type of unit to convert to: ' )


    user_digits = input('Thanks! Now please enter the value: ')
    is_int = 1
    while not user_digits.isdigit():
        if user_digits.replace('.',"").isdigit():
            is_int = 0
            break
        user_digits = input('Thanks! Now please enter the value: ')

    user_digits = int(user_digits) if is_int == 1 else float(user_digits)
    converted = unit_converter(user_type_from,user_type_to, user_digits)

    print(f"{user_digits} {user_type_from} converted to {user_type_to} is {round(converted,2)} {user_type_to}.")








if __name__ == "__main__":
    main()