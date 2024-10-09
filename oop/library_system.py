class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
    def __str__(self):
        return f"{self.title} by {self.author}"

class EBook(Book):
    def __init__(self, title, author, file_size:int):
        super().__init__(title, author)
        self.file_size = file_size
        



class PrintBook(Book):
    def __init__(self, title, author, page_count:int):
        
        super().__init__(title, author)
        self.page_count = page_count

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