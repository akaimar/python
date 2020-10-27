"""Koostada funktsioon yhisosa, mis võtab argumendiks kaks järjendit ja
tagastab uue järjendi, mis sisaldab ühekordselt neid elemente, mis
esinesid mõlemas sisendjärjendis. Tagastatav järjend peab sisaldama ainult
neid elemente, mis eelnevale tingimusele vastavad.

Kontrollitakse vaid funktsiooni definitsiooni, programmis seda rakendama ei pea.

Näited:
>yhisosa([1, 2], [2, 3])
[2]
>yhisosa(['ich', 'du', 'er', 'sie', 'es'], ['wir', 'ihr', 'sie', 'Sie'])
['sie']
"""

#koostada funktsioon yhisosa, milles on kaks argumenti

def yhisosa(a,b):

    a1, b1 = set(a), set(b) # sisend on järjend, selle teeme hulgaks "set"
    uus_jarjend = list(a1 & b1) #ühisosa tüüp on hulk, selle teeme järjendiks
    return uus_jarjend

#test
arg1 = ['ich', 'du', 'er', 'sie', 'es']
arg2 = ['wir', 'ihr', 'sie', 'Sie']
print(yhisosa(arg1, arg2))
