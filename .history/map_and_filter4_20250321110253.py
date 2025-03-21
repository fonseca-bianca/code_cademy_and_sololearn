"""
Do you remember lambda expressions? Another valuable aspect of
them is their ability to be directly provided to the map function.
This eliminates the need to define a regular funcion explicitly
"""

number = [1, 2, 3]  
doubled = list(map(lambda x: x*2, number))
print(doubled)

# lambda: é função anônima