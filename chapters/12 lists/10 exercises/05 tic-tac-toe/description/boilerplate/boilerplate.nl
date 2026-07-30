def opponent(speler):

    """
    >>> opponent('X')
    'O'
    >>> opponent('O')
    'X'
    """

def toon_bord(bord):

    """
    >>> toon_bord([['X', 'O', '.'], ['.', 'X', '.'], ['O', '.', 'X']])
      1 2 3
    1 X O .
    2 . X .
    3 O . X
    """

def winnaar(bord):

    """
    >>> winnaar([['X', 'O', '.'], ['.', 'X', '.'], ['O', '.', 'X']])
    'X'
    >>> winnaar([['X', 'O', '.'], ['.', '.', '.'], ['O', '.', 'X']])
    """

def vol(bord):

    """
    >>> vol([['X', 'O', 'X'], ['X', 'O', 'O'], ['O', 'X', 'X']])
    True
    >>> vol([['X', 'O', '.'], ['.', 'X', '.'], ['O', '.', 'X']])
    False
    """

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

if __name__ == '__main__':
    import doctest
    doctest.testmod()
