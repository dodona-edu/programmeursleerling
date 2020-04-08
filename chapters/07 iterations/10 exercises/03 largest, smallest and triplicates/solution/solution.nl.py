# eerste getal inlezen
getal = int(input())

# statistieken initialiseren
grootste = getal
kleinste = getal
drievouden = 0 if getal % 3 else 1

# andere getallen inlezen en verwerken
for _ in range(9):

    # volgende getal inlezen
    getal = int(input())

    # grootste bijwerken
    if getal > grootste:
        grootste = getal

    # kleinste bijwerken
    if getal < kleinste:
        kleinste = getal

    # drievouden bijwerken
    if not getal % 3:
        drievouden += 1

# statistieken uitschrijven
print(f'grootste: {grootste}')
print(f'kleinste: {kleinste}')
print(f'drievouden: {drievouden}')
