#Iz danega dictionary-ja d izpišite vse ključe, katerih vrednost vsebuje črko r ali veliko tiskano črko R.
d = {
    "mačka": "Micka",
    "pes": "Fido",
    "volk": "Rex",
    "medved": "Žan",
    "slon": "Jan",
    "žirafa": "Helga",
    "lev": "Gašper",
    "tiger": "Anže",
    "papagaj": "Črt",
    "ribica": "Elena",
    "krokodil": "Kasper",
    "zajec": "Lars",
    "kamela": "Manca" 
}

for kljuc, vrednost in d.items():
    if(("r" in vrednost) or ("R" in vrednost)):
        print(kljuc)