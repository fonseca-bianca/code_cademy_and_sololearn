for x in range(200):
    print("Repeat")
print("Stop") # vai aparecer por último, depois de 'x' repetir 200 vzs
"""
se o 2º print estiver no mesmo alinhamento do 1º, então estará DENTRO do loop,
logo, será impresso 200 vzs tbm
"""

count = 1
while count < 10:
    print(count)