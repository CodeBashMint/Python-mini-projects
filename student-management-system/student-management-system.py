students = []

while True:
    print("---------Students Management Program---------")
    print("1. Add student")
    print("2. Show all students")
    print("3. Search student by name")
    print("4. Update student")
    print("5. Remove student")
    print("6. Exit")

    choice = input("Enter a choice: ")

    if choice == '1':
        name = input("Enter student name: ")
        age = input("Enter student age: ")
        city = input("Enter student city: ")

        student = {
            "name": name,
            "age": age,
            "city": city
        }
        students.append(student)
        print("Student added successfully!")

    elif choice == '2':
        if len(students) == 0:
            print("No students found.")
        else:
            for s in students:
                print(f"Name: {s['name']}, Age: {s['age']}, City: {s['city']}")

    elif choice == '3':
        search_name = input("Enter name to search: ")
        found = False
        for s in students:
            if s["name"].lower() == search_name.lower():
                print(f"Found: Name: {s['name']}, Age: {s['age']}, City: {s['city']}")
                found = True
                break
        if not found:
            print("Student not found.")

    elif choice == '4':
        update_name = input("Enter name to update: ")
        found = False
        for s in students:
            if s["name"].lower() == update_name.lower():
                new_age = input("Enter new age: ")
                new_city = input("Enter new city: ")
                s["age"] = new_age
                s["city"] = new_city
                print("Student updated successfully.")
                found = True
                break
        if not found:
            print("Student not found.")

    elif choice == '5':
        remove_name = input("Enter name to remove: ")
        found = False
        for s in students:
            if s["name"].lower() == remove_name.lower():
                students.remove(s)
                print("Student removed successfully.")
                found = True
                break
        if not found:
            print("Student not found.")

    elif choice == '6':
        print("Exiting... Goodbye!")
        break

    else:
        print("Invalid choice. Try again!")

