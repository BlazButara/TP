#Napišite funkcijo, ki sprejme nabor podatkov v obliki dictionary-ja data in vrne največjo vrednost vsakega ključa 
# (vrednosti so v obliki lista).

data = {"prices": [41970, 40721, 41197, 41137, 43033],
       "volume": [49135346712, 50768369805, 47472016405, 34809039137, 38700661463]}

def najvecja_vrednost(podatki): 
    izpis = []

    izpis.append(min(data[list(data)[0]]))    
    izpis.append(max(data[list(data)[1]]))
    
    return izpis


vrednosti = najvecja_vrednost(data)
print(vrednosti)