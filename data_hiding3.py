"""
The next level of data hiding involves making an attribute 
private. 
This is achieved by prefixing the attribute name with 
two underscores (e.g., __attribute). In this case, unlike 
protected attributes, this is not just a convention - it 
limits its access outside the class through name mangling, 
enhancing data protection and encapsulation. This method is 
used for sensitive or internal data, strongly discouraging 
external access.
"""

class Car:
    def __init__(self, model, year, odometer):
        self.model = model
        self.year = year
        self.__odometer = odometer # private attribute (single underscore)
    
    # Encapsulamento:
    # criação de método público 'getter' pra acessar o atributo privado
    def get_odometer(self):  # método público para leitura
        return self.__odometer

my_car = Car("Audi", 2023, 5000)
print(my_car.get_odometer())  # saída: 5000