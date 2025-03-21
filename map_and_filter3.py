"""
The map() function requires the first argumento to be a function
and the second argument to be an iterable.
1 - The code below has a mistake. Can you fix it?
"""

exam_scores = [85, 62, 95, 40, 78]
def is_passing(score):
    return score >= 70

# status = list(map(exam_scores, is_passing)) <-- ERRADA

status = list(map(is_passing, exam_scores))
# map(function, iterable)

print(status)

# output: [True, False, True, False, True]

"""
status: é uma variável que armazena o resultado da expressão 
list(map(is_passing, exam_scores)).

list(): é uma função que converte o objeto map em uma lista.

map(): é uma função que aplica a função is_passing a cada 
elemento do iterável exam_scores.
"""