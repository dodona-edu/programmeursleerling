r"""
>>> compress('Hello, world!')
b'\x04\x81\xbb@,\xf0wI\xba\x02\x10'
>>> compress('etaoinshrdlcum ')
b'\x124Vx\x9a\xbc\xde\xf0'
>>> compress('')
b''
"""

# the fourteen most common letters in the English language, followed by the space
COMMON = 'etaoinshrdlcum '


def compress(text):

    # translate the text into a list of half-bytes
    half_bytes = []
    for character in text:
        index = COMMON.find(character)
        if index < 0:
            # an uncommon character is stored as a zero half-byte, followed by
            # the two half-bytes of its ordinal value
            half_bytes.append(0)
            half_bytes.append(ord(character) // 16)
            half_bytes.append(ord(character) % 16)
        else:
            # a common character is stored as a single half-byte
            half_bytes.append(index + 1)

    # pad the list with a zero half-byte if it has an odd length, so that it
    # can be split into pairs of half-bytes
    if len(half_bytes) % 2:
        half_bytes.append(0)

    # combine every pair of half-bytes into a single byte
    return bytes(
        16 * half_bytes[index] + half_bytes[index + 1]
        for index in range(0, len(half_bytes), 2)
    )


if __name__ == '__main__':
    import doctest
    doctest.testmod()
