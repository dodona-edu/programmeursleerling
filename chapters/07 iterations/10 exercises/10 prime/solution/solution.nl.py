# getal inlezen
getal = int(input())

# bepalen of het getal een priemgetal is
priem = True
deler = 2
while priem and deler < getal:
    if not getal % deler:
        priem = False
    deler += 1

# resultaat uitschrijven
print(f'{getal} is {"" if priem else "g"}een priemgetal')
