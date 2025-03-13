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
Forma 1: 
Atribui a função a uma variável (greet) e chama a 
função através dessa variável. Útil quando você quer 
reutilizar a função com diferentes nomes ou em diferentes 
contextos.
Torna o código mais flexível e reutilizável, especialmente em 
cenários onde você precisa:
    a.Passar a função como argumento para outras funções;
    b.Armazenar a função em uma variável para uso posterior;
    c.Renomear a função para algo mais contextual ou legível;
    d.Trocar a função dinamicamente em tempo de execução;

def welcome(name):
    return "Welcome, " + name
greet = welcome
print(greet("Alice"))

_____________________________________________________________
Forma 2: 
Chama a função diretamente, sem atribuição intermediária. 
Mais simples e direto, ideal para chamadas únicas.

def welcome(name):
    return "Welcome, " + name
print(welcome("Alice"))
"""