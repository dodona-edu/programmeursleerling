bovengrens = int(input())

# rij van Fibonacci uitschrijven
vorige, volgende = 0, 1
print(vorige)
while vorige <= bovengrens:
    print(volgende)
    vorige, volgende = volgende, vorige + volgende