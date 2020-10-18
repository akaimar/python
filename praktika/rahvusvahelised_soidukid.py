"""
Sõiduki registreerimismärgile või riigi tunnusmärgile on tavaliselt märgitud riigi tähis 1-3-tähelise lühendina. Eesti puhul on lühendiks näiteks EST. Piirivalvel on andmebaas eri riikide tähistest tekstifailis nii, et faili igal real on tühikuga eraldatud riigi tähis ja selle riigi nimi.

Väljavõte riigitähiste failist:
ER Eritrea
FIN Soome
F Prantsusmaa
H Ungari
LT Leedu
EST Eesti
S Rootsi


Koostada funktsioon failist_sonastik, mis võtab argumendiks andmebaasi faili nime ning tagastab vastava faili sisu põhjal sõnastiku, kus võtmeteks on riigitähised (sõned) ja väärtusteks riikide nimed (sõned).

Koostada funktsioon tahised_nimedeks, mis võtab argumendiks järjendi riikide tähistest (sõned) ja eelmise funktsiooni poolt koostatud sõnastiku ning tagastab järjendi vastavate riikide nimedest. Kui mõni tähis argumendiks antud järjendis on tundmatu, siis selle riigi nimi tuleb asendada tagastatavas järjendis väärtusega None.

Rakendada funktsioone sobivalt programmis, mis
küsib kasutajalt andmebaasi faili nime,
küsib kasutajalt sõne, mis koosneb tühikutega eraldatud piiri ületanud sõidukite riikide tähistest,
väljastab sõidukite päritolumaade nimed üksteise alla. Kui mõni riigitähis on tundmatu, siis väljastada selle riigi nime asemel Tundmatu maa.

>>> failist_sonastik("aasia.txt")
{'J': 'Jaapan', 'SGP': 'Singapur', 'IND': 'India', 'LAO': 'Laos', 'T': 'Tai', 'CHN': 'Hiina'}

>>> tahised_nimedeks(['FIN', 'RUS', 'CHN', 'IND', 'F', 'LAO'], failist_sonastik("aasia.txt"))
[None, None, 'Hiina', 'India', None, 'Laos']

"""


# Teen failist sõnastiku
def failist_sonastik(sisend):
    andmed = {}
    f = open(sisend, "r")
    for rida in f:
        read = rida.split()
        andmed[read[0]] = read[1]
    f.close()
    return andmed

# Teen sisendist järjendi ja kontrollin vastu sõnastikku

def tahised_nimedeks(tahised, andmed):
    jarjend = [] #tühi järjend, mille väljastame
    for el in tahised:
        if el in andmed:
            jarjend.append(andmed[el])
        else:
            jarjend.append(None)
    return jarjend


# Küsin kasutaja sisendi

failinimi = input("Sisesta andmebaasi faili nimi (aasia.txt, lounaameerika.txt): ")
tahised_input = input("Sisesta tühikutega eraldatud piiri ületanud sõidukite riikide tähised: ").split() # tahised_input = FIN RA CHN IND F LAO

# Annan väljundi

for i in tahised_nimedeks(tahised_input, failist_sonastik(failinimi)):
        if i == None:
            print("Tundmatu maa")
        else:
            print(i)
