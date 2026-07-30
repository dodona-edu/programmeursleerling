r"""
>>> print(open('data.txt', 'r').read(), end='')
Hello, world!
>>> encrypteer('data.txt')
>>> open('data.txt', 'rb').read()
b'\xc8\xe5\xec\xec\xef\xac\xa0\xf7\xef\xf2\xec\xe4\xa1\x8a'
>>> encrypteer('data.txt')
>>> print(open('data.txt', 'r').read(), end='')
Hello, world!
"""


def encrypteer(bestandsnaam):

    # lees het volledige bestand in als een byte string
    with open(bestandsnaam, 'rb') as bestand:
        data = bestand.read()

    # overschrijf het bestand met de geëncrypteerde byte string
    with open(bestandsnaam, 'wb') as bestand:
        bestand.write(data)
