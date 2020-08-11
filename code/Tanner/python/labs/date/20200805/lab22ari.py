def read(file_name):
    with open(file_name) as cows:
        text = cows.read().lower()
    return text


print(read("how_to_select_cows.txt"))