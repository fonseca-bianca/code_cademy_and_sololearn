"""
What if we want to not only inheritance attibutes but also 
add specific ones to a child class? In this case, we define 
an '__init__' method in the child class. Use 
'super().__init__()' to inherit attibutes from the parent 
class, and then define any additional attributes as usual
"""

# parent class:
class Animal:
    def __init__(self, name):
        self.name = name

    def move(self):
        print("Moving")
        
# child class:
class Dog(Animal):
    def __init__(self, name, breed, age):
        
        # initialize attributes of the superclass:
        super().__init__(name)
        
        # additional attributes specific to Dog:
        self.breed = breed
        self.age = age
        
    def bark(self):
        print("Woof!")
        
my_dog = Dog(name="Rex", breed="Golden Retriever", age=3)

# inherited attribute
print(my_dog.name)

# additional attributes:
print(my_dog.breed)
print(my_dog.age)