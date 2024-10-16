"""
Loop FOR:
SABEMOS quantas repetições teremos
NÃO precisa controlar iteração
"""

for i in range(3):
    print("Email sent")
    

"""
BREAK:
deve ser colocada DENTRO da instrução 'if' onde a condição é definida, garantindo
a identação adequada.
"""

music = ["Hello", "Hold the line"]
for i in music:
    if i == "Hello":
        print("Music found")
        break

prices = [35, 80, 16, 89, 95, 76]

for price in prices:
    if price < 90:
        print(price)


"""
CONTINUE:
Pula a iteração atual e continua a próxima quando uma certa condição é TRUE
"""
print()
ages = [13, 19, 22, 8]
for age in ages:
    if age < 18:
        continue
    print(age)
    
print()

animals = ["cat", "giraffe", "lion", "leopard", "mouse"]
for animal in animals:
  if animal[0] == "l":
    continue
  print(animal)