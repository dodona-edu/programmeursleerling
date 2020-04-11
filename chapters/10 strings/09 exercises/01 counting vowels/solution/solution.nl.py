# tekst inlezen
tekst = input().upper()

# aantal voorkomens van elke klinker in de tekst uitschrijven
for klinker in 'AEIOU':
    print(f'{klinker}: {tekst.count(klinker)}')
