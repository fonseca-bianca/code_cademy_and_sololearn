"""
To add attributes to a class, you must define the 
'__init__ method'. This method's first parameter is always 
self, which represents the instance of the class. self, you 
specify the attributes you Following wish to include. Then, 
inside the function, you assign values ​​to the initialized 
object's attributes, setting their initial state.
"""

class Car:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color
        
my_car = Car("Citroen", "black")
print(my_car)