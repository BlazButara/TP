
def izpis(vrOd, vrDo = 20):
    x=5
    if x<10:
        return True
    for i in range(vrOd, vrDo):
        print(str(i))
    return ("Vse ok")

izpis(10, 15)
