"""
Para lidar com um tipo específico de exceção, você precisa especificá-lo no 
bloco except.
1 - Complete o código para lidar com uma exceção relacionada a um nome de 
variável errado.
"""

color = "Green"
try:
    print(color)
except NameError:
    print("Verifique o nome da variável")
    
# Output:
#     print(colorr)
#     "Verifique o nome da variável"