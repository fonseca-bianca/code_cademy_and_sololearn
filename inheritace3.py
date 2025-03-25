"""
You can define methods with the same name in both 
parent and child classe, bnut they can perfomr different 
operations. This is known as 'method overriding'. For instance,
consider the Animal class with a sound() method. The Dog and 
Cat child classes inherit the sound() method from Animal, but
override it to suit their specific need.
"""

# parent class:
class Animal:
    def __init__(self, name):
        self.name = name
        
    # generic sound method for any Animal:
    def sound(self):
        print("Meking a sound")
        
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

# using overridden methods:
my_dog.sound() # output: Woof!
my_cat.sound() # output: Meow!