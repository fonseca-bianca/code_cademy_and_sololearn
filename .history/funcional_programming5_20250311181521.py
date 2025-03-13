"""
An important concept in Funcional Programming is PURE FUNCTIONS.
A function is called 'pure' if it gives the same result every
time you give it the same inputs, and it doesn't affect anything
outside of the function. This makes them trustworthy and simpler
to understand.
"""

def total(price, count):
    return price + count