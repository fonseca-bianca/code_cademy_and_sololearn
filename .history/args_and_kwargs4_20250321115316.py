"""
You need to use the unpacking operator * before args. This 
operator informs Python that the argument is an iterable and 
should be unpacked (desempacotar) to receive its values as 
individual arguments.
"""

# ex.:
# def total(*args):

"""
Note that args is just a name. You’re not required to use the
name args. You can choose any name that you prefer
"""

def total(*prices):
    result = 0
    for arg in prices:
        result += arg
    return result

print(total(1,2,3,4,5)) # output: 15
print(total(1,2,3,4,5,6,7)) # output: 28
print(total(1,2,3)) # output: 6