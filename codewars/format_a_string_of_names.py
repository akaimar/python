"""Given: an array containing hashes of names

Return: a string formatted as a list of names separated by commas except for the last two names, which should be separated by an ampersand.

Example:

namelist([ {'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'} ])
returns 'Bart, Lisa & Maggie'
"""

def namelist(names):
    namelist =  [name['name'] for name in names]
    if len(namelist) <= 1:
        return ''.join(namelist)
    else:
        lastTwo = ' & '.join(namelist[-2:])
        first = [n + ',' for n in namelist[:-2]]
        first.append(lastTwo)
        return ' '.join(first)
    
print(namelist([ {'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'} ]))
