# contacts list 

# existing contacts list 
def get_contacts():
    with open("contacts.csv") as file:
        data = file.read().split("\n")


    headers = data[0]
    headers = headers.split(",")
    data = data[1:]

    contact_data = []
    for contacts in data:
        contact_data.append(contacts.split(","))

    contacts = []
    for contacts in contact_data:
        current_contact = {}
        for i in range(len(headers)):
            current_contact[headers[i]] = contacts[i]
        contacts.append(current_contact)

    return contacts, headers    

    


    


# CRUD to add contacts



def add_contact(contacts):
    
    
    existing_contacts = []
    for x in contacts:
        existing_contacts.append(x["name"])

    new_contact = input("Enter the name of your new contact: ")

    if new_contact not in existing_contacts:
        new_phone = input("Enter thier phone number: ")    
        new_address = input("Enter thier address: ")
        new_movie = input("Enter thier favorite movie genre: ")
        new_rating = input("Enter their rating: ")
    else:
        print("Name already in contacts.")
        return

    contacts.append({"name": new_contact,
                    "phone": new_phone,
                    "adress": new_address,
                    "movie genre": new_movie,
                    "rating": new_rating
                    })

    return contacts


    def update_contacts():
        existing_contacts = []
        for x in contacts:
            existing_contacts.append(x["name"])
        pass    

    # output = ""
    # output += ",".join(headers) + "\n"

    # for i in range(len(contacts)):
    #     if i != len(contacts) - 1:
    #         output += ",".join(list(contacts[i].values())) + "\n"
    #     else:
    #         output += ",".join(list(contacts[i].values()))

    # with open("contacts.csv", "w") as file:
    #     file.write(output)

# menu to choose view contacts or update contacts

def menu():
    print("""What would you like to do?:
    1) view contacts list.
    2) Create contacts.
    3) Update contacts.
    4) Exit. """)
    choice = input(">")
    return choice.lower()


# main program
def main():
    print("welcome to your contacts list.")

    while True:
        contacts, headers = get_contacts()
        choice = menu()
        
        if choice == "1" or choice == "View contacts list".lower():
            get_contacts()
            print(contacts)
        
        elif choice == "2" or choice == "Create contacts".lower():
            add_contact(contacts)
            print(contacts)

        elif choice == "3" or choice == "Update contacts".lower():
            pass

        
        elif choice == "4" or choice == "Exit".lower():
            break

        else:
            print(f"invalid choice {choice}.")
        add_contact(contacts, headers)  

main()          



