"""
In programming, there is a paradigm that follows the same
principle as blueprints and instances. It's called OOP. In
OOP, blueprints are referred to as classes and instances
are known as objects.
"""

# abstraction of a car: class
# a green car on a website: instance

"""
In the real world, everything has distinguishing characteristics:
a dog has its breed, color and name; a car has its brand, model
and color. In programming, classes and objects mirror this concept 
with attributes. Those are the properties that define an object's
individuality within a class.
1 - Use the image to select all the attributes of the Car class
"""

class Car:
    def __init__(self, brand, model, color):
        self.brand = brand
        self.model = model
        self.color = color

car1 = Car("Toyota", "Camry", "Green")
car2 = Car("Jeep", "Wrangler", "Green")

print(car1)  
print(car2)  