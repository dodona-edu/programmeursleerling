# bovengrens inlezen
bovengrens = int(input())

# rij van Fibonacci uitschrijven
vorige, volgende = 0, 1
while vorige <= bovengrens:
    print(vorige)
    vorige, volgende = volgende, vorige + volgende

# eerste getal groter dan bovengrens uitschrijven
print(volgende)
