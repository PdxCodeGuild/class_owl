

def get_contacts():
    with open("contacts.csv") as contacts:
        data = contacts.read().split('\n')

    headers = data[0]
    headers = headers.split(',')
    data = data[1:]

    contact_data ={}
    for contact in data:
        contact.data.append(contact.split(","))
   
    contacts =[]
    for contact in contact_data
        current_contact ={}
        for i in range(len(headers)):
            current_contact[headers[i]] = contact[i]
        contacts.append(current_contact)

    return contacts

def create_contact():
    pass

def retrieve_contact():
    pass

def update_contact():
    pass

def delete_contact():
    pass

def menu():
    pass

def main():
    pass