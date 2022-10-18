#Uporabnika zaprosite naj vnese neko celo število. To vrednost shranite v spremenljivko z imenom n in jo izpišite in izpišite njen tip.
#Nato to vrednost pretvorite v float vrednost. Dobljeno float vrednost shranite v spremenljivko n. Nato n izpišite in izpišite njen tip.

n = int(input("Vnesite celo število: "))
print("Število " + str(n) + " je tipa " + str(type(n)) + ".")

n = float(n)
print("Število " + str(n) + " je tipa " + str(type(n)) + ".")