

def get_users():
    with open("users.csv") as file:
        text = file.read().split('\n')
    
    #text = text.split('/n')
    headers = text[0]
    headers = headers.split(",")
    data = text[1:]
    
    user_data = []
    for user in data:
        user_data.append(user.split(','))
    users = []
    for user in user_data:
        current_user = {}
        for i in range(len(headers)):
            current_user[headers]


            
                
         


get_users()
