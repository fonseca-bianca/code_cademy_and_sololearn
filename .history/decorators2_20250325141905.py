"""
1 - What is the output of this code?
"""
def order():
    def prepare(): # função nested (aninhada): está DENTRO da função 'order()'
        return "Your meal is being prepared!"
    status = prepare()
    return status # função 'order()' retorna o valor da variável 'status'

print(order()) # 'order()' executa função nested 'prepare()' e retorna a string contida nessa
# output: "Your meal is being prepared!"