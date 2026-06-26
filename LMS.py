class Book:
    def __init__(self, book_id, title, author):
        self.book_id = book_id.strip()
        self.title = title.strip()
        self.author = author.strip()
        self.is_issued = False
        self.issued_to = None

    def display_book(self):
        status = "Available" if not self.is_issued else f"Issued to {self.issued_to}"

        print("\n-----------------------------")
        print(f"Book ID : {self.book_id}")
        print(f"Title   : {self.title}")
        print(f"Author  : {self.author}")
        print(f"Status  : {status}")
        print("-----------------------------")


class Member:
    def __init__(self, member_id, name):
        self.member_id = member_id.strip()
        self.name = name.strip()
        self.borrowed_books = []

    def display_member(self):
        print("\n-----------------------------")
        print(f"Member ID : {self.member_id}")
        print(f"Name      : {self.name}")

        if self.borrowed_books:
            print("Borrowed Books :", ", ".join(self.borrowed_books))
        else:
            print("Borrowed Books : None")

        print("-----------------------------")


class Library:
    def __init__(self):
        self.books = {}
        self.members = {}

    # ---------------- BOOK OPERATIONS ----------------

    def add_book(self):
        book_id = input("Enter Book ID: ").strip()

        if book_id in self.books:
            print("Book ID already exists!")
            return

        title = input("Enter Book Title: ").strip()
        author = input("Enter Author Name: ").strip()

        self.books[book_id] = Book(book_id, title, author)
        print("Book added successfully!")

    def view_books(self):
        if not self.books:
            print("No books available in library.")
            return

        print("\n========== BOOK LIST ==========")

        for book in self.books.values():
            book.display_book()

    def remove_book(self):
        book_id = input("Enter Book ID to remove: ").strip()

        if book_id not in self.books:
            print("Book not found!")
            return

        if self.books[book_id].is_issued:
            print("Cannot remove an issued book.")
            return

        del self.books[book_id]
        print("Book removed successfully!")

    # ---------------- MEMBER OPERATIONS ----------------

    def add_member(self):
        member_id = input("Enter Member ID: ").strip()

        if member_id in self.members:
            print("Member ID already exists!")
            return

        name = input("Enter Member Name: ").strip()

        self.members[member_id] = Member(member_id, name)
        print("Member registered successfully!")

    def view_members(self):
        if not self.members:
            print("No members registered.")
            return

        print("\n========== MEMBER LIST ==========")

        for member in self.members.values():
            member.display_member()

    # ---------------- ISSUE BOOK ----------------

    def issue_book(self):
        book_id = input("Enter Book ID: ").strip()
        member_id = input("Enter Member ID: ").strip()

        if book_id not in self.books:
            print("Book not found!")
            return

        if member_id not in self.members:
            print("Member not found!")
            return

        book = self.books[book_id]
        member = self.members[member_id]

        if book.is_issued:
            print("Book is already issued.")
            return

        book.is_issued = True
        book.issued_to = member.name
        member.borrowed_books.append(book.title)

        print(f"'{book.title}' issued to {member.name} successfully!")

    # ---------------- RETURN BOOK ----------------

    def return_book(self):
        book_id = input("Enter Book ID to return: ").strip()

        if book_id not in self.books:
            print("Book not found!")
            return

        book = self.books[book_id]

        if not book.is_issued:
            print("This book was not issued.")
            return

        for member in self.members.values():
            if book.title in member.borrowed_books:
                member.borrowed_books.remove(book.title)

        book.is_issued = False
        book.issued_to = None

        print("Book returned successfully!")

    # ---------------- SEARCH BOOK ----------------

    def search_book(self):
        keyword = input(
            "Enter Book Title or Author Name: "
        ).lower().strip()

        found = False

        for book in self.books.values():
            if (
                keyword in book.title.lower()
                or keyword in book.author.lower()
            ):
                book.display_book()
                found = True

        if not found:
            print("No matching books found.")


def display_menu():
    print("\n")
    print("====================================")
    print("      LIBRARY MANAGEMENT SYSTEM")
    print("====================================")
    print("1. Add Book")
    print("2. View Books")
    print("3. Remove Book")
    print("4. Register Member")
    print("5. View Members")
    print("6. Issue Book")
    print("7. Return Book")
    print("8. Search Book")
    print("9. Exit")
    print("====================================")


def main():
    library = Library()

    while True:
        display_menu()

        try:
            choice = input("Enter your choice: ").strip()

            if choice == "1":
                library.add_book()

            elif choice == "2":
                library.view_books()

            elif choice == "3":
                library.remove_book()

            elif choice == "4":
                library.add_member()

            elif choice == "5":
                library.view_members()

            elif choice == "6":
                library.issue_book()

            elif choice == "7":
                library.return_book()

            elif choice == "8":
                library.search_book()

            elif choice == "9":
                print("\nThank you for using Library Management System.")
                break

            else:
                print("Invalid choice! Please try again.")

        except KeyboardInterrupt:
            print("\nProgram terminated by user.")
            break

        except Exception as e:
            print(f"Unexpected error occurred: {e}")


if __name__ == "__main__":
    main()

