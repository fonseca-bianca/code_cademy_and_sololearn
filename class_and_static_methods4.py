"""
Static Methods are similar to Class Methods, except they 
don't receive any additional arguments; they are identical 
to normal functions that belong to a class. They are marked 
with the @staticmethod decorator
"""

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        
    # regular method:
    def describe_book(self):
        print(self.title, "by", self.author)
        
    # static method:
    @staticmethod # decorator for creation of a static method
    def books_in_series(series_name, number_of_books):
        print("There are", number_of_books, "books in series", series_name)
        
# create an instance of Book:
my_book = Book("Foundation", "Isaac Asimov")

# use the instance method to describe the book:
my_book.describe_book() # output: Foundation by Isaac Asimov

# call the static method:
Book.books_in_series("Foundation", 3) # output: There are 3 books in series Foundation  