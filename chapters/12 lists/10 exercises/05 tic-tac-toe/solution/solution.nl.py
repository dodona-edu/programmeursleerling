def opponent(speler):

    """
    >>> opponent('X')
    'O'
    >>> opponent('O')
    'X'
    """

    return 'O' if speler == 'X' else 'X'

def toon_bord(bord):

    """
    >>> toon_bord([['X', 'O', '.'], ['.', 'X', '.'], ['O', '.', 'X']])
      1 2 3
    1 X O .
    2 . X .
    3 O . X
    """

    print('  1 2 3')
    for index, rij in enumerate(bord):
        print(f'{index + 1} ' + ' '.join(rij))

def winnaar(bord):

    """
    >>> winnaar([['X', 'O', '.'], ['.', 'X', '.'], ['O', '.', 'X']])
    'X'
    >>> winnaar([['X', 'O', '.'], ['.', '.', '.'], ['O', '.', 'X']])
    """

    # verzamel de drie rijen, de drie kolommen en de twee diagonalen
    lijnen = list(bord)
    lijnen.extend([bord[rij][kolom] for rij in range(3)] for kolom in range(3))
    lijnen.append([bord[index][index] for index in range(3)])
    lijnen.append([bord[index][2 - index] for index in range(3)])

    # een speler wint zodra één van die lijnen enkel haar tekens bevat
    for lijn in lijnen:
        if lijn[0] != '.' and lijn[0] == lijn[1] == lijn[2]:
            return lijn[0]

    return None

def vol(bord):

    """
    >>> vol([['X', 'O', 'X'], ['X', 'O', 'O'], ['O', 'X', 'X']])
    True
    >>> vol([['X', 'O', '.'], ['.', 'X', '.'], ['O', '.', 'X']])
    False
    """

    for rij in bord:
        for cel in rij:
            if cel == '.':
                return False

    return True

def plaats(bord, speler, rij, kolom):

    """
    >>> bord = [['.', '.', '.'], ['.', '.', '.'], ['.', '.', '.']]
    >>> plaats(bord, 'X', 2, 2)
    True
    >>> bord
    [['.', '.', '.'], ['.', 'X', '.'], ['.', '.', '.']]
    >>> plaats(bord, 'O', 2, 2)
    False
    >>> plaats(bord, 'O', 4, 1)
    False
    """

    # de rij en de kolom moeten allebei op het bord liggen
    if not (1 <= rij <= 3 and 1 <= kolom <= 3):
        return False

    # de cel moet nog leeg zijn
    if bord[rij - 1][kolom - 1] != '.':
        return False

    bord[rij - 1][kolom - 1] = speler

    return True

if __name__ == '__main__':
    import doctest
    doctest.testmod()
