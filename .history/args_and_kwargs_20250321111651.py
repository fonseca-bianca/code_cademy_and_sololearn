"""
When calling a function, you need to use the same number of
arguments that have been defined, in the same order.

1- What's theoutput of this code?
""" 

def total(x, y, z):
    return x + y + z

print(total(1, 2, 3, 4)) 
# output: 
# TypeError: total() takes 3 positional arguments but 4 were given