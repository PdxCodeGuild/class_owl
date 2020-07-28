
# Function that converts to meters

def unit_converter(type, value):
    # Dictionary of units

    unit_dict_TO_METERS = {'feet': 0.3048, 'miles': 1609.34, 'kilometers' : 1000, 'yards': 0.9144 , 'inches': 0.0254}
    meter_conv = unit_dict_TO_METERS[type] * value

    return meter_conv

def main():
    ft_dict = {'feet': 0.3048, 'miles': 1/5280, 'kilometers' : 1, 'yards': 1/3, 'inches': 12}

    print('Welcome to the unit converter')
    user_type = input("Please enter the unit you wish to convert to meters:(feet, miles, kilometers, yards, inches): ").lower()
    
    while user_type not in ft_dict:
         user_type = input("Please enter the UNIT you wish to convert to meters:(feet, miles, kilometers, yards, inches): ").lower()

    user_digits = input('Thanks! Now please enter the value: ')
    is_int = 1
    while not user_digits.isdigit():
        if user_digits.replace('.',"").isdigit():
            is_int = 0
            break
        user_digits = input('Thanks! Now please enter the value: ')

    user_digits = int(user_digits) if is_int == 1 else float(user_digits)
    converted = unit_converter(user_type, user_digits)

    print(f"{user_digits} {user_type} converted to meters is {round(converted,2)} m.")








if __name__ == "__main__":
    main()