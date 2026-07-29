import random

# het te raden getal nemen
getal = random.randint(1, 1000)

# gokken inlezen tot het getal geraden is
pogingen = 0
geraden = False
while not geraden:

    # volgende gok inlezen
    gok = int(input())
    pogingen += 1

    # zeggen hoe het te raden getal zich tot de gok verhoudt
    if getal < gok:
        print('Lager')
    elif getal > gok:
        print('Hoger')
    else:
        print('Je hebt het geraden!')
        geraden = True

# afdrukken hoeveel pogingen er nodig waren
print(f'Aantal pogingen: {pogingen}')
