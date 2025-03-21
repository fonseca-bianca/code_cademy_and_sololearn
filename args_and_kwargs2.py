"""
If the number of arguments of your function is unknown and 
unpredictable, you can always use an iterable as an argument.
Here is an example of using a list as an argument.
"""

def total(numbers):
    result = 0
    # iterating over the list:
    for i in numbers:
        result += i
        # se colocasse o 'return' aq, ele iria executar APÓS a 1ª iteração --> output: 1
    return result # return só é executado DEPOIS q o 'for' termina --> output: 15
    
nums = [1,2,3,4,5]

print(total(nums))