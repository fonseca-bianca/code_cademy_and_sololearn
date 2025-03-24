"""
Functions are a fundamental concept in programming, greatly
enhancing the efficiency and flexibility of your code. Up until
now, you've focused on defining and calling functions. However,
Python offers advanced techniques to make your code even more
powerful and adaptable.
In this lesson, we'll about decorators, special functions that
modify or enhance other functions

1 - Identify the functions with their scopes:
"""

# parent/outer function:
def greet(name):
    print("Hello, " + name)
    
    #child/inner function:
    def welcome():
        print("Welcome this site!")
        
        