"""
1 - How many lines of output will this code produce?
"""

def display(*words):
    for item in words:
        print(item)
        # print(item, end=" "): vai imprimir todos os itens numa ÚNICA linha
display("paper", "pen", "pencil")
# output: 
""" 
O código imprime 3 linhas pq o 'for' itera sobre cada 
elemento da tupla 'words' e chama 'print' para cada um.
"""

