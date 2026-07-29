r"""
>>> print(open('data.txt', 'r').read(), end='')
Hello, world!
>>> encrypt('data.txt')
>>> open('data.txt', 'rb').read()
b'\xc8\xe5\xec\xec\xef\xac\xa0\xf7\xef\xf2\xec\xe4\xa1\x8a'
>>> encrypt('data.txt')
>>> print(open('data.txt', 'r').read(), end='')
Hello, world!
"""


def encrypt(filename):

    # read the entire file as a byte string
    with open(filename, 'rb') as datafile:
        data = datafile.read()

    # flip the highest bit of every byte
    data = bytes(
        byte + 128 if byte < 128 else byte - 128
        for byte in data
    )

    # overwrite the file with the encrypted byte string
    with open(filename, 'wb') as datafile:
        datafile.write(data)


if __name__ == '__main__':
    import doctest
    doctest.testmod()
