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
"""

res = (lambda x, y: x + y) (2,3)
print(res)