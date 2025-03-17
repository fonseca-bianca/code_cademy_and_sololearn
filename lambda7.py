"""
Lambdas execute single, concise expressions. They are more 
limited than regular functions, which can have multiple lines
and actions, and are ideal for straightforward, simple operations
"""

lambda x, y: x * y

#########################################################

"""
You can provide arguments to lambda expressions on-the-fly
by adding them in parentheses immediately after the lambda 
function. The lambda expression should be also enclosed
in parentheses

OBS.: 
expressões lambda on-the-fly" são funções simples e anônimas 
que você cria diretamente no momento em que precisa delas, 
sem precisar defini-las com um nome usando def. Elas são 
chamadas de "on-the-fly" (ou "na hora") porque são criadas e 
usadas imediatamente, sem armazená-las em uma variável.
útil para operações rápidas e curtas

OBS.:
não são a melhor opção quando se trata de cód limpo e boas 
práticas de codificação
"""

res = (lambda x, y: x + y) (2,3)
print(res)
# output: 5