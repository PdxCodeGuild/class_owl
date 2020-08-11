

def getC():
    with open("contacts.csv") as file:
        data = file.read().split('\n')

    headers = data[0]
    headers = headers.split(',')
    data = data[1:]
    
    contactD = []
    for contact in data:
        contactD.append(contact.split(","))
        
    contacts = []
    for contact in contactD:
        currentC = {}
        for i in range(len(headers)):
            currentC[headers[i]] = contact[i]
        contacts.append(currentC)
    
    return contacts

getC()
 
print(getC())