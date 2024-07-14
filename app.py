from library import Library
from book import Book
from user import User
import utils

def main():
    library = Library()
    
    while True:
        print("\nLibrary Management System")
        print("1. Add Book")
        print("2. View Books")
        print("3. Search Books")
        print("4. Search Books by Author")
        print("5. Remove Book")
        print("6. Lend Book")
        print("7. View Lent Books")
        print("8. Return Book")
        print("9. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            title = input("Enter the title: ")
            authors = input("Enter the authors (comma-separated): ").split(',')
            isbn = input("Enter the ISBN: ")
            publishing_year = utils.get_int("Enter the publishing year: ")
            price = utils.get_float("Enter the price: ")
            quantity = utils.get_int("Enter the quantity: ")
            book = Book(title, authors, isbn, publishing_year, price, quantity)
            library.add_book(book)
            print(f"Book '{title}' added successfully.")
        
        elif choice == '2':
            library.view_books()
        
        elif choice == '3':
            search_term = input("Enter the title or ISBN to search: ")
            library.search_books(search_term)
        
        elif choice == '4':
            author = input("Enter the author to search: ")
            library.search_books_by_author(author)
        
        elif choice == '5':
            isbn = input("Enter the ISBN of the book to remove: ")
            library.remove_book(isbn)
        
        elif choice == '6':
            isbn = input("Enter the ISBN of the book to lend: ")
            user_name = input("Enter the name of the user: ")
            user = User(user_name)
            library.lend_book(isbn, user)
        
        elif choice == '7':
            library.view_lent_books()
        
        elif choice == '8':
            isbn = input("Enter the ISBN of the book to return: ")
            library.return_book(isbn)
        
        elif choice == '9':
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
