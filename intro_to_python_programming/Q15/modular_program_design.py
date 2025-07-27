class Library:
    def __init__(self, books):
        self.books = set()
    
    def add_book(self, book):
        self.books.add(book)
        return f"Book {book} succesfully added."
    
    def search_book(self, book):
        if book in self.books:
            # return self.books.(book)
            pass
        pass

    def dispaly_books(self):
        for book in self.books:
            print(f"Book: {book}")


    pass

