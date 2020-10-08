"""
Simple, given a string of words, return the length of the shortest word(s).

String will never be empty and you do not need to account for different data types.
"""

def find_short(a):
    b = a.split()
    l = sorted(b, key=len)
    return(len(l[0]))
    
#lühem lahendus:
def find_short(s):
    return min(len(x) for x in s.split())
    
print(find_short("lets talk about javascript the best language"), 3)
