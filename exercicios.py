# budget = 20
# print(budget + 10)

# price = 14
# discount = 0.2 * price
# final_price = price - discount
# print(final_price)

# items = 18
# boxes = 6
# print(items/boxes)

# start = 0
# end = 10
# while start < end:
#     start += 1
#     print(start)
    
# linhas = 2
# colunas = 2
 
# linha = 1
# while linha <= linhas:
#     coluna = 1
#     while coluna <= colunas:
#         print(linha, coluna)
#         coluna += 1
#     linha += 1
    
# score1 = int(input("Enter a score1: "))  
# score2 = int(input("Enter a score2: "))
# total_score = score1 + score2
# print(total_score)

# a = 14
# b = "km" --> gera erro, pois em Python NÃO é permitido concatenar string com int

# a = 14
# b = "km"
# print(str(a) + b) # tem q transformar o int em string, aí o Python consegue concatená-los
# print("14" + "km") # ou fazer a alteração do 14 para "14" direto no print


# cucumbers = 100
# num_people = 6
# whole_cucumbers_per_person = cucumbers / num_people
# print(whole_cucumbers_per_person)

# string_num = "7.5"
# print (float(string_num)) 


"""ambos vão imprimir a mesma coisa = 0 1 2 | 0 1 2
for i in range(3):
    print(i)
    
print("--")

for something in range(3):
    print(something)
"""


"""
for i in range(3):
    print(i < 1)
    # sendo i = 0:
        # 0 < 1 = True
    # sendo i = 1:
        # 1 < 1 = False
    # sendo i = 2:
        # 2 < 1 = False
"""

# for i in range(3):
#     print("First") # impresso 3 vzs
#     print("Second") # impresso 3 vzs

# for box in range(50):
#     print("Package A") # imprime 50 vzs
# print("Task complete") # imprime após completar 50 vzs, pois está fora do loop


# print("Spam"+"and"+"eggs") # imprime tudo grudado
# print("Spam "+"and "+"eggs") # imprime com espaços

"""
O str()método converte não strings em strings .
print ("The value of pi is around " + str(3.14))
"""

"""
O % operador após a string é usado para combinar uma string com variáveis. 
O % operador substituirá o %s na string pela variável string que vem depois dele.

Se você quiser imprimir uma variável que é um int, você pode “preenchê-la” 
com zeros usando %02d. 
O 0 (zero) significa “preencher com zeros”, o 2 significa preencher 
com 2 caracteres de largura, e o 'd' significa que o número é um int assinado
(pode ser positivo ou negativo).

name = "Alex"
quest = "Teaching Python"
color = "Blue"

print ("Ah, so your name is %s, your quest is %s, " \
"and your favorite color is %s." % (name, quest, color))
"""

"""substituição de strings para impressão de data no formato mm/dd/yyyy

from datetime import datetime
now = datetime.now()

print("%02d/%02d/%04d" % (now.month, now.day, now.year))
# vai imprimir o month/day/year
"""

bool_two = not 3**4 < 4**3
print(bool_two)