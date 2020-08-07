

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

def create(user_list):
    current_list = user_list

    used_names = []
    for x in current_list:
        used_names.append(x['name'])


    new_user = input("Enter name: ")

    if new_user not in used_names:
        
        new_phone = input("Enter phone number: ")
        new_address = input("Enter address: ")
        new_genre = input("Enter movie genre: ")
        new_rating = input("Enter rating: ")
    
    else:
        print('Name already used.')
        return
        
    current_list.append({'name': new_user,
                        'phone': new_phone,
                      'address': new_address,
                  'movie genre': new_genre,
                       'rating': new_rating      
                        })  

    
    return current_list

# name,phone,address,movie genre,rating
        






def fetch_record(look_up):
    
    current_list = look_up
    used_names = []
    for x in current_list:
        used_names.append(x['name'])

    s_name = input('Enter the name to look up: ')
    
    if s_name not in used_names:
        print('Not in contact list')
    
    else:
        print(current_list[used_names.index(s_name)])

        input('\n\nPress enter to continue')

   

def update_record(user_list):
    current_list = user_list
    used_names = []
    for x in current_list:
        used_names.append(x['name'])


    new_user = input("Enter name of record to change: ")

    if new_user in used_names:
        
        new_phone = input("Enter phone number: ")
        new_address = input("Enter address: ")
        new_genre = input("Enter movie genre: ")
        new_rating = input("Enter rating: ")
    
    else:
        print('Name not in database.')

        return
        
    current_list[used_names.index(new_user)].update({
                                    'phone': new_phone,
                                  'address': new_address,
                              'movie genre': new_genre,
                                   'rating': new_rating      
                                    })  

    
    return current_list




def delete_record(user_list):
    current_list = user_list
    used_names = []
    for x in current_list:
        used_names.append(x['name'])

    new_user = input("Enter name of record to delete: ")

    if new_user in used_names:
        print(current_list[used_names.index(new_user)])

        sure = input('Are you sure you want to delete?\n...(y/n) ')
        while sure not in 'yn':
            sure = input('Are you sure you want to delete?\n...(y/n) ')

        if sure == "y":
            del current_list[used_names.index(new_user)]
            print('Record Deleted!')
            return current_list
        else:
            return current_list
        


def exit(current_list, headers):
    
    output = ""
    output += ",".join(headers) + "\n"

    for i in range(len(current_list)):
        if i != len(current_list) - 1:
            output += ",".join(list(current_list[i].values())) + "\n"
        else:
            output += ",".join(list(current_list[i].values()))

    with open("contacts.csv", "w") as file:
        file.write(output)    


# Implement a CRUD REPL

# Create a record: ask the user for each attribute, add a new contact to your contact list 
# with the attributes that the user entered.

# Retrieve a record: ask the user for the contact's name, find the user with the given name, 
# and display their information
# Update a record: ask the user for the contact's name, then for which attribute of the user 
# they'd like to update and the value of the attribute they'd like to set.
# Delete a record: ask the user for the contact's name, remove the contact with the given 
# name from the contact list.

def address_book():
    
    user_list, headers = get_contacts()
    
    print("Contact list")


    while True:

        menu = input(f'''
Please select an option:

1) Create new entry
2) Retrieve records
3) Update record
4) Delete record  
5) Exit  
''').replace(' ',"")

        if not menu.isdigit():
            print('Invalid option. Enter the number only')

        elif menu == '1':
            user_list = create(user_list)
        
        elif menu == '2':
            fetch_record(user_list)
        
        elif menu == '3':
            user_list = update_record(user_list)
        
        elif menu == '4':
            user_list = delete_record(user_list)

        elif menu == '5':
            exit(user_list,headers)
            
            break

        else:
            print('Invalid Selection')


    
    
    pass








if __name__ == "__main__":
    address_book()