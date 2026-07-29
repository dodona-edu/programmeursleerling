# het te raden getal ligt nog tussen deze twee getallen
kleinste = 1
grootste = 1000

# gokken zolang een getal mogelijk is en het getal niet geraden is
pogingen = 0
geraden = False
while not geraden and kleinste <= grootste:

    # het midden van de getallen die nog mogelijk zijn gokken
    gok = (kleinste + grootste) // 2
    pogingen += 1
    print(f'Is het {gok}?')

    # antwoord van de gebruiker verwerken
    antwoord = input()
    if antwoord == 'C':
        geraden = True
    elif antwoord == 'L':
        grootste = gok - 1
    else:
        kleinste = gok + 1

# afdrukken hoeveel pogingen er nodig waren, of dat de antwoorden onmogelijk zijn
if geraden:
    print(f'Aantal pogingen: {pogingen}')
else:
    print('Dat is onmogelijk!')
