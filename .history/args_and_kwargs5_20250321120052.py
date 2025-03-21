"""
1 - How many lines of output will this code produce?
"""

def display(*words):
    for item in words:
        print(item, end=" ")
    print('\n')
display("paper", "pen", "pencil")