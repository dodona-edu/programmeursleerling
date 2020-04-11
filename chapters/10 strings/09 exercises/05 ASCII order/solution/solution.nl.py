# tekst inlezen
tekst = input()

# letters van tekst in ASCII volgorde zetten
ntekst = ""
while len( tekst ) > 0:
    i = 0
    ch = tekst[i]
    j = 1
    while j < len( tekst ):
        if tekst[j] < ch:
            ch = tekst[j]
            i = j
        j += 1
    tekst = tekst[:i] + tekst[i+1:]
    ntekst += ch

# letters van tekst in ASCII volgorde uitschrijven
print( ntekst )
