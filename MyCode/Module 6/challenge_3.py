class Item:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"Title: {self.title}, Author: {self.author}"


class Book(Item):
    def __init__(self, title, author, pages):
        Item.__init__(self, title, author)
        self.pages = pages

    def __len__(self):
        return self.pages
    

class DVD(Item):
    def __init__(self, title, director, duration):
        Item.__init__(self, title, director)
        self.duration = duration

    def __len__(self):
        return self.duration
    

class LibraryItem(Book, DVD):
    def __init__(self, title, author, pages, director, duration, copies):
        Book.__init__(self, title, author, pages)
        DVD.__init__(self, title, director, duration)
        self.copies = copies
        self.director = director

    def __str__(self):
        return f"{self.title} by {self.author} (Book: {self.pages} pages, DVD: {self.duration} minutes)"
    
    def __add__(self, other):
        if isinstance(other, LibraryItem):
            combo = self.copies + other.copies
            return LibraryItem(self.title, self.author, self.pages, self.director, self.duration, combo)
        else:
            raise TypeError("Can not add.")
    

book = Book("Harry Potter", "JK Rowling", 500)

dvd = DVD("Inception", "Christopher Nolan", 130)

library_item = LibraryItem("Python Course","Josh Wenner", 500, "James Cameron",160, 10)

print(book)
print(dvd)
print(library_item)


print(len(book))
print(len(dvd))
            
            
add_items = library_item + library_item
print(add_items)
        
print(add_items.copies)
