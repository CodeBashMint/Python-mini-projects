Books = [
    {"Title": "Harry Potter", "Author": "Rolling", "year": "2000"},
    {"Title": "Successful Stories", "Author": "Khan", "year": "2019"},
    {"Title": "Code Complete", "Author": "Ibne Sina", "year": "1900"}
]

while True:
    print("\n--- Book Management System ---")
    print("1. Add a book")
    print("2. Show all books")
    print("3. Search for a book by title")
    print("4. Delete a book")
    print("5. Exit")

    inputusr = input("Enter a number: ")

    if inputusr == '1':
        title_book = input("Enter the title: ")
        author_book = input("Enter the author: ")
        year_book = input("Enter the year: ")

        new_book = {
            "Title": title_book,
            "Author": author_book,
            "year": year_book
        }
        Books.append(new_book)
        print("Book added!")

    elif inputusr == '2':
        if len(Books) == 0:
            print("No books found.")
        else:
            for book in Books:
                print(f"Title: {book['Title']}, Author: {book['Author']}, Year: {book['year']}")

    elif inputusr == '3':
        show_book = input("Enter title to find: ")
        found = False
        for book in Books:
            if book["Title"].lower() == show_book.lower():
                print(f"Title: {book['Title']}, Author: {book['Author']}, Year: {book['year']}")
                found = True
                break
        if not found:
            print("Book is not available.")

    elif inputusr == '4':
        dele = input("Enter title of the book to delete: ")
        found = False
        for book in Books:
            if book["Title"].lower() == dele.lower():
                Books.remove(book)
                print("Book deleted successfully.")
                found = True
                break
        if not found:
            print("Book not found.")

    elif inputusr == '5':
        print("Exiting.....")
        break

    else:
        print("Invalid input. Please try again.")

