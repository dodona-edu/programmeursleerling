def schoon(s):
    ns = ""
    s = s.lower()
    for c in s:
        if 'a' <= c <= 'z':
            ns += c
        else:
            ns += " "
    return ns


# woord inlezen
woord = input()

# tekst inlezen
tekst = input()

# aantal voorkomens van woord in tekst bepalen
aantal = 0
for woord2 in schoon(tekst).split():
    if woord2 == woord:
        aantal += 1

# print number of occurrences of woord in sentence
print(f'Aantal keren dat het woord "{woord}" voorkomt: {aantal}')
