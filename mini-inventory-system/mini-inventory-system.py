# Learner Store - Mini Inventory System

My_Store = ["Computer", "Laptop", "Mouse", "Keyboard", "Hard disk", "USB", "USB"]

def search_item():
    item = input("Search an item: ").strip().title()
    count = My_Store.count(item)
    print(f"You have {count} '{item}' left in inventory.\n")

def sell_item():
    item = input("Enter item to sell: ").strip().title()
    if item in My_Store:
        My_Store.remove(item)
        print(f"'{item}' sold successfully.\n")
    else:
        print(f"'{item}' not found in inventory.\n")

def store_item():
    item = input("Enter item to store: ").strip().title()
    My_Store.insert(0, item)
    print(f"'{item}' added to inventory.\n")

def save_inventory():
    with open('store.txt', 'w') as file:
        for item in My_Store:
            file.write(item + '\n')
    print("Inventory saved to 'store.txt'.")

def show_menu():
    print("""
========= Learner Store =========
[f] Find item
[s] Sell item
[a] Add item
[e] Exit
=================================
""")

print("Welcome to Learner Store")

while True:
    show_menu()
    operation = input("Choose an operation: ").strip().lower()

    try:
        if operation == "f":
            search_item()
        elif operation == "s":
            sell_item()
        elif operation == "a":
            store_item()
        elif operation == "e":
            print("Exiting... Saving inventory.")
            save_inventory()
            break
        else:
            print("Invalid operation. Please try again.\n")
    except Exception as e:
        print("An error occurred:", str(e))

