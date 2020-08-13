

def get_contacts():
    with open('contacts1.csv') as file:
        data = file.read().split("\n")

    headers = data[0]
    headers = headers.split(",")
    data = data[1:]

    contactdata = []
    for contact in data:

        contactdata.append(contact.split(','))
    
    contacts = []
    for contact in contactdata:
        current_contact = {}
        for i in range(len(headers)):
                current_contact[headers[i]] = contact[i]
        contacts.append(current_contact) 

            

    return contacts, headers


def create_contact(all_contacts):
    print("\n\n\t Lets Create a New Contact!")
    contact_name = input("\n\n\t\t Write in the Contacts Name:   ")

    contactnames = []
    for x in all_contacts:
        contactnames.append(x['name'])
    
    while contact_name in contactnames:
        print("contact exists")
        name = input("\n\n\t\t Write in the Contacts Name:   ")   
    
    contact_number = input("\n\n\t\t Write in the Contacts Phone:   ")
    contact_address = input("\n\n\t\t Write in the Contacts Address:   ")
    contact_genre = input("\n\n\t\t Write in the Contacts Fav Genre:   ")
    contact_ranking = input("\n\n\t\t Write in the Contacts Friend Rank:   ")

    all_contacts.append({
            "name": contact_name,
            "number": contact_number,
            "address": contact_address,
            "genre": contact_genre,
            "ranking": contact_ranking,
        })

    print("\n\n\t\t Contact added!")
    print(all_contacts)
    return all_contacts

def retrieve_contact(contacts):
    print(contacts)
    print("\n\n\t Lets Search for a Contact!")
    search_name = input("\n\n\t\t Write the Contact\'s name you are searching for:   ")


    for contact in contacts:
        if contact['name'] == search_name:
            print(contact)
            break
    else:
        print("\n\n\t\tContact Does Not Exist")
        search_name = input("\n\n\t\t Write the Contact\'s name you are searching for:   ")  
    



def menu():
    '''Reusable menu'''

    print("""Choose one of the following: 
    1) Contacts
    2) Add a Contact
    3) Search for a Contact
    4) Exit""")
    choice = input(">")
    return choice.lower()

def main():
    print("Welcome to Copamine's Contact Repository")

    # while True loop to keep the program running
    while True:
        contacts, headers = get_contacts()
        choice = menu()

        # Check to see what the user entered and call the appropriate function
        if choice == "1" or choice == "Contacts":
            get_contacts(contacts)
        elif choice == "2" or choice == "Add a Contact":
            create_contact(contacts)
        elif choice == "3" or choice == "Search for a Contact":
            retrieve_contact(contacts)
        elif choice == "4" or choice == "exit":
            break
        else:
            print(f"Invalid choice: {choice}.")

main()