def cube(number):
  return number * number * number # ou number ** 3 pra saber o cubo do valor

def by_three(number):
    if number % 3 == 0: # se o número for divisível por 3
        return cube(number) # então será retornado o seu resultado
    else:
        return False