def missing_char(message):
    strings = []
    for i in range(len(message)):
        strings.append(message[:i] + message[i+1:])


    return strings

print(missing_char('kitten'))