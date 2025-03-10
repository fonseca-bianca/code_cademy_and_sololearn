"""
Você pode usar a instrução finally para realizar uma 
operação após o bloco try/except, não importa se ocorreu 
uma exceção ou não.
"""

prices = [559, 879, "n/a", 349]
try:
    print(sum(prices))
except TypeError:
    print("Check the prices")
finally:
    print("Need help? Contact us.")