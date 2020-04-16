def mask2int(mask):

    """
    >>> mask2int('00101010')
    42
    """

    intmask = 0
    for index, bit in enumerate(mask[::-1]):
        if bit == '1':
            intmask |= 1 << index

    return intmask

def bitmask(s, mask):

    """
    >>> bitmask('Hello, world!', '00101010')
    'bOFFE\\x06\\n]EXFN\\x0b'
    >>> bitmask('bOFFE\\x06\\n]EXFN\\x0b', '00101010')
    'Hello, world!'
    """

    mask = mask2int(mask)

    return ''.join(chr(ord(c) ^ mask) for c in s)

if __name__ == '__main__':
    import doctest
    doctest.testmod()