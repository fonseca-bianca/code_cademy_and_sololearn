"""
Python also allows you to pass keyword arguments using 
**kwargs. In this case, **kwargs receives arguments in the 
form of a dictionary, consisting of key:value pairs.
"""

# **kwargs is a dictionary:
def display_info(**kwargs):
    # kwargs.items() returns the key:value pairs
    for key, value in kwargs.items():
        print(f"{key}: {value}")
        
display_info(name="Louise", age=30, city="Vancouver")
# keys: name, age, city
# values: Louise, 30, Vancouver