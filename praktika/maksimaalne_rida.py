"""
+ Küsib kasutajalt failinime
+ Pärib failist read
# Summerib read kokku
# Leiab suurima summaga rea numbri failis (algab 1st)
# Väljastab rea järjekorranumbri ekraanile
# Näide väljundist: Suurim summa on failis 2. real ja see on 99
"""

# KASUTAJA PÄRINGUD

failinimi = input('Sisestage failinimi: ')
fail = open(failinimi, encoding='UTF-8')


# ANDMETE VÕTMINE FAILIST

andmed = [] #read ühte järjendisse

for rida in fail:
    andmed.append(rida)

table = [] #iga rea jaoks oma järjend

for el in andmed:
    table.append(el.split())

# RIDADE SUMMEERIMINE TABELIS

summad = [] #siia paigutan kõik ridade summad

for n in range(len(table)): #saan kätte, kui mitu järjendit on tabelis
    x = 0
    for i in range(len(table[n])): #saan kätte igast järjendist tabelis elemendid
        x = x + int(table[n][i]) #liidan kokku
    
    summad.append(x) #lisan summad järjendisse
    

suurim_summa = summad.index(max(summad)) + 1

print("Summade nimekiri on järgmine:", summad)
print("Suurim summa on failis " + str(suurim_summa) + ". real ja see on " + str(max(summad)))
    
    



