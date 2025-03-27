"""
Você pode ter vários blocos except para lidar especificamente
com cada possível exceção. Como uma boa prática, 
recomenda-se emitir uma mensagem definitiva para cada 
tipo de exceção tratada.
"""

colors = ['Red', 'Yellow', 'Green']
try:
    print(colors[10])
except IndexError:
    print("Out of range")
except NameError:
    print("Variable is not defined")
    
print("Happy shopping")