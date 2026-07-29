r"""
>>> comprimeer('Hello, world!')
b'\x04\x81\xbb@,\xf0wI\xba\x02\x10'
>>> comprimeer('etaoinshrdlcum ')
b'\x124Vx\x9a\xbc\xde\xf0'
>>> comprimeer('')
b''
"""

# de veertien meest gebruikte letters in de Engelse taal, gevolgd door de spatie
VEELVOORKOMEND = 'etaoinshrdlcum '


def comprimeer(tekst):

    # zet de tekst om in een lijst van halve bytes
    halve_bytes = []
    for teken in tekst:
        index = VEELVOORKOMEND.find(teken)
        if index < 0:
            # een zeldzaam teken wordt opgeslagen als een halve byte met waarde
            # nul, gevolgd door de twee halve bytes van zijn ordinale waarde
            halve_bytes.append(0)
            halve_bytes.append(ord(teken) // 16)
            halve_bytes.append(ord(teken) % 16)
        else:
            # een veelvoorkomend teken wordt opgeslagen als één halve byte
            halve_bytes.append(index + 1)

    # vul de lijst aan met een halve byte met waarde nul als ze een oneven
    # lengte heeft, zodat ze in paren van halve bytes opgesplitst kan worden
    if len(halve_bytes) % 2:
        halve_bytes.append(0)

    # combineer elk paar halve bytes tot één byte
    return bytes(
        16 * halve_bytes[index] + halve_bytes[index + 1]
        for index in range(0, len(halve_bytes), 2)
    )


if __name__ == '__main__':
    import doctest
    doctest.testmod()
