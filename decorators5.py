"""
Complete the wrapper() function so that ir displays a message 
after calling the original function

"""

def light_decorator(func):
    def wrapper():
        result = func()
        print("Turning off the lights...")
        return result
    return wrapper


"""
1.func não é a função wrapper:
func é o parâmetro que recebe a função decorada (a função que você passa para light_decorator).
No exemplo, se você fizer @light_decorator em uma função como party(), então func será a função party.

2.result = func():
Aqui, func() chama a função original (por exemplo, party()).
O resultado dessa chamada é armazenado em result.

3.return result:
Dentro de wrapper, return result retorna o resultado da função original (party()), para que ele não seja perdido.

4.return wrapper:
A função light_decorator retorna a função wrapper, que é a função modificada (com o código extra de "Turning off the lights...").
"""