#Uporabite knjižnico math in za spišite funkcijo, ki za poljubno polje števil vrne:
#    najmanjši element,
#    največji element
#    povprečje in
#    element polja, ki je najbližje povrečju.
import math
import statistics
data = [41970, 40721, 41197, 41137, 43033]

print(min(data))                                                                        #Najmanjši element
print(max(data))                                                                        #Največji element
print(statistics.mean(data))                                                            #Povprečje
print(min(data, key=(lambda vrednosti : abs(vrednosti - statistics.mean(data)))))       #Element polja, ki je najbližje povprečju