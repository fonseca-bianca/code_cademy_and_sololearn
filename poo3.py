"""
The main difference between FUNCTIONS and METHODS is that 
FUNCTIONS are independent and can be called on their own, 
while METHODS are associated with a class and can be called 
only with its instance. This means that you can't call a 
methods without having the instance of a class where that 
method is defined
"""

# print() = function
# my_car.fonk(): method #fonk = buzinar

"""
Everything in Python, including FUNCTIONS, is a Object.
For instance, integers are instances of the 'int' class, and
functions are instances of the function classe, among others.
This OOP nature underlies Python's flexibility and power
"""
# function:
def greet():
    print("Welcome!")
    
# list:
prices = [1.25, 50.99]

# data types:
x = 5 # int
city = "Vancouver" # string
is_open = True # boolean

print(type(greet)) # output: <class 'function'>
print(type(prices)) # output: <class 'list'>
print(type(x)) # output: <class 'int'>
print(type(city)) # output: <class 'str'>
print(type(is_open)) # output: <class 'bool'>