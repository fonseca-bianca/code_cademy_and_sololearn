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