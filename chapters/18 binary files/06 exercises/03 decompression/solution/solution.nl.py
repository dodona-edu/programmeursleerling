r"""
>>> decomprimeer(b'\x04\x81\xbb@,\xf0wI\xba\x02\x10')
'Hello, world!'
>>> decomprimeer(b'\x124Vx\x9a\xbc\xde\xf0')
'etaoinshrdlcum '
>>> decomprimeer(b'')
''
"""

# de veertien meest gebruikte letters in de Engelse taal, gevolgd door de spatie
VEELVOORKOMEND = 'etaoinshrdlcum '


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
            # een halve byte verschillend van nul is een veelvoorkomend teken
            tekens.append(VEELVOORKOMEND[halve_bytes[index] - 1])
            index += 1
        elif index + 2 < len(halve_bytes):
            # een halve byte met waarde nul wordt gevolgd door de twee halve
            # bytes van de ordinale waarde van een zeldzaam teken
            tekens.append(
                chr(16 * halve_bytes[index + 1] + halve_bytes[index + 2])
            )
            index += 3
        else:
            # een halve byte met waarde nul die niet gevolgd wordt door twee
            # andere halve bytes, is de opvulling van de laatste byte
            break

    return ''.join(tekens)


if __name__ == '__main__':
    import doctest
    doctest.testmod()
