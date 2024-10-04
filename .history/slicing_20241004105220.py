"""
SLICING/FATIAMENTO: permite que você extraia uma parte de uma lista.
Os índices de início e parada são separados por dois pontos (:)
O índice inicial é inclusivo. 
O índice final é exclusivo.
"""

animals = ["cat", "dog", "bird", "cow", "pig", "horse"]
print(animals[1:4]) 
# começará no 'cat'[1] e vai terminar na 'cow'[4]

animals = ["cat", "dog", "bird", "cow", "pig", "horse"]
print(animals[0:2]) 
# vai até 'dog'[1], pq 'bird'[2] é excluído