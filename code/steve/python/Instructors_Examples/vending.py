"""
Vending Machine
REPL

"""



# Inventory
inventory = {
    "A1": {
        "product": "Red Vines",
        "price": 1.99,
        "quantity": 10 
    },"A2": {
        "product": "Fruit Lops",
        "price": .75,
        "quantity": 8 
    },"B1": {
        "product": "Milk",
        "price": 1.25,
        "quantity": 2 
    },"B2": {
        "product": "Chips",
        "price": 1.25,
        "quantity": 6 
    },"C1": {
        "product": "Beer",
        "price": 7.50,
        "quantity": 0 
    },
    "balance": 0
}


# Insert Money
def insert_money():
    current_balance = inventory["balance"]
    print(f"Current balance: {current_balance}")
    amount = input("Give me your money: ")
    while True:
        try:
            amount = float(amount)
            break
        except ValueError:
            print(f"Invalid input {amount}")
            amount = input("Enter a dollar amount")

    inventory["balance"] += amount
    print(f"Current balance: {inventory['balance']}")

# Make Selection (Menu)
def select():
    print("Key \t Item \t\t Price \t Quantity")
    for item in inventory:
        if item != "balance":
            print(f"{item}\t{inventory[item]['product']}\t\t{inventory[item]['price']}\t{inventory[item]['quantity']}")

    choice = input("Select one: ")
    selection = inventory.get(choice, False)
    if selection:
        if selection['quantity'] > 0:
            if inventory['balance'] > selection['price']:
                vend(choice)
            else:
                print(f"Insufficient funds, {inventory['balance']} remaining.")
        else:
            print(f"{selection['product']} is out of stock.")
    else:
        print("Invalid selection")


# Vend
def vend(key):
    inventory[key]['quantity'] -= 1
    inventory['balance'] -= inventory[key]['price']
    print(f"Dispencing {inventory[key]['product']}.")
    print(f"{inventory['balance']} remaining.")

# Give change
def give_change():
    print(f"Giving you {inventory['balance']}")
    inventory['balance'] = 0


# Restock
def restock():
    for item in inventory:
        if item != "balance":
            print("Key \t Item \t\t Price \t Quantity")
            print(f"{item}\t{inventory[item]['product']}\t\t{inventory[item]['price']}\t{inventory[item]['quantity']}")

            update = input("Does this need updating? ")
            if update == "no":
                continue
            else:
                quantity = input("Enter the updated quantity: ")
                while True:
                    try:
                        quantity = int(quantity)
                        break
                    except ValueError:
                        quantity = input("Enter the updated quantity: ")
                inventory[item]['quantity'] =  quantity


    

# Main
def main():
    print("Welcome to PDX Vending...")
    while True:
        menu_display = """
        1) Insert Money
        2) Make a Selection
        3) Coin Return
        """
        choice = input(menu_display)
        if choice == "1":
            insert_money()
        elif choice == "2":
            select()
        elif choice == "3":
            give_change()
        elif choice == "123":
            restock()
        else:
            print("Invalid choice.")



main()