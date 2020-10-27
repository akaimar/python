"""

Kui esimeses (võtmete) järjendis on korduvaid elemente, siis sõnastikku tuleb panna neist
viimane koos vastava elemendiga väärtuste järjendist. Teisisõnu kirjutavad sama võtmega
kirjed eelnevaid väärtuseid üle nagu sõnastiku puhul ikka kombeks.

Näited:
>>> listid_sonastikuks([1, 2], [3, 4])
{1: 3, 2: 4}

>>> listid_sonastikuks(['ATI', 'KAMA'], ['Arvutiteaduse instituut', 'Kasutatav masintõlge'])
{'KAMA': 'Kasutatav masintõlge', 'ATI': 'Arvutiteaduse instituut'}

"""

def listid_sonastikuks(a,b):
    võtmed = list(a)
    väärtused = list(b)
    
    sonastik = {}
    
    #võtame võtmed ja leiame vastava väärtuse
    for i in range(len(võtmed)):
        sonastik[võtmed[i]] = väärtused[i]
    
    return sonastik
    
#KONTROLL

arg1 = ['ATI', 'ATI', 'KAMA']
arg2 = ['Butafooria', 'Arvutiteaduse instituut', 'Kasutatav masintõlge']

arg3 = [0, 1, 0]
arg4 = ['a', 'b', 'c']

arg5 = [1, 2]
arg6 = [3, 4]

print(listid_sonastikuks(arg1, arg2))
print(listid_sonastikuks(arg3, arg4))
print(listid_sonastikuks(arg5, arg6))

