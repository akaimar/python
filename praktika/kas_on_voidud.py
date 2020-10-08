"""
Järgnevad funktsioonid võtavad argumendiks 5 x 5 maatriksi, mis tähistab Bingo Loto
tabelit ning milles iga element on kas täisarv lõigust 1 - 75 või suur trükitäht X.
Täht X sümboliseerib seda, et vastav arv on mängus juba loositud.

1. Koostada funktsioon voitis_nurkademangu, mis tagastab tõeväärtuse vastavalt sellele,
kas see mänguväli on võitnud nurkademängu: kõik mänguvälja nurgad on loositud.

2. Koostada funktsioon voitis_diagonaalidemangu, mis tagastab tõeväärtuse vastavalt
sellele, kas see mänguväli on võitnud diagonaalidemängu: kõik mänguvälja diagonaalidel
olevad arvud on loositud.

Selleks koostada ja kasutada kahte abifunktsiooni:
Funktsioon x_peadiagonaalil, mis võtab argumendiks mänguvälja ja tagastab selle
peadiagonaalil olevate X arvu.

Funktsioon x_korvaldiagonaalil, mis võtab argumendiks mänguvälja ja tagastab selle
kõrvaldiagonaalil olevate X arvu.

3. Koostada funktsioon voitis_taismangu, mis tagastab tõeväärtuse vastavalt sellele,
kas see mänguväli on võitnud täismängu: kõik mänguvälja arvud on loositud.

Bingo Loto reeglitega saab täpsemalt tutvuda siin.

"""
# NURKADEMÄNG
# Nurgad table[0][0], table[0][4], table[5][0], table[4]

def voitis_nurkademangu(table):
    if table[0][0] == "X" and table[0][4] == "X" and table[4][0] == "X" and table[4][4] == "X":
        return True
    else:
        return False
    
# DIAGONAALIDEMÄNG
# on vaja välja võtta tabelist järjendid ja igas järjendis 1 element edasi
# peadiagonaal

def x_peadiagonaalil(table):
    indeks = 0
    peadiagonaal = []
    for i in range(5):
        if table[i][indeks] == "X":
            peadiagonaal.append(table[i][indeks]) #lisan kõik X-id järjendisse
        indeks += 1
    return len(peadiagonaal)

def x_korvaldiagonaalil(table):
    indeks = 0
    korvaldiagonaal = []
    for i in range(5):
        if table[i][4-indeks] == "X":
            korvaldiagonaal.append(table[i][4-indeks])
        indeks += 1
    return len(korvaldiagonaal)
    
def voitis_diagonaalidemangu(table):
    if x_peadiagonaalil(table) == 5 and x_korvaldiagonaalil(table) == 5:
        return True
    else:
        return False
    
# TÄISMÄNG
def voitis_taismangu(table):
    taismang = [] 
    for i in range(len(table)):
        for j in range(len(table[i])):
            if table[i][j] == "X":
                taismang.append(table[i][j]) 
    if len(taismang) == 25:
        return True
    else:
        return False

table1 = [[1, 30, 34, 55, 1],
         [10, 16, 40, 50, 67],
         [5, 20, 38, 48, 61],
         [4, 26, 43, 49, 70],
         [15, 17, 33, 51, 66]]

table2 = [["X", 30, 34, 55, "X"],
         [10, 16, 40, 50, 67],
         [5, 20, 38, 48, 61],
         [4, 26, 43, 49, 70],
         ["X", 17, 33, 51, "X"]]

table3 = [["X", 30, 34, 55, "X"],
         [10, "X", 40, "X", 67],
         [5, 20, "X", 48, 61],
         [4, "X", 43, "X", 70],
         ["X", 17, 33, 51, "X"]]

table4 = [["X", "X", "X", "X", "X"],
         ["X", "X", "X", "X", "X"],
         ["X", "X", "X", "X", "X"],
         ["X", "X", "X", "X", "X"],
         ["X", "X", "X", "X", "X"]]

sisend = table4
print(voitis_nurkademangu(sisend))
print(voitis_diagonaalidemangu(sisend))
print(voitis_taismangu(sisend))
