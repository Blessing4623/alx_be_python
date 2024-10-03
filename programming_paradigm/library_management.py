class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False
    def check_out(self):
        self._is_checked_out = True
        return self._is_checked_out
    def return_book(self):
        self._is_checked_out = False
        return self._is_checked_out
class Library:
    def __init__(self):
        self._books = []
    def add_book(self, title, author):
        for book in self._books:
            if book.title == title:
                return "Book is in Library"
        self._books.append(Book(title, author))
    def check_out_book(self, title):
        for book in self._books:
            if book.title == title and book._is_checked_out:
                return f"{title} is already checked out"
            elif book.title == title and not book._is_checked_out:
                book.check_out()
        else:
            return f"{title} is not in library"
    def return_book(self, title):
        for book in self._books:
            if book.title == title and book._is_checked_out:
                book.return_book()
            elif book.title == title and not book._is_checked_out:
                return f"{title} is not checked out"
    def list_available_books(self):
        for book in self._books:
            if book._is_checked_out:
                pass
            elif not book._is_checked_out:
                print(book.title, book.author)