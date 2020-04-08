# zin inlezen
zin = input()

# zin omzetten naar kleine letters
# OPMERKING: hierdoor wordt geen onderscheid gemaakt tussen hoofdletters en kleine letters
zin = zin.lower()

# aantal verschillende klinkers in de zin tellen
aantal = 0
for klinker in 'aeiou':
    if klinker in zin:
        aantal += 1

meervoud = 's'
verschillende = ' verschillende'
if aantal == 0:
    aantal = 'geen'
    verschillende = ''
elif aantal == 1:
    aantal = 'slechts 1'
    meervoud = ''

print(f'De zin bevat {aantal}{verschillende} klinker{meervoud}.')
