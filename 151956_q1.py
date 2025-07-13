class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False

    def mark_as_borrowed(self):
        self.is_borrowed = True

    def mark_as_returned(self):
        self.is_borrowed = False


class LibraryMember:
    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id
        self.borrowed_books = []

    def borrow_book(self, book):
        if not book.is_borrowed:
            book.mark_as_borrowed()
            self.borrowed_books.append(book)
            print(f"{self.name} has borrowed '{book.title}'.")
        else:
            print(f"'{book.title}' is already borrowed.")

    def return_book(self, book):
        if book in self.borrowed_books:
            book.mark_as_returned()
            self.borrowed_books.remove(book)
            print(f"{self.name} has returned '{book.title}'.")
        else:
            print(f"{self.name} hasn't borrowed '{book.title}'.")

    def list_borrowed_books(self):
        if not self.borrowed_books:
            print("No books currently borrowed.")
        else:
            print("Borrowed books:")
            for book in self.borrowed_books:
                print(f"- {book.title} by {book.author}")


# Interactive session
book1 = Book("1984", "George Orwell")
book2 = Book("The Hobbit", "J.R.R. Tolkien")

member = LibraryMember("Alice", "LM123")

while True:
    print("\n--- Library Menu ---")
    print("1. Borrow a book")
    print("2. Return a book")
    print("3. List borrowed books")
    print("4. Exit")
    choice = input("Choose an option: ")

    if choice == "1":
        book_title = input("Enter book title to borrow: ")
        if book_title == book1.title:
            member.borrow_book(book1)
        elif book_title == book2.title:
            member.borrow_book(book2)
        else:
            print("Book not found.")

    elif choice == "2":
        book_title = input("Enter book title to return: ")
        if book_title == book1.title:
            member.return_book(book1)
        elif book_title == book2.title:
            member.return_book(book2)
        else:
            print("Book not found.")

    elif choice == "3":
        member.list_borrowed_books()

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid choice.")