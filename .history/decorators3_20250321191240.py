"""
Imagine you have a function that generates a message. Your 
goal is to create another function that takes this original 
function as an argument and converts the original message 
into uppercase, without altering the original function's code.

These functions are known as decorators. In the code below, 
the uppercase() function acts as a decorator, and the 
wrapper() function represents the modified (or decorated) 
version of the greet() function.

DECORATORS:
they modify a function's behavior (comportamento) without 
alterging its original code.
- Components of Decorator:
    * a function that modifies the original function;
    * a function as an argument
"""

def greet():
    return "Hello!"

# takes a function as an argument:
def uppercase(func): # uppercase() é uma função genérica, portanto, ela poderá receber qlqr argumento
    # se usasse a função (greet) como parâmetro, uppercase() estaria limitada à função (greet) como seu parâmetro
    # wrapper function to keep the original function code unchanged
    def wrapper():
        original_message = func()
        modified_message = original_message.upper()
        return modified_message
    return wrapper

greet_uper = uppercase(greet) # greet_upper(): é função wrapper
print(greet_uper())

# output: HELLO!