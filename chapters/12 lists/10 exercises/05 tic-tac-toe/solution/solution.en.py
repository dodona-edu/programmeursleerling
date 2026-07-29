def opponent(player):

    """
    >>> opponent('X')
    'O'
    >>> opponent('O')
    'X'
    """

    return 'O' if player == 'X' else 'X'

def display_board(board):

    """
    >>> display_board([['X', 'O', '.'], ['.', 'X', '.'], ['O', '.', 'X']])
      1 2 3
    1 X O .
    2 . X .
    3 O . X
    """

    print('  1 2 3')
    for index, row in enumerate(board):
        print(f'{index + 1} ' + ' '.join(row))

def winner(board):

    """
    >>> winner([['X', 'O', '.'], ['.', 'X', '.'], ['O', '.', 'X']])
    'X'
    >>> winner([['X', 'O', '.'], ['.', '.', '.'], ['O', '.', 'X']])
    """

    # collect the three rows, the three columns and the two diagonals
    lines = list(board)
    lines.extend([board[row][column] for row in range(3)] for column in range(3))
    lines.append([board[index][index] for index in range(3)])
    lines.append([board[index][2 - index] for index in range(3)])

    # a player wins as soon as one of these lines only holds their markers
    for line in lines:
        if line[0] != '.' and line[0] == line[1] == line[2]:
            return line[0]

    return None

def full(board):

    """
    >>> full([['X', 'O', 'X'], ['X', 'O', 'O'], ['O', 'X', 'X']])
    True
    >>> full([['X', 'O', '.'], ['.', 'X', '.'], ['O', '.', 'X']])
    False
    """

    for row in board:
        for cell in row:
            if cell == '.':
                return False

    return True

def place(board, player, row, column):

    """
    >>> board = [['.', '.', '.'], ['.', '.', '.'], ['.', '.', '.']]
    >>> place(board, 'X', 2, 2)
    True
    >>> board
    [['.', '.', '.'], ['.', 'X', '.'], ['.', '.', '.']]
    >>> place(board, 'O', 2, 2)
    False
    >>> place(board, 'O', 4, 1)
    False
    """

    # the row and the column must both be on the board
    if not (1 <= row <= 3 and 1 <= column <= 3):
        return False

    # the cell must still be empty
    if board[row - 1][column - 1] != '.':
        return False

    board[row - 1][column - 1] = player

    return True

if __name__ == '__main__':
    import doctest
    doctest.testmod()
