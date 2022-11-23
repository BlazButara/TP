#Z pomočjo knjižnice json pretvorite spodnji slovar podatki v JSON besedilo.
import json
podatki = {
  "name": "John",
  "age": 30,
  "city": "New York"
}

json_podatki = json.dumps(podatki) 
print(json_podatki)