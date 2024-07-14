class Book:
    def __init__(self, title, authors, isbn, publishing_year, price, quantity, lent_to=None):
        self.title = title
        self.authors = authors
        self.isbn = isbn
        self.publishing_year = publishing_year
        self.price = price
        self.quantity = quantity
        self.lent_to = lent_to

    def __str__(self):
        lent_status = f" (lent to {self.lent_to})" if self.lent_to else ""
        return f"{self.title} by {', '.join(self.authors)} (ISBN: {self.isbn}, Year: {self.publishing_year}, Price: ${self.price}, Quantity: {self.quantity}){lent_status}"
