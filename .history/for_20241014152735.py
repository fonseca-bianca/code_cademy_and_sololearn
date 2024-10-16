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
    if music == "Hello":
        print("Music found")
    break