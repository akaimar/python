"""Koostada funktsioon leidub_anagramm, mis võtab argumendiks sõnede maatriksi
kahemõõtmelise järjendina, milles sõned koosnevad vaid tähtedest a, b, c ja d.
Funktsioon tagastab tõeväärtuse vastavalt sellele, kas selles maatriksis leidub element,
mis on sellise sõne anagramm, mis on saadud temast vahetult vasakul ja vahetult paremal
olevate sõnede kokkukirjutamise teel.

Kui vasakul või paremal elementi ei leidu, siis tuleb seda arvestada tühja sõnena.

Kontrollitakse vaid funktsiooni definitsiooni, programmis seda rakendama ei pea."""

#Löön maatriksi laiali, sordin ja võrdlen sisusid

def leidub_anagramm(sisend):
    for i in range(len(sisend)):
        for j in range(len(sisend[i])):
            if j == 0:
                esimene = ""
            else:
                esimene = sisend[i][j-1]
            if j == len(sisend[i])-1:
                viimane = ""
            else:
                viimane = sisend[i][j+1]
            if sorted(sisend[i][j]) == sorted(esimene+viimane):
                return True             
    return False             
                
        
    
ag1 = [['ab', 'cad', 'cd'], ['abd', 'a', 'bd']] #false
ag2 = [['ab', 'cad', 'cd'], ['a', 'bad', 'bd']] #true

leidub_anagramm(ag1)
leidub_anagramm(ag1)