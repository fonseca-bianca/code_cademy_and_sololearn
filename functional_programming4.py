"""
In Python, functions that operate with other functions - that 
is, take another function as an argument or return a function - 
are called HIGHER-ORDER FUNCTIONS. They are particularly useful
for processing various functions and returning specific results.
"""

def welcome(name):
    return "Welcome, " + name

def bye(name):
    return "Bye, " + name

def process_user(name, func):
    return func(name)

print(process_user("Alice", welcome)) 
#output: Welcome, Alice
print(process_user("John", bye))
#output: Bye, John

