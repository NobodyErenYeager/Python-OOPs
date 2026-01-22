class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def display_info(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Year: {self.year}")


class FictionBook(Book):
    def __init__(self, title, author, year, genre):
        super().__init__(title, author, year)
        self.genre = genre
    
    def display_info(self):
        super().display_info()
        print(f"Genre: {self.genre}")


class NonFictionBook(Book):
    def __init__(self, title, author, year, topic):
        super().__init__(title, author, year)
        self.topic = topic

    def display_info(self):
        super().display_info()
        print(f"Topic: {self.topic}")


class Library:
    books_list = []

    def add_book(self, book):
        self.books_list.append(book)
    
    def search_by_author(self, author):
        for book in self.books_list:
            if book.author == author:
                book.display_info()
                print("#########################################")

    def search_by_year(self, year):
        for book in self.books_list:
            if book.year == year:
                book.display_info()
                print("#########################################") 

library = Library()

library.add_book(FictionBook(
    title="Harry Potter and the Deathly Hallows",
    author="J.K. Rowling",
    year=2007,
    genre="Fantasy"
))

library.add_book(FictionBook(
    title="Handmaids Tale",
    author="Margaret Atwood",
    year=1985,
    genre="Dystopian"
))

library.add_book(NonFictionBook(
    title="Atomic Habits",
    author="James Clear",
    year=2018,
    topic="Self-help"
))

library.add_book(NonFictionBook(
    title="Rich Dad Poor Dad",
    author="Robert Kiyosaki",
    year=1997,
    topic="Personal Finance"
))

library.search_by_year(2007)
library.search_by_year(2000)
library.search_by_author("James Clear")
