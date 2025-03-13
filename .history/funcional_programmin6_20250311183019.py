"""
The function is impure if it depends on any external state 
that it modifies or that affects its output. This includes 
changing variables, or altering input arguments. Such 
dependencies make the function's behavior unpredictable and 
dependent on the context in which it's run.
"""

product = ['pen', 'scissors', 'paper']

def add_item(product, item):
    product.append(item)