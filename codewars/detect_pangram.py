"""
A pangram is a sentence that contains every single letter of the alphabet at least once. For example, the sentence "The quick brown fox jumps over the lazy dog" is a pangram, because it uses the letters A-Z at least once (case is irrelevant).

Given a string, detect whether or not it is a pangram. Return True if it is, False if not. Ignore numbers and punctuation.
"""

def is_pangram(pangram):
    abc = 'abcdefghijklmnopqrstuvwxyz' #alphabet
    p = ''.join(e for e in pangram if e.isalnum()).lower() #removes special chars
    p1 = ''.join(set(p)) #removes dublicates
    p2 = ''.join([i for i in p1 if not i.isdigit()])
    p3 = ''.join(sorted(p2)) #sorting
    return(p3 == abc)
    
#profide lahendus:

""" import string

def is_pangram(s):
    return set(string.lowercase) <= set(s.lower())
"""
    
pangram = "The quick, brown fox jumps over the lazy dog!"
print(is_pangram(pangram), True)
