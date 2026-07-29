r"""
>>> comprimeer_bestand('data.txt', 'data.cmp')
(13, 11)
>>> open('data.cmp', 'rb').read()
b'\x04\x81\xbb@,\xf0wI\xba\x02\x10'
>>> decomprimeer_bestand('data.cmp', 'data.new')
(11, 13)
>>> open('data.new', 'rb').read() == open('data.txt', 'rb').read()
True
>>> comprimeer_bestand('data.xxx', 'data.yyy')
Traceback (most recent call last):
AssertionError: invoerbestand bestaat niet
>>> comprimeer_bestand('data.txt', 'data.cmp')
Traceback (most recent call last):
AssertionError: uitvoerbestand bestaat al
"""

import os

# de veertien meest gebruikte letters in de Engelse taal, gevolgd door de spatie
VEELVOORKOMEND = 'etaoinshrdlcum '


def comprimeer(tekst):

    # zet de tekst om in een lijst van halve bytes
    halve_bytes = []
    for teken in tekst:
        index = VEELVOORKOMEND.find(teken)
        if index < 0:
            halve_bytes.append(0)
            halve_bytes.append(ord(teken) // 16)
            halve_bytes.append(ord(teken) % 16)
        else:
            halve_bytes.append(index + 1)

    # vul de lijst aan met een halve byte met waarde nul als ze een oneven
    # lengte heeft
    if len(halve_bytes) % 2:
        halve_bytes.append(0)

    # combineer elk paar halve bytes tot één byte
    return bytes(
        16 * halve_bytes[index] + halve_bytes[index + 1]
        for index in range(0, len(halve_bytes), 2)
    )


def decomprimeer(data):

    # splits elke byte op in zijn twee halve bytes
    halve_bytes = []
    for byte in data:
        halve_bytes.append(byte // 16)
        halve_bytes.append(byte % 16)

    # zet de lijst van halve bytes terug om in de originele tekst
    tekens = []
    index = 0
    while index < len(halve_bytes):
        if halve_bytes[index]:
            tekens.append(VEELVOORKOMEND[halve_bytes[index] - 1])
            index += 1
        elif index + 2 < len(halve_bytes):
            tekens.append(
                chr(16 * halve_bytes[index + 1] + halve_bytes[index + 2])
            )
            index += 3
        else:
            # halve byte met waarde nul die de laatste byte vervolledigt
            break

    return ''.join(tekens)


def comprimeer_bestand(bronbestand, doelbestand):

    assert os.path.exists(bronbestand), 'invoerbestand bestaat niet'
    assert not os.path.exists(doelbestand), 'uitvoerbestand bestaat al'

    # lees het volledige invoerbestand in als een byte string
    with open(bronbestand, 'rb') as bestand:
        data = bestand.read()

    # elke byte wordt behandeld als het teken met die ordinale waarde
    gecomprimeerd = comprimeer(data.decode('latin-1'))

    with open(doelbestand, 'wb') as bestand:
        bestand.write(gecomprimeerd)

    return len(data), len(gecomprimeerd)


def decomprimeer_bestand(bronbestand, doelbestand):

    assert os.path.exists(bronbestand), 'invoerbestand bestaat niet'
    assert not os.path.exists(doelbestand), 'uitvoerbestand bestaat al'

    # lees het volledige invoerbestand in als een byte string
    with open(bronbestand, 'rb') as bestand:
        data = bestand.read()

    # elk teken wordt weggeschreven als de byte met die ordinale waarde
    gedecomprimeerd = decomprimeer(data).encode('latin-1')

    with open(doelbestand, 'wb') as bestand:
        bestand.write(gedecomprimeerd)

    return len(data), len(gedecomprimeerd)


if __name__ == '__main__':
    import doctest
    doctest.testmod()
