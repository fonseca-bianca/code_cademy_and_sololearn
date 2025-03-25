"""
In Python, data hiding has two levels. The first involves 
prefixing an attribute with a single underscore _, signaling 
it's meant for internal use and should be viewed as 
'protected'.
"""
class Car:
    def __init__(self, model, year, odometer):
        self.model = model
        self.year = year
        self._odometer = odometer # protected attribute
        
    def describe_car(self):
        print(self.year, self.model)
        
    def read_odometer(self):
        print("Odometer: ", self._odometer, "miles")  