"""
>>> opslag = setbit(0, 0, True)
>>> opslag
1
>>> getbit(opslag, 0)
True
>>> bitstring(opslag)
'00000001'
>>> opslag = setbit(opslag, 1, True)
>>> opslag
3
>>> getbit(opslag, 1)
True
>>> bitstring(opslag)
'00000011'
>>> opslag = setbit(opslag, 2, False)
>>> opslag
3
>>> getbit(opslag, 2)
False
>>> bitstring(opslag)
'00000011'
>>> opslag = setbit(opslag, 3, True)
>>> opslag
11
>>> getbit(opslag, 3)
True
>>> bitstring(opslag)
'00001011'
>>> opslag = setbit(opslag, 4, False)
>>> opslag
11
>>> getbit(opslag, 4)
False
>>> bitstring(opslag)
'00001011'
>>> opslag = setbit(opslag, 5, True)
>>> opslag
43
>>> getbit(opslag, 5)
True
>>> bitstring(opslag)
'00101011'
>>> opslag = setbit(opslag, 1, False)
>>> opslag
41
>>> getbit(opslag, 1)
False
>>> bitstring(opslag)
'00101001'
"""


def setbit(opslag, index, value):

    masker = 1 << index
    if value:
        opslag |= masker
    else:
        opslag &= ~masker

    return opslag

def getbit(opslag, index):

    """
    Geeft 0 terug als de bit behorende bij de index op 1 staat, en geeft anders
    iets anders terug. Omdat alleen 0 als False wordt beschouwd, kun
    je deze functie gebruiken om de waarde van een bit te testen.
    """

    masker = 1 << index
    return bool(opslag & masker)

def bitstring(opslag):

    bits = ''
    for i in range(8):
        index = 7 - i
        bits += '1' if getbit(opslag, index) else '0'

    return bits

if __name__ == '__main__':
    import doctest
    doctest.testmod()
