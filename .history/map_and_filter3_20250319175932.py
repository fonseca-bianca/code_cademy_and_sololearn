"""
The map() function requires the first argumento to be a function
and the second argument to be an iterable.
1 - The code below has a mistaje. Can you fix it?
"""

exam_scores = [85, 62, 95, 40, 78]
def is_passing(score):
    return score >= 70

status = list(map(exam_scores, is_passing))
# map(function, iterable)

print(status)