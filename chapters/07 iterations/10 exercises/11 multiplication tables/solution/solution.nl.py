# getal inlezen
getal = int(input())

# eerste rij uitschrijven
breedte = len(str(getal))
rij = f'{"":{breedte}s} |'
for m in range(1, getal + 1):
    breedte = len(str(m * getal))
    rij += f' {m:{breedte}d}'
print(rij)

# rij van streepjes uitschrijven
print('-' * len(rij))

# overige rijen uitschrijven
for n in range(1, getal + 1):
    breedte = len(str(getal))
    rij = f'{n:{breedte}d} |'
    for m in range(1, getal + 1):
        breedte = len(str(m * getal))
        rij += f' {m * n:{breedte}d}'
    print(rij)
