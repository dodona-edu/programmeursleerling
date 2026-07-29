import random

KOLOMMEN = 'ABCD'
RIJEN = '123'

def plaats_schepen():

    """
    >>> matrix = plaats_schepen()
    >>> schepen(matrix)
    3
    """

    while True:

        # kies drie verschillende cellen van de matrix
        cellen = random.sample(
            [(rij, kolom) for rij in range(3) for kolom in range(4)], 3
        )

        # de schepen mogen elkaar noch horizontaal, noch verticaal raken
        raken = False
        for rij1, kolom1 in cellen:
            for rij2, kolom2 in cellen:
                if abs(rij1 - rij2) + abs(kolom1 - kolom2) == 1:
                    raken = True

        if not raken:
            break

    # verstop in elk van de drie cellen een oorlogsschip
    matrix = [['.'] * 4 for _ in range(3)]
    for rij, kolom in cellen:
        matrix[rij][kolom] = 'X'

    return matrix

def toon_matrix(matrix):

    """
    >>> toon_matrix([['.', '.', 'X', '.'], ['X', '.', '.', '.'], ['.', '.', 'X', '.']])
      A B C D
    1 . . X .
    2 X . . .
    3 . . X .
    """

    print('  ' + ' '.join(KOLOMMEN))
    for index, rij in enumerate(matrix):
        print(f'{index + 1} ' + ' '.join(rij))

def schepen(matrix):

    """
    >>> schepen([['.', '.', 'X', '.'], ['X', '.', '.', '.'], ['.', '.', 'X', '.']])
    3
    """

    aantal = 0
    for rij in matrix:
        for cel in rij:
            if cel == 'X':
                aantal += 1

    return aantal

def schiet(matrix, cel):

    """
    >>> matrix = [['.', '.', 'X', '.'], ['X', '.', '.', '.'], ['.', '.', 'X', '.']]
    >>> schiet(matrix, 'C1')
    'Raak!'
    >>> schiet(matrix, 'C1')
    'Mis!'
    >>> schiet(matrix, 'E1')
    Traceback (most recent call last):
    AssertionError: ongeldige cel
    """

    assert (
        len(cel) == 2 and cel[0] in KOLOMMEN and cel[1] in RIJEN
    ), 'ongeldige cel'

    rij = RIJEN.index(cel[1])
    kolom = KOLOMMEN.index(cel[0])

    if matrix[rij][kolom] == '.':
        return 'Mis!'

    matrix[rij][kolom] = '.'

    return 'Raak!'

if __name__ == '__main__':
    import doctest
    doctest.testmod()
