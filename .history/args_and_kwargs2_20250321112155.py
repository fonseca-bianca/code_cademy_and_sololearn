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
        
    return result
    
nums = [1,2,3,4,5]

print(total(nums))