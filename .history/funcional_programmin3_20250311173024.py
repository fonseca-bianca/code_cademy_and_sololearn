"""
Functiond can take other functions as arguments
"""
def welcome(name):
    return "Welcome, " + name

def process_user(name, func):
    return func(name)

print(process_user("Alice", welcome))
#output: Welcome, Alice

###################################################

#função order: retorna uma mensagem sobre o prato
def order(dish):
    return "Your order: " + dish

# função process_order: chama uma função passada como argumento "func" e imprime o resultado
def process_order(dish, func):
    print(func(dish))
    
process_order("Spaghetti", order)

# O valor "Spaghetti" é passado para o parâmetro dish.
# A função order é passada para o parâmetro func.
    