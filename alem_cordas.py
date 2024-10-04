def biggest_number(*args):
    print(max(args))
    return max(args)
    
def smallest_number(*args):
    print(min(args))
    return min(args)

def distance_from_zero(arg): # função personalizada
    print(abs(arg)) 
    # # abs(arg): função embutida retorna valor 
    # absoluto de um número recebido como argumento
    return abs(arg)

biggest_number(-10, -5, 5, 10)
smallest_number(-10, -5, 5, 10)
distance_from_zero(-10) # o valor abs --> absoluto de -10 é 10

"""Retorno:
10
-10
10
"""