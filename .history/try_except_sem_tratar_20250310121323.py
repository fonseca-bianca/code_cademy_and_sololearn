"""
Quando você especifica apenas um tipo de exceção a ser 
tratada, outros tipos de exceções não serão cobertos. 
Se estas outras exceções ocorrerem, a execução do 
programa falhará.
Por exemplo, a execução do código abaixo falhará porque
a exceção que ele lança não é tratada.
"""

colors = ['Red', 'Yellow', 'Green']
try:
    #index error
    print(colors[10])
    
    #wrong exception
except NameError:
    print("Error")
    
#will not be executed
print("Happy holliday")

# Output:
# Traceback (most recent call last):
#   File "try_except_sem_tratar.py", line 77, in <module>
#     print(colors[10])
# IndexError: list index out of range