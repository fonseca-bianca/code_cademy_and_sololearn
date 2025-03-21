"""
The map() function applies a specified function to every 
element in an iterable, like lists or tuples. It produces a 
result that can be transformed into a list using the list() 
function for easy viewing or further use.
"""

# list of names in various cases:
names = ["alice", "bob", "CHARLIE", "DavID", "EDwArD"]

# function to capitalize each name:
def captalize(name):
    return name.capitalize()

# using map() function to apply the capitalization to each name:
capitalized = map(capitalize, names)

# converting map object to a list:
capitalized = list(capitalized)

print(capitalized)