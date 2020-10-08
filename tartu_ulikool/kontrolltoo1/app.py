#FAILI AVAMINE

failinimi =  input('Siesta faili nimi (andmed.txt): ') # küsime faili nimie

fail = open(failinimi, encoding = 'UTF-8') # avame faili

ringid = [] # koostame tühja järjendi faili andmete kogumiseks

for i in fail:
    ringid.append(float(i)) # andmete sisestamine järjendisse

fail.close()

#LISAANDMETE PÄRING
staadioniringi_pikkus = float(input('Sisestage staadioniringi pikkus meetrites: '))
norm = float(input('Sisestage norm meetrites: '))


#FUNKTSIOON ARVUTAMISEKS

def jooksu_pikkus_meetrites(staadioniringi_pikkus, joostud_ringid):
    return staadioniringi_pikkus * joostud_ringid

#VÄLJUND

kokku = 0

for el in ringid:
    
    tulemus = jooksu_pikkus_meetrites(staadioniringi_pikkus,el) #arvutame tulemuse
    kokku +=1
    
    if tulemus < norm:
        print('Jooksa jooksis ', tulemus, 'meetrit ja ei läbinud testi')
    else:
        print('Jooksa jooksis ', tulemus, 'meetrit ja läbis testi')

print('Kokku oli jooksjaid: ', kokku)
