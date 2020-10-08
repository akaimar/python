# Fail: saja_aakri_mets_andmed.txt

#1 aaker = 0,4047 ha

#Omanik tahab teada, mitu tihumeetrit metsa aastas teatud suurusest
#suuremates metsatükkides juurde kasvab.

"""Koostada funktsioon juurdekasv, mis
võtab argumentideks metsatüki pindala (ujukomaarv aakrites) ja metsa aastase
juurdekasvu hektari kohta (ujukomaarv), tagastab selle pindalaga metsatüki
aastase juurdekasvu ümardatuna sajandikeni.

Arvutamise vihje: [1]

Koostada programm, mis

küsib kasutajalt
failinime (failis on eraldi ridadel metsatükkide pindalad aakrites);

vastava puuliigi aastase juurdekasvu hektari kohta tihumeetrites (ujukomaarv);

piiri, mitmest aakrist suuremad metsatükid arvesse võtta (ujukomaarv);

loeb failist metsatükkide pindalad;

arvutab (funktsiooni juurdekasv abil) ja väljastab metsatüki aastase juurdekasvu, kui selle metsatüki pindala on sisestatud piirist suurem;

väljastab teate “Metsatükki ei võeta arvesse”, kui metsatüki pindala ei ole sisestatud piirist suurem;

väljastab lõpuks ekraanile, mitme metsatüki juurdekasv arvutati."""

# Arvutamiseks võib kasutada valemit: (metsatüki juurdekasv) =
#(metsatüki pindala aakrites) * 0.4047 * (aastane juurdekasv)

''' ADNMED FAILIS '''

failinimi = input('Sisesta faili nimi (andmed.txt): ') #küsime faili nime

pindalad = [] #teeme tühja listi

fail = open(failinimi, encoding = 'UTF-8') #avame faili

for rida in fail: #teeme tsükli failidest ridade lugemiseks
    pindalad.append(float(rida)) #lisame pindalade järjendisse
    
fail.close()

''' FUNKTSIOON ARVUTAMISEKS '''

kasv = float(input("Sisestage aastene juurde kasv aastas hetkari kohta tihumeetrit: "))
piir = float(input("Sisesta piiri, mitmest aakrist suuremad metsatükid arvesse võtta: "))

def juurdekasv(pindala, juurdekasv): 
    #tagastab metsatüki aastase juurdekasvu ümardatuna sajandikeni
    return round(pindala * 0.4047 * juurdekasv,2)

kokku = 0

for el in pindalad:
    if el < piir:
        print(el, 'seda metsatükki ei võeta arvesse')
    else:
        print("Metsatüki aastane juurdekasv on", juurdekasv(el,kasv))
        kokku += 1
        
print("Arvutati ", kokku, " metsatüki juurdekasv")
