import random
r = random.randrange(0,30)
print(r)
for i in range(0, 5):
    x = input("Ugani število:")
    x= int(x)

    if x<r:
        print("Število je večje!")

    elif x>r:
        print("Število je manjše!")

    else:
        print("Bravo!")
        break

