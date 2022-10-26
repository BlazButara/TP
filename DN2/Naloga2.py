#Iz sledečega lista our_list odstranite vrednost, ki se nahaja na indexu 4. Vrednost dodajte v dictionary pod ključ d. 
#Nato iz dictionary our_dict pridobite vse vrednosti. Te vrednosti shranite v nov tuple in novonastali tuple primerjajte 
# ali je enak podanemu tuple-u our_tuple.


import string


our_list = [1,2,3,4,5,6,7]
our_dict = {
    "a": 2,
    "b": 5,
    "c": 8,
    "d": 12,
    "e": 357,
    "f": 12
}
our_tuple = (357, 12, 12, 8, 5, 2, 2)

d = our_list[4]
our_list.remove(4)
our_dict["d"] = d
print(our_dict)
nov_tuple=list(our_dict.values())   #zapis samo vrednosti iz our_dict v nov_tuple
print(our_tuple == nov_tuple)       #primerjava
