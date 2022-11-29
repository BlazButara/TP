#Dopolnite spodnjo funkcijo, ki sprejeme kot parameter URL spletne strani, vrne pa HTML kodo strani v tekstovnem formatu. 
#Uporabite knjižnico request. Po prejemu odgovora preverite ali je status koda enaka 200 (v tem primeru vrnenmo HTML kodo). 
#V vseh drugih primerih vrnemo vrednost False.

import requests
def get_html(url):
    r = requests.get(url)
    if r.status_code==200:              #Če je status 200 (OK) potem vrne html, drugače vrne False
        return r.text
    else :
        return False


# preizkusite na primerih
page = get_html("https://example.com/")
print(page)

page = get_html("http://example.com/neobstaja")
print(page)