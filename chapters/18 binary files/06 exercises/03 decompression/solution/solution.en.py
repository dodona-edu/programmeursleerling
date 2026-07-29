r"""
>>> decompress(b'\x04\x81\xbb@,\xf0wI\xba\x02\x10')
'Hello, world!'
>>> decompress(b'\x124Vx\x9a\xbc\xde\xf0')
'etaoinshrdlcum '
>>> decompress(b'')
''
"""

# the fourteen most common letters in the English language, followed by the space
COMMON = 'etaoinshrdlcum '


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
            # a non-zero half-byte is one of the common characters
            characters.append(COMMON[half_bytes[index] - 1])
            index += 1
        elif index + 2 < len(half_bytes):
            # a zero half-byte is followed by the two half-bytes of the
            # ordinal value of an uncommon character
            characters.append(
                chr(16 * half_bytes[index + 1] + half_bytes[index + 2])
            )
            index += 3
        else:
            # a zero half-byte that is not followed by two other half-bytes is
            # the padding that was added to complete the last byte
            break

    return ''.join(characters)


if __name__ == '__main__':
    import doctest
    doctest.testmod()
