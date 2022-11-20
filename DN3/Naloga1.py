#Napišite funkcijo, ki od uporabnika zahteva naj vnese svojo EMŠO število. Funkcija naj nato izpiše koliko let je uporabnik star 
# (upoštevamo samo letnico rojstva) in vrne število let (celoštevilska vrednost). EMŠO ima 13 številk XXXXyyyXXXXXXX. 5.,6.,7. 
# številka predstavljajo letnico rojstva (999 -> 1999 leto rojstva).
import datetime
datum = datetime.datetime.now()
def emso_leta_preracun():
    emso = ''
    while len(str(emso)) != 13:                 	            #Preverjanje dolžine emso (ker int odreže začetne ničle spustimo čez,
        emso = int(input("Vpišite EMSO: "))                     # tudi če je samo 12 znakov in dodamo 0 na začetek )
        if len(str(emso)) == 13 or len(str(emso)) == 12:
            break
    
    emso = str(emso).zfill(13)
    emso_s = []
    for x in str(emso):
        emso_s.append(int(x))

    dan = 0
    m_in_d = (datum.month * 100 + datum.day) - (emso_s[2] * 1000 + emso_s[3] * 100 + emso_s[0] * 10 + emso_s[1])
    if m_in_d < 0:              #Če upoštevamo tudi dan in mesec
        dan = 1

    leto = int(emso_s[4] * 100 + emso_s[5] * 10 + emso_s[6])
    print(leto)
    if leto < 100:
        starost = datum.year - (leto + 2000) - dan
    if leto > 100:
        starost = datum.year - (leto + 1000) - dan
    return starost


starost = emso_leta_preracun()
print("Star si " + str(starost) + " let.")
