#Poiščite vsa praštevila med 1 in 50.

print("Praštevila med 1 in 50 so: ")
for x in range(0, 50):
   if x > 1:
       for i in range(2, x):
           if (x % i) == 0:
               break
       else:
           print(x, end = "  ")