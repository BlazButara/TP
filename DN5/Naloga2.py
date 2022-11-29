#Podobno kot v prvem primeru napišite funkcijo ki sprejme URL API-ja (vrača vrednosti v JSNO formatu) in vrnite vrednost kot slovar. 
#Še vedno izvedite validacijo.

import requests
import json
def get_api_data(url):
    r = requests.get(url)
    if r.status_code==200:              #Če je status 200 (OK) potem vrne html, drugače vrne False
        return json.loads(r.text)
    else :
        return False


# preizkusite na primerih
data = get_api_data("https://jsonplaceholder.typicode.com/todos/1")
print(data)

data = get_api_data("https://jsonplaceholder.typicode.com/nedala/nedala")
print(data)
