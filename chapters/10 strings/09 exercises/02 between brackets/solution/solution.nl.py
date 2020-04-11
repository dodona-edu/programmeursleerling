# tekst inlezen
tekst = input()

# letters verzamelen die ingesloten zitten tussen vierkante haakjes
letters = ''
ingesloten = False
for karakter in tekst:
    if karakter == '[':
        ingesloten = True
    elif karakter == ']':
        ingesloten = False
    elif ingesloten:
        letters += karakter

# letters afdrukken
print(letters)
