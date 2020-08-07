

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
        

    return contacts

        

get_contacts()