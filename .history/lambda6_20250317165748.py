""""
Lambda expressions can take multiple arguments separated
by commas
"""

lambda width, height: width * height

# arguments: width, height
# expression: width * height

##########################################################

x = lambda price, count: price * count
print(x(2,10))

# 'x' = é uma função anônima q usa 'lambda' como palavra-chave