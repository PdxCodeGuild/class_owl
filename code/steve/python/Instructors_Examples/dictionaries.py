cereals = {
    "twinkie": 3.98,
    "Twinkie": 2.49,
    "lucky charms": 4.59,
    "oreo": 7.00,
    "honey smacks": 4.00,
    "fruit lops": 1.99
}


# print(cereals["moon pies"])
# cereals["moon pies"] = 6.00


# print(cereals.get("twinkie", False))

# if "Twinkie" in cereals:
#     print("We have that in stock")
# if "fruit loops" not in cereals:
#     print("That cereal is not in stock, sorry.")


# choice = input("Choose a cereal: ")

# if choice in cereals:
#     price = cereals.get(choice)
#     print(f"{choice} is priced at {price}")
# else:
#     print(f"{choice} not found.")
#     should_add = input("Would you like to add it? ")
    
#     if should_add in ["yes", "y", "yeah", "sure"]:
#         cereals[choice] = input(f"Enter the price for {choice}: ")
#         print(cereals)


# for key in cereals:
#     # print(key)
#     # print(cereals[key])
#     print(f"{key}: {cereals[key]}")

# print(cereals.keys())
# print(cereals.values())
# print(cereals.items())

for key, value in cereals.items():
    print(key, value)