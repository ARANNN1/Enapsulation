class Book:
    def __init__(self, title, author, publication_year):
        self.title = title
        self.author = author
        self.publication_year = publication_year
        self.is_available = True
    
    def get_title(self):
        return self.title
    
    def get_author(self):
        return self.author
    
    def get_publication_year(self):
        return self.publication_year
    
    def is_book_available(self):
        return self.is_available
    
    def borrow_book(self):
        if self.is_available:
            self.is_available = False
            return True
        else:
            return False
    
    def return_book(self):
        if not self.is_available:
            self.is_available = True
            return True
        else:
            return False


library = []

# Prompt the user to enter book details and add them to the library
while True:
    title = input("Enter the title of the book (or 'q' to quit): ")
    if title == "q":
        break
    
    author = input("Enter the author of the book: ")
    publication_year = input("Enter the publication year of the book: ")
    
    book = Book(title, author, publication_year)
    library.append(book)
    print("Book added to the library.")

# Display the available books in the library
print("\nAvailable Books:")
for i, book in enumerate(library):
    if book.is_book_available():
        print(f"{i}: {book.get_title()} by {book.get_author()} ({book.get_publication_year()})")

# Prompt the user to choose a book to borrow
while True:
    book_index = input("\nEnter the index of the book to borrow (or 'q' to quit): ")
    if book_index == "q":
        break
    
    book_index = int(book_index)
    if book_index >= 0 and book_index < len(library):
        book = library[book_index]
        if book.borrow_book():
            print("Book borrowed successfully.")
        else:
            print("Book is not available for borrowing.")
        
        # Display the available books in the library
        print("\nAvailable Books:")
        for i, book in enumerate(library):
            if book.is_book_available():
                print(f"{i}: {book.get_title()} by {book.get_author()} ({book.get_publication_year()})")
        
        # Prompt the user to choose a book to return
        return_index = input("Enter the index of the book to return: ")
        return_index = int(return_index)
        if return_index >= 0 and return_index < len(library):
            return_book = library[return_index]
            if not return_book.is_book_available():
                return_book.return_book()
                print("Book returned successfully.")
            else:
                print("Book is already available.")
        
        # Display the available books in the library
        print("\nAvailable Books:")
        for i, book in enumerate(library):
            if book.is_book_available():
                print(f"{i}: {book.get_title()} by {book.get_author()} ({book.get_publication_year()})")
    else:
        print("Invalid book index.")
