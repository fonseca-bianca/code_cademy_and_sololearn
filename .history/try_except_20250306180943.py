"""
Para lidar com um tipo específico de exceção, você precisa especificá-lo no 
bloco except.
1 - Complete o código para lidar com uma exceção relacionada a um nome de 
variável errado.
"""

color = 12
try:
    print(color)
except NameError:
    print("Verifique o nome da variável")