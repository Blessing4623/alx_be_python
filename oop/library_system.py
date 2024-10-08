class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

class EBook(Book):
    def __init__(self, title, author, filesize:int):
        self.title = title
        self.filesize = filesize
        self.author = author



class PrintBook(Book):
    def __init__(self, title, author, pagecount:int):
        self.title = title
        self.author = author
        self.pagecount = pagecount

class Library:
    def __init__(self):
        self.books = []
    def add_book(self, book):
         
        self.book = book
        for bok in self.books:
            if self.book == bok:
                return f"book is in library"
        return self.books.append(self.book)
    def list_books(self):
        for bok in self.books:
            print(f"{bok.title} by {bok.author}")