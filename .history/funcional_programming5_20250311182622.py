"""
An important concept in Funcional Programming is PURE FUNCTIONS.
A function is called 'pure' if it gives the same result every
time you give it the same inputs, and it doesn't affect anything
outside of the function. This makes them trustworthy and simpler
to understand.
"""
from nbconvert.exporters.tests.test_asciidoc import TestASCIIDocExporter
from IPython.extensions.tests.test_autoreload import TestAutoreload

def total(price, count):
    return price * count #price multiplied by count
# price = 2
# count = 3
# print(total(price, count)) #output: 6
""" 
print() é considerado um efeito colateral, pq modifica o estado  
do sistema
SEM 'return' a função NÃO retorna nada, ou seja, retorna 'none'
Funções puras devem retornar um valor explícito
"""