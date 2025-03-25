"""
Inheritance = Herança
The strength of OOP lies in organizing a program so its various
components, treated as classes and objects can interact 
smoothly.
"""
"""
Inheritance is a key concept for situations where you have an 
existing class with defined attributes and behaviors, and you 
need a new class that not only shares these characteristics 
but also has its own unique ones. Inheritance allow the new 
class to 'inherit' properties from existing class while adding
or modifying specific features as needed.
"""

class Animal:
    def __init__(self, name):
        self.name = name
        
        def move(self):
            print("Moving")
            
        # inherits from Animal class:
        class Dog(Animal):
            # specifi behavior
            def bark(self):
                print("Woof!")
                
        # creating an instance:
        my_dog = Dog(name="Rex")
        
        # inherited attribute and behavior:
        print(my_dog.name)
        my_dog.move()
        
        # specific behavior:
        my_dog.bark()
