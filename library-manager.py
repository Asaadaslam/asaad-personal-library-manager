import json

# Load existing library data from file
try:
    with open("library.txt", "r") as file:
        library = json.load(file)
except FileNotFoundError:
    library = []

# Save library to file
def save_library():
    with open("library.txt", "w") as file:
        json.dump(library, file, indent=4)

# Add a book
def add_book():
    title = input("Enter the book title: ")
    author = input("Enter the author: ")
    year = int(input("Enter the publication year: "))
    genre = input("Enter the genre: ")
    read = input("Have you read this book? (yes/no): ").strip().lower() == "yes"
    
    book = {
        "title": title,
        "author": author,
        "year": year,
        "genre": genre,
        "read": read
    }
    library.append(book)
    print("Book added successfully!\n")

# Remove a book
def remove_book():
    title = input("Enter the title of the book to remove: ")
    for book in library:
        if book["title"].lower() == title.lower():
            library.remove(book)
            print("Book removed successfully!\n")
            return
    print("Book not found.\n")

# Search for a book
def search_book():
    print("Search by:\n1. Title\n2. Author")
    choice = input("Enter your choice: ")
    query = input("Enter the search term: ")
    results = []
    
    if choice == "1":
        results = [book for book in library if query.lower() in book["title"].lower()]
    elif choice == "2":
        results = [book for book in library if query.lower() in book["author"].lower()]

    if results:
        print("Matching Books:")
        for i, book in enumerate(results, 1):
            status = "Read" if book["read"] else "Unread"
            print(f"{i}. {book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {status}")
    else:
        print("No matching books found.")
    print()

# Display all books
def display_books():
    if not library:
        print("No books in your library.\n")
        return
    print("Your Library:")
    for i, book in enumerate(library, 1):
        status = "Read" if book["read"] else "Unread"
        print(f"{i}. {book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {status}")
    print()

# Display statistics
def display_statistics():
    total = len(library)
    if total == 0:
        print("No books in library.\n")
        return
    read_books = len([book for book in library if book["read"]])
    percent_read = (read_books / total) * 100
    print(f"Total books: {total}")
    print(f"Percentage read: {percent_read:.1f}%\n")

# Menu system
def menu():
    while True:
        print("Welcome to your Personal Library Manager!")
        print("1. Add a book")
        print("2. Remove a book")
        print("3. Search for a book")
        print("4. Display all books")
        print("5. Display statistics")
        print("6. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            add_book()
        elif choice == "2":
            remove_book()
        elif choice == "3":
            search_book()
        elif choice == "4":
            display_books()
        elif choice == "5":
            display_statistics()
        elif choice == "6":
            save_library()
            print("Library saved to file. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.\n")

# Start program
if __name__ == "__main__":
    menu()
