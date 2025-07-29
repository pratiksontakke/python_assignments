class Library:
    def __init__(self):
        self.books = set()

    def add_book(self, book):
        self.books.add(book)
        return f"Book '{book}' successfully added."

    def search_book(self, book):
        if book in self.books:
            return f"Book '{book}' is available in the library."
        else:
            return f"Book '{book}' not found in the library."

    def display_books(self):
        if self.books:
            print("Books in the library:")
            for book in self.books:
                print(f"- {book}")
        else:
            print("No books available in the library.")

if __name__ == "__main__":
    library = Library()
    while True:
        try:
            user_input = int(input("\nType 1 to add a book\nType 2 to search for a book\nType 3 to view all books\nType 4 to exit\n>> "))
            if user_input == 1:
                book_name = input("Enter book name to add: ")
                print(library.add_book(book_name))
            elif user_input == 2:
                book_name = input("Enter book name to search: ")
                print(library.search_book(book_name))
            elif user_input == 3:
                library.display_books()
            elif user_input == 4:
                print("Exiting... Thank you!")
                break
            else:
                print("Invalid input. Please choose between 1 and 4.")
        except ValueError:
            print("Please enter a valid number.")
