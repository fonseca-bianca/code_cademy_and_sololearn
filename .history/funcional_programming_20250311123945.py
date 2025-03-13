""" 
You can assign a function to a variable.
1 - Define the welcome() function and assign it to the greet variable
"""

def welcome(name):
    return "Welcome, " + name
greet = welcome
print(greet("Alice"))
# print(welcome("Alice"))

"""
Jeito 1: Atribui a função a uma variável (greet) e chama a função através dessa variável. Útil quando você quer reutilizar a função com diferentes nomes ou em diferentes contextos.

Jeito 2: Chama a função diretamente, sem atribuição intermediária. Mais simples e direto, ideal para chamadas únicas.
"""