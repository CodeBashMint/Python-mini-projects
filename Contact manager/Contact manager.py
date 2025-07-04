all_contacts = {}

while True:
    print("\n--- Contact Manager ---")
    print("1. Add a contact")
    print("2. Show all contacts")
    print("3. Search contact by name")
    print("4. Update contact")
    print("5. Delete contact")
    print("6. Exit")

    try:
        user_input = int(input("Enter your choice (1-6): "))
        
        if user_input == 1:
            name = input("Enter full name: ").strip()
            phone = input("Enter phone number: ").strip()
            email = input("Enter email address: ").strip()
            all_contacts[name] = [phone, email]
            print(f"Contact '{name}' has been added successfully.")

        elif user_input == 2:
            if all_contacts:
                print("\nAll Contacts:")
                for name, info in all_contacts.items():
                    print(f"- Name: {name}, Phone: {info[0]}, Email: {info[1]}")
            else:
                print("No contacts found.")

        elif user_input == 3:
            name = input("Enter the name to search: ").strip()
            if name in all_contacts:
                phone, email = all_contacts[name]
                print(f"Name: {name}, Phone: {phone}, Email: {email}")
            else:
                print(f"No contact found with the name '{name}'.")

        elif user_input == 4:
            name = input("Enter the name to update: ").strip()
            if name in all_contacts:
                phone = input("Enter new phone number: ").strip()
                email = input("Enter new email address: ").strip()
                all_contacts[name] = [phone, email]
                print(f"Contact '{name}' has been updated.")
            else:
                print(f"No contact found with the name '{name}'.")

        elif user_input == 5:
            name = input("Enter the name to delete: ").strip()
            if name in all_contacts:
                del all_contacts[name]
                print(f"Contact '{name}' has been deleted.")
            else:
                print(f"No contact found with the name '{name}'.")

        elif user_input == 6:
            print("Exiting Contact Manager. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

    except ValueError:
        print("Invalid input. Please enter a valid number.")
