"""
You can also designate methods as protected or private, 
following the same convention as with attributes. Protected 
methods are prefixed with a single underscore and can be 
accessed within the class and its subclasses. However, private
methods, marked by a double underscore, cannot be directly 
accessed from outside the class.
"""

class Car:
    def __init__(self, model, year, odometer):
        self.model = model
        self.year = year
        self.__odometer = odometer # private attribute
        
    def describe_car(self):
        print(self.year, "-", self.model)
        
    def read_odometer(self):
        print("Odometer: ", self._odometer, "miles")
        
my_car = Car("Toyota", 2019, 5000)

my_car.describe_car() # output: 2019 Toyota
my_car.read_odometer() # output: Odometer: 5000 miles  

print(my_car._odometer) # output: 5000