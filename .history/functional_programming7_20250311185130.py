"""
Dependencies on external factors can make a function impure
"""

def hashtag():
    word = input()
    return "#" + word


##################################################

"""
Pure Function:
"""
def play_song(song):
    return "Playing " + song