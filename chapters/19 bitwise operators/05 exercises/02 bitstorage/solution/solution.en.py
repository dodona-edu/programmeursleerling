"""
>>> store = setbit(0, 0, True)
>>> store
1
>>> getbit(store, 0)
True
>>> bitstring(store)
'00000001'
>>> store = setbit(store, 1, True)
>>> store
3
>>> getbit(store, 1)
True
>>> bitstring(store)
'00000011'
>>> store = setbit(store, 2, False)
>>> store
3
>>> getbit(store, 2)
False
>>> bitstring(store)
'00000011'
>>> store = setbit(store, 3, True)
>>> store
11
>>> getbit(store, 3)
True
>>> bitstring(store)
'00001011'
>>> store = setbit(store, 4, False)
>>> store
11
>>> getbit(store, 4)
False
>>> bitstring(store)
'00001011'
>>> store = setbit(store, 5, True)
>>> store
43
>>> getbit(store, 5)
True
>>> bitstring(store)
'00101011'
>>> store = setbit(store, 1, False)
>>> store
41
>>> getbit(store, 1)
False
>>> bitstring(store)
'00101001'
"""


def setbit(store, index, value):

    mask = 1 << index
    if value:
        store |= mask
    else:
        store &= ~mask

    return store

def getbit(store, index):

    """
    Returns 0 when the bit corresponding to index is set, and something else
    otherwise. As only 0 is interpreted as False this function can be used to
    test the value of the bit.
    """

    mask = 1 << index
    return store & mask

def bitstring(store):

    bits = ''
    for i in range(8):
        index = 7 - i
        bits += '1' if getbit(store, index) else '0'

    return bits

if __name__ == '__main__':
    import doctest
    doctest.testmod()
