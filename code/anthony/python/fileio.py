

with open("stuff.txt", "r") as file:
    contents = file.read()
    contents = contents.split(",")
    print(contents)


while True:
    new_item = input("Enter a new item: ")
    if new_item == "done":
        break
    else:
        contents.append(new_item)


output = ""
for i in range(len(contents)):
    if i != len(contents) - 1:
        output += contents[i] + ","
    else:
        output += contents[i]



with open("things.txt", "a") as file:
    file.write(output)