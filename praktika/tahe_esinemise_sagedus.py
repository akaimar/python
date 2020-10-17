'''Koostada funktsioon symbolite_sagedus, mis võtab argumendiks sõne ja tagastab
sõnastiku, mis sisaldab selles sõnes esinevate tähemärkide esinemiste sagedusi.
Tagastatav sõnastik peab seega sisaldama kirjeid, kus võtmeteks on ühetähemärgilised
sõned (sümbolid) ja väärtusteks vastavate sõnede (sümbolite) esinemiste arv
argumendiks antud sõnes.

Pange tähele, et sümbolite alla käivad kõik pikkusega 1 sõned, mis argumendiks
antud sõnes sisalduvad, sh tühikud ja kirjavahemärgid. Samuti loetakse erinevateks
sümboliteks näiteks väike täht a ja suur täht A.

Kontrollitakse vaid funktsiooni definitsiooni, programmis seda rakendama ei pea.

symbolite_sagedus("suitsupääsuke")
{'s': 3, 'u': 3, 'i': 1, 't': 1, 'p': 1, 'ä': 2, 'k': 1, 'e': 1}
'''

# FUNKTSIOON
def symbolite_sagedus(sone):
    sonastik = {}
    # skännin läbi, mitu tähte on sõnes
    for i in range(len(sone)):
        sonastik[sone[i]] = sone.count(sone[i])
    return sonastik

# prindin ja kontrollin töökorda

kontroll = {
            "a1" : "Suitsupääsuke",
            "a2" : "Hommikul silmad on kinni ja huulil on naer",
            "a3" : "l@htek00d"
            }
        
for key in kontroll:
    print(symbolite_sagedus(kontroll[key]))
    

