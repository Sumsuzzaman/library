import json
from book import Book
from user import User

class Library:
    def __init__(self, filename='library.json'):
        self.books = []
        self.lent_books = []
        self.filename = filename
        self.load_books()

    def add_book(self, book):
        self.books.append(book)
        self.save_books()

    def remove_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                self.books.remove(book)
                self.save_books()
                return
        print("This book isn’t available to remove.")

    def view_books(self):
        if not self.books:
            print("No books found in the library.")
        else:
            for book in self.books:
                print(book)

    def search_books(self, search_term):
        results = [book for book in self.books if search_term.lower() in book.title.lower() or search_term in book.isbn]
        if not results:
            print("No books found matching the search term.")
        else:
            for book in results:
                print(book)

    def search_books_by_author(self, author):
        results = [book for book in self.books if author.lower() in ' '.join(book.authors).lower()]
        if not results:
            print("No books found for the given author.")
        else:
            for book in results:
                print(book)

    def lend_book(self, isbn, user):
        for book in self.books:
            if book.isbn == isbn:
                if book.quantity > 0:
                    book.quantity -= 1
                    book.lent_to = user.name
                    self.lent_books.append(book)
                    self.save_books()
                    return
                else:
                    print("Not enough books available to lend.")
                    return
        print("Book not found.")

    def return_book(self, isbn):
        for book in self.lent_books:
            if book.isbn == isbn:
                book.quantity += 1
                book.lent_to = None
                self.lent_books.remove(book)
                self.save_books()
                return
        print("Book not found.")

    def view_lent_books(self):
        if not self.lent_books:
            print("No books are currently lent out.")
        else:
            for book in self.lent_books:
                print(f"{book} lent to {book.lent_to}")

    def save_books(self):
        with open(self.filename, 'w') as f:
            books_data = [book.__dict__ for book in self.books]
            json.dump(books_data, f, indent=4)

    def load_books(self):
        try:
            with open(self.filename, 'r') as f:
                books_data = json.load(f)
                for book_data in books_data:
                    book = Book(**book_data)
                    self.books.append(book)
        except FileNotFoundError:
            pass
