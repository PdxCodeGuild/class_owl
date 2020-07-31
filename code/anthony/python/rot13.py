import string

alphabet = string.ascii_lowercase + string.ascii_uppercase + string.punctuation + string.digits


# Prompt user for string
# message = input("Enter a message to be encrypted: ").lower()
message = input("Enter a message to be encrypted: ")
rotation = int(input("Enter they encryption amount: "))

# Encrypt string
encrypted_message = ''
for x in message:
    if x != " ":
        index = alphabet.find(x)
        index = (index + rotation) % len(alphabet)
        encrypted_message += alphabet[index]
    else:
        encrypted_message += " "

# Display encrypted string
print(encrypted_message)

message = ""
for x in encrypted_message:
    if x != " ":
        index = alphabet.find(x)
        index = (index - rotation) % len(alphabet)
        message += alphabet[index]
    else:
        message += " "
print(message)