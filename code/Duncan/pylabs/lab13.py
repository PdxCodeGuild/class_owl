# rot cypher
import string


alphabet = string.ascii_lowercase + string.ascii_uppercase + string.punctuation + string.digits
# promt user for string
message = input("Enter a message to be encrypted")
rotation = int(input("Enter the crypt amount: "))
#encrypt string
encrypted_message = ""
for x in message:
    if x != " ":
        index = alphabet.find(x)
        index = (index + rotation) % len(alphabet)
        encrypted_message += alphabet[index]
    else:
        encrypted_message += " "

# display encrypted string
print(encrypted_message)

# decoding
message = ""
for x in encrypted_message:
    if x != " ":
        index = alphabet.find(x)
        index = (index - rotation) % len(alphabet)
        message += alphabet[index]
    else: 
        message += " "
print(message)

