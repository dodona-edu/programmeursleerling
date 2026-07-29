r"""
>>> compress_file('data.txt', 'data.cmp')
(13, 11)
>>> open('data.cmp', 'rb').read()
b'\x04\x81\xbb@,\xf0wI\xba\x02\x10'
>>> decompress_file('data.cmp', 'data.new')
(11, 13)
>>> open('data.new', 'rb').read() == open('data.txt', 'rb').read()
True
>>> compress_file('data.xxx', 'data.yyy')
Traceback (most recent call last):
AssertionError: input file does not exist
>>> compress_file('data.txt', 'data.cmp')
Traceback (most recent call last):
AssertionError: output file already exists
"""

import os

# the fourteen most common letters in the English language, followed by the space
COMMON = 'etaoinshrdlcum '


def compress(text):

    # translate the text into a list of half-bytes
    half_bytes = []
    for character in text:
        index = COMMON.find(character)
        if index < 0:
            half_bytes.append(0)
            half_bytes.append(ord(character) // 16)
            half_bytes.append(ord(character) % 16)
        else:
            half_bytes.append(index + 1)

    # pad the list with a zero half-byte if it has an odd length
    if len(half_bytes) % 2:
        half_bytes.append(0)

    # combine every pair of half-bytes into a single byte
    return bytes(
        16 * half_bytes[index] + half_bytes[index + 1]
        for index in range(0, len(half_bytes), 2)
    )


def decompress(data):

    # split every byte into its two half-bytes
    half_bytes = []
    for byte in data:
        half_bytes.append(byte // 16)
        half_bytes.append(byte % 16)

    # translate the list of half-bytes back into the original text
    characters = []
    index = 0
    while index < len(half_bytes):
        if half_bytes[index]:
            characters.append(COMMON[half_bytes[index] - 1])
            index += 1
        elif index + 2 < len(half_bytes):
            characters.append(
                chr(16 * half_bytes[index + 1] + half_bytes[index + 2])
            )
            index += 3
        else:
            # trailing zero half-byte that completes the last byte
            break

    return ''.join(characters)


def compress_file(source, destination):

    assert os.path.exists(source), 'input file does not exist'
    assert not os.path.exists(destination), 'output file already exists'

    # read the entire input file as a byte string
    with open(source, 'rb') as datafile:
        data = datafile.read()

    # every byte is treated as the character with that ordinal value
    compressed = compress(data.decode('latin-1'))

    with open(destination, 'wb') as datafile:
        datafile.write(compressed)

    return len(data), len(compressed)


def decompress_file(source, destination):

    assert os.path.exists(source), 'input file does not exist'
    assert not os.path.exists(destination), 'output file already exists'

    # read the entire input file as a byte string
    with open(source, 'rb') as datafile:
        data = datafile.read()

    # every character is written back as the byte with that ordinal value
    decompressed = decompress(data).encode('latin-1')

    with open(destination, 'wb') as datafile:
        datafile.write(decompressed)

    return len(data), len(decompressed)


if __name__ == '__main__':
    import doctest
    doctest.testmod()
