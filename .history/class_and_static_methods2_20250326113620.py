"""
Class methods are called on the class itself, not on individual
instances. This allows their use without needing to create a 
class instance. They are especially useful for actions 
relevant to the class as a whole, rather than actions limited 
to a single object. Here's an example:
"""

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        
    # regular method:
    def describe_book(self):
        print(self.title, "by", self.author)
        
    # class method:
    @classmethod # decorator for creation of a class method
    def books_in_series(cls, series_name, number_of_books): # cls = refers to the class itself (Book)
        print("There are", number_of_books, "books in series", series_name)
    
# create an instance of Book:
my_book = Book("Harry Potter and the Philosopher's Stone", "J.K. Rowling")

# use the instance method to describe the book:
my_book.describe_book() # output: Harry Potter and the Philosopher's Stone by J. K. Rowling

# use the class method to display information about the series:
Book.books_in_series("Harry Potter", 7) # output: There are 7 books in series Harry Potter

