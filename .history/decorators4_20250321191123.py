"""
You can apply a decorator to a function using the @ sign.
It improves the code readability and provides a clean separation
between the function and its decoration.
When a funtion with a decorator is called, it automatically
includes the behavior defined in the decorator
"""

def uppercase(func):
    def wrapper():
        original_message = func()
        modified_message = original_message.upper()
        return modified_message
    return wrapper

@uppercase
def greet():
    return "Hello!"

# using the decoreted function:
print(greet())

# output: HELLO!