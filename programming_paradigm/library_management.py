class Book:
    """
    Represents a book with a title, author, and checkout status.
    _is_checked_out is a private attribute demonstrating encapsulation.
    """
    def __init__(self, title, author):
        # Public attributes
        self.title = title
        self.author = author
        # Private attribute (conventionally marked by a single underscore)
        self._is_checked_out = False

    def check_out(self):
        """Marks the book as checked out if it's currently available."""
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        return False

    def return_book(self):
        """Marks the book as available if it's currently checked out."""
        if self._is_checked_out:
            self._is_checked_out = False
            return True
        return False

    def is_available(self):
        """Returns the current availability status of the book."""
        return not self._is_checked_out

    def __str__(self):
        """String representation for easy printing."""
        return f"{self.title} by {self.author}"


class Library:
    """
    Manages a collection of Book objects and handles library operations.
    """
    def __init__(self):
        # Private list to store Book instances (demonstrates encapsulation)
        self._books = []

    def add_book(self, book):
        """Adds a Book object to the library's collection."""
        self._books.append(book)
        # print(f"Added: {book.title}") # Optional confirmation

    def _find_book(self, title):
        """Helper method to find a Book object by title."""
        for book in self._books:
            if book.title == title:
                return book
        return None

    def check_out_book(self, title):
        """Checks out a book by title, if available."""
        book = self._find_book(title)
        if book:
            if book.check_out():
                # print(f"Successfully checked out '{title}'.") # Optional confirmation
                return True
            else:
                print(f"'{title}' is already checked out.")
                return False
        else:
            print(f"Error: Book with title '{title}' not found.")
            return False

    def return_book(self, title):
        """Returns a book by title, if it was checked out."""
        book = self._find_book(title)
        if book:
            if book.return_book():
                # print(f"Successfully returned '{title}'.") # Optional confirmation
                return True
            else:
                print(f"'{title}' was not checked out.")
                return False
        else:
            print(f"Error: Book with title '{title}' not found.")
            return False

    def list_available_books(self):
        """Prints all books that are currently available (not checked out)."""
        available_count = 0
        for book in self._books:
            if book.is_available():
                print(book)
                available_count += 1
        
        if available_count == 0:
            print("No books are currently available.")

# End of library_management.py