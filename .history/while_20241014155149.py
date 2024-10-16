"""
Loop While:
quando NÃO sabemos QUANTAS repetições teremos
contador EVITA loop infinito
HÁ condição q precisa ser atendida
"""

place = 30
while place > 0:
    place -= 1
    print("Sale the ticket")
    

"""
while True:
significa que a condição do loop while é sempre verdadeira, 
fazendo com que ele seja executado infinitamente. Ele só vai parar quando 
a condição para a declaração break for atendida.
"""

while True:
    text = input()
    print(text)
    if text == "Stop":
        break
    
print()


hour = 1
while hour <= 10:
    if hour == 0:
        hour += 1
        continue
    print("Take coffee")
    hour += 1