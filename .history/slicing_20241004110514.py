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

animals = ["cat", "dog", "bird", "cow"]
print(animals[0:3])
# exibirá os 3 primeiros valores da lista

animals = ["cat", "dog", "bird", "cow"]
print(animals[1:4])
# exibirá os 3 últimos valores da lista


vehicle = "airplane"
print(vehicle[3:8])