"""
1 - Trate uma exceção causada por entrada do usuário INCORRETA
que está fora do intervalo da lista
"""

choice = int(input())
coffees = ["latte", "macchiato", "espresso"]
try:
    print(coffees[choice])
except IndexError:
    print("Escolha 0, 1 ou 2")