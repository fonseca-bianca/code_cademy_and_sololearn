def distance_from_zero(arg):
    if type(arg) == int or type(arg) == float:
        return abs(arg)
    return "Nope"

# Exemplo de chamada da função com um número
numero = -15
resultado = distance_from_zero(numero)
print(resultado)