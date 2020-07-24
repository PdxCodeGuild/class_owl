
# Global variable
some_thing = "This is a global variable"

def pretty_print(my_list: list):
    """
        Takes a list, prints each item one at a time.
    """
    
    if type(my_list) != list:
        return "Can not print that"
    for item in my_list:
        print(item)

    return "printed successfully"


def pow(num, power):
    return (num ** power)


def main():
    car_makes = ["bmw", "gmc", "porche", "kia", "subaru", "nissan", "honda", "ford"]

    # result = pretty_print("car_makes")

    number = int(input("Enter a number: "))
    power = int(input("Raised to what power: "))

    new_number = pow(number, power)
    print(new_number)

main()