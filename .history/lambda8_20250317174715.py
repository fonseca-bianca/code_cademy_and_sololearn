"""
The power of lambda is better shown when you use them as an 
anonymous function inside another function
(função anônima dentro de outra função). Say you have a 
function definition that takes one argument, and that argument
will be multiplied with an unknown number:
"""

def mult(n):
    return lambda a: a * n

doubler = mult(2)
tripler = mult(3)

print(doubler(5)) # output: 10
print(tripler(5)) # output: 15