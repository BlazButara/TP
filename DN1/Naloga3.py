#Uporabnika vprašajte za 3 celoštevilske vrednosti in jih izpišite s pomočjo print() in type(). 
#V eni vrstici preverite ali je druga vrednost enaka prvi in ali je tretja vrednost manjša ali enaka prvi.

x = int(input("Vnesite prvo celo število: "))
y = int(input("Vnesite drugo celo število: "))
z = int(input("Vnesite tretje celo število: "))
print()
print("Prvo število " + str(x) + " tipa " + str(type(x)) + ", drugo število " + str(y) + " tipa " + str(type(x)) + " in tretje število " + str(z) + " tipa " + str(type(x)))

print()
if x==y and x>=z:
    print("Druga vrednost je enaka prvi in tretja vrednost je manjša ali enaka prvi.")
else :
    print("Števila ne ustrezajo pogoju.")