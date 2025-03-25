"""
Method overriding is a demonstration of another key concept 
in OOP - polymorphism. Polymorphism lets objects use methods 
in their own way, even if they share the same name.

In this example, even though each animal in the animals list 
may be of a different subclass, the code can call sound() on 
each without needing to know its specific type.
"""

# parent class:
class Animal:
    def __init__(self, name):
        self.name = name
        
    # generic sound method for any Animal:
    def sound(self):
        print("Making a sound:" )
        
# child class Dog:
class Dog(Animal):
    def __init__(self, name, breed, age):
        super().__init__(name)
        self.breed = breed
        self.age = age
        
    # overriding sound method for Dog class:
    def sound(self):
        super().sound() # calling parent class method
        print("Woof!")
        
# child class Cat:
class Cat(Animal):
    def __init__(self, name, breed, age):
        super().__init__(name)
        self.breed = breed
        self.age = age
        
    # overriding sound method for Cat class:
    def sound(self):
        print("Meow!")
        
# create instances:
my_dog = Dog(name="Rex", breed="Golden Retriever", age=3)
my_cat = Cat(name="Whiskers", breed="Siamese", age=2)

animals = [my_dog, my_cat]

for animal in animals:
    animal.sound() # output: Woof! Meow!