import requests
import json

# data = requests.get("https://jsonplaceholder.typicode.com/users")

# data = data.text

# users = json.loads(data)

# new_users = {}
# for user in users:
#     new_users[user['username']] = {
#         'name': user['name'],
#         'email': user['email'],
#         'phone': user['phone']
#     }


# output = json.dumps(new_users)

# with open('users.txt', 'w') as file:
#     file.write(output)


# with open('users.txt') as file:
#     data = file.read()


# users = json.loads(data)
# for user in users:
#     print(user)


data = requests.get("https://aol.com").text

with open('aol.html', 'w') as file:
    file.write(data)