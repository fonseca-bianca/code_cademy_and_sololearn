"""
KWARGS:
keyword arguments = "argumentos nomeados"
Args allows (*args) you to provide any number of arguments without 
the need to create a list before calling the function each 
time.
"""

def total(*args):
    result = 0
    for arg in args:
        result += arg
    return result # espera encerrar todo o loop for

print(total(1,2,3,4,5)) 
print(total(1,2,3,4,5,6,7))
print(total(1,2,3))
