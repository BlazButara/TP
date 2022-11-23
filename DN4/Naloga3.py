#Namestite knjižnico requests in spišite funkcijo, ki za iskalni niz vrne html kodo rtvslo iskalnika novic 
# (https://www.rtvslo.si/iskalnik?q=iskalni niz).
import requests

def req():    
    r = requests.get('https://www.rtvslo.si/iskalnik?q=iskalni')
    print(r.text)


req()