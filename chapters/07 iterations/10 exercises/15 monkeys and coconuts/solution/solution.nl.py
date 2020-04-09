# aantal piraten inlezen
piraten = int(input())

# minimaal aantal kokosnoten bepalen
kokosnoten = 0
while True:
    kokosnoten += 1
    stapel = kokosnoten
    for i in range(piraten):
        if stapel % piraten != 1:
            break
        stapel = (piraten - 1) * int((stapel - 1) / piraten)
    if stapel % piraten == 1:
        break

# minimaal aantal kokosnoten uitschrijven
print(kokosnoten)
