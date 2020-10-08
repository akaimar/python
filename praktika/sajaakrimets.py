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