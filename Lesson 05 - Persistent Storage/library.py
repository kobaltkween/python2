import shelve

class Library:
    def __init__(self, fn):
        self.fn = fn
        self.shelf = shelve.open(fn)
    
    def add(self, book):
        self.shelf[book.isbn] = book
    
    def getByIsbn(self, isbn):
        return self.shelf[isbn]
    
    def getByTitle(self, title):
        for book in self.shelf.values():
            if book.title == title:
                return book
        return None
    
    def getByAuthor(self, author):
        for book in self.shelf.values():
            for a in book.authors:
                if a == author:
                    return book
        return None
    
    def close(self):
        self.shelf.close()
    

class Book:
    def __init__(self, isbn, title, authors):
        self.isbn, self.title, self.authors = isbn, title, authors
        
    def __eq__(self, other):
        if type(other) is type(self):
            return self.__dict__ == other.__dict__
        return False
    
    def __ne__(self, other):
        return not self.__eq__(other)
    

class Author:
    def __init__(self, firstName, middleName, lastName):
        self.firstName, self.middleName, self.lastName = firstName, middleName, lastName
        
    def __eq__(self, other):
        if type(other) is type(self):
            return self.__dict__ == other.__dict__
        return False
    def __ne__(self, other):
        return not self.__eq__(other)