""" 
A função sum() só funciona com iteráveis que contêm tipos de dados 
numéricos (int ou float)
"""
prices = [250, 300, "240", 400]
total = sum(prices)
print(total)

# Output ERROR messages:
# Traceback (most recent call last):
#   File "prices.py", line 44, in <module>
#     total = sum(prices)