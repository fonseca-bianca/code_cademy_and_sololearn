"""
1 - Identify the arguments with their types
"""

prices = [25.99, 14.50, 8.75, 19.95]
def discount(price):
    discounted_price = price * 0.9
    return discounted_price

discounted_price = list(map(discount, prices))  
print(discounted_price)