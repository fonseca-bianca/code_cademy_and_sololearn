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
    
    def print_info(self):
        print(f"{self.brand}, {self.model}, {self.color}")

# Criando um carro
meu_carro = Car("Toyota", "Camry", "Orange")

# Imprimindo tudo de uma vez
meu_carro.print_info()  # Saída: Toyota, Camry, Orange