"""
Você pode escolher não especificar o tipo de exceção, o que
permite o manuseio de quaisquer exceções que possam ocorrer.
Embora essa abordagem seja mais fácil, a desvantagem é que 
as mensagens de erro podem não ser tão claras e úteis.

"""
# Try except genérico:
product = "TV":
try:
    print(product)
except:
    print("Error, is not a product")