""" 
The else statement can be used in conjunction with the 
try/except block and will execute only when no error occurs 
in the try block.
"""

books = ["HP", "Dune", "Emma"]
try:
    choice = books[1]
except IndexError:
    print("Out of range")
else:
    print(choice + " is a great choice")
    
#output: Dune is a great choice