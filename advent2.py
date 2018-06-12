#### RINGE ####

import math


x=49

sqrt = math.sqrt(x)
n = math.ceil(sqrt)
if n % 2 == 0:
    n += 1

ring_anzahl = math.floor(n / 2)
print("ringnummer: ",ring_anzahl)

n_groesse_einer_spalte = ring_anzahl *2 +1

maxim = int(n_groesse_einer_spalte*n_groesse_einer_spalte)
print("größte zahl: ", maxim)


b = maxim
li_ecken = [b]

for a in range(3):
    ecken = b - (n_groesse_einer_spalte - 1)
    b = ecken
    li_ecken.append(b)

print(li_ecken)

v_diff = []
for y in li_ecken:
    diff = y - x
    v_diff.append(diff)


b_diff = []
for a in range(len(v_diff)):
    b = int(math.fabs(v_diff[a]))
    b_diff.append(b)

for a in range(len(b_diff)):
    for speicher in range(a, len(b_diff)):
        if(b_diff[a] > b_diff[speicher]):
            b_diff[a], b_diff[speicher] = b_diff[speicher], b_diff[a]



mini = b_diff[0]
mitteldiff = int(b_diff[1]/2)
print(b_diff)
print( mini)


print(mitteldiff)

zur_mitte= mini - mitteldiff

print(zur_mitte)


