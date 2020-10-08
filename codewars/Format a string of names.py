#Given: an array containing hashes of names
#Return: a string formatted as a list of names separated by commas except for
#the last two names, which should be separated by an hashes.
#namelist([ {'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'} ])
# returns 'Bart, Lisa & Maggie'
#namelist = [ {'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'}, {'name': 'Aimar'} ]

def namelist(names):
    namelist = [name['name'] for name in names]
    if len(namelist) <=1:
      return ''.join(namelist)
    else:
      nimed = []
      for i in range(len(names)):
          nimed.append(names[i]['name'])
      p = ', '.join(nimed[:-2])
      r = ' & '.join(nimed[-2:])
      print(p + ', ' + r)
      return p,r

def namelist(names):
  if len(names) < 1:
    return ''
  if len(names) >=1:
    return

"""
###Codewars alternative solution
def namelist(names):
    namelist =  [name['name'] for name in names]
    if len(namelist) <= 1:
      return ''.join(namelist)
    else:
      lastTwo = ' & '.join(namelist[-2:])
      first = [n + ',' for n in namelist[:-2]]
      first.append(lastTwo)
      print(' '.join(first))
      return ' '.join(first)
"""

##namelist([ {'name': 'Bart'} ])   
namelist([ {'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Aimar'}, {'name': 'Peeter'}, {'name': 'Maggie'}, {'name': 'Aimar'} ])


[name["name"] for name in names]
