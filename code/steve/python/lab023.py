

def get_contacts():
    with open("contacts.csv") as file:
        data = file.read().split('\n')
    
    headers = data[0]
    headers = headers.split(',')
    data = data[1:]

    contact_data = []
    for contact in data:
        contact_data.append(contact.split(","))

    contacts = []
    for contact in contact_data:
        current_contact = {}
        for i in range(len(headers)):
            current_contact[headers[i]] = contact[i]
        contacts.append(current_contact)
        
    
    return contacts, headers

        
def get_records():
    name = input('What is your name?: ')
    phone = input('What is your phone number?: ')
    address = input('What is your address?: ')
    movie_genre = input('What is your favorite movie genre?: ')
    rating = input('Are you hot or not? 1-10: ')

    new_user = f'{name},{phone},{address},{movie_genre},{rating}'
    
    return new_user

def add_record(contacts, new_user, headers):
    
    contact_data = new_user.split(",")

    current_contact = {}
    for i in range(len(headers)):
        current_contact[headers[i]] = contact_data[i]
    contacts.append(current_contact)
    
    return contacts


def retrieve_contact(headers, contacts): # Not done
    name = input('Please select a contact name to lookup: ')
    for key in contacts:
        if key.value == name:
            print()
    


def update_contact(headers, contacts, new_user): # Not done
    pass

def delete_contact(headers, contacts): # Not done
    pass

def menu():

    print("Welcome to the Contact manager!")
    while True:
        menu_display = """
        1) Add a contact
        2) Change a contact
        3) Lookup a contact
        4) Delete a contact
        """
        choice = input(menu_display)
        return choice

def main():
    contacts, headers = get_contacts()
    while True:
        menu_display = """
        1) Add a contact
        2) Change a contact
        3) Lookup a contact
        4) Delete a contact
        5) Quit
        """
        choice = input(menu_display)


        if choice == "1":
            new_user = get_records()
            contacts = add_record(contacts, new_user, headers) 
            print(contacts)      
        elif choice == "2":
            print('Please select a contact to update: ')
            new_user = get_records()
            update_contact(headers, contacts, new_user)
        elif choice == "3":
            
            retrieve_contact(contacts, headers)
        elif choice == "4":
            print('Please select a contact name to delete: ')
            delete_contact(contacts, headers)
        elif choice == "5":
            print('Goodbye')
            break
        else:
            print("Invalid choice.")


main()