"""  
strings são imutáveis, ou seja, uma vez criada, não é possível modificar 
diretamente seus caracteres por meio de atribuição de índice.
Pra alterar uma string, seria necessário criar uma nova
O exemplo abaixo irá retornar um erro.
"""

word = "car"
word[2] = "t"

# Lists are mutable
words = ["car", "dog", "bird"]
words[0] = "cat"
print(words)

x = "arctic"
print(x[2] + x[0] + x[3])