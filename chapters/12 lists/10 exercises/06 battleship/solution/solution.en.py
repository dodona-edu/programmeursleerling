import random

COLUMNS = 'ABCD'
ROWS = '123'

def place_ships():

    """
    >>> grid = place_ships()
    >>> ships(grid)
    3
    """

    while True:

        # pick three different cells of the grid
        cells = random.sample(
            [(row, column) for row in range(3) for column in range(4)], 3
        )

        # ships are not allowed to touch each other horizontally or vertically
        touching = False
        for row1, column1 in cells:
            for row2, column2 in cells:
                if abs(row1 - row2) + abs(column1 - column2) == 1:
                    touching = True

        if not touching:
            break

    # hide a battleship in each of the three cells
    grid = [['.'] * 4 for _ in range(3)]
    for row, column in cells:
        grid[row][column] = 'X'

    return grid

def display_grid(grid):

    """
    >>> display_grid([['.', '.', 'X', '.'], ['X', '.', '.', '.'], ['.', '.', 'X', '.']])
      A B C D
    1 . . X .
    2 X . . .
    3 . . X .
    """

    print('  ' + ' '.join(COLUMNS))
    for index, row in enumerate(grid):
        print(f'{index + 1} ' + ' '.join(row))

def ships(grid):

    """
    >>> ships([['.', '.', 'X', '.'], ['X', '.', '.', '.'], ['.', '.', 'X', '.']])
    3
    """

    count = 0
    for row in grid:
        for cell in row:
            if cell == 'X':
                count += 1

    return count

def shoot(grid, cell):

    """
    >>> grid = [['.', '.', 'X', '.'], ['X', '.', '.', '.'], ['.', '.', 'X', '.']]
    >>> shoot(grid, 'C1')
    'You sunk my battleship!'
    >>> shoot(grid, 'C1')
    'Miss!'
    >>> shoot(grid, 'E1')
    Traceback (most recent call last):
    AssertionError: invalid cell
    """

    assert (
        len(cell) == 2 and cell[0] in COLUMNS and cell[1] in ROWS
    ), 'invalid cell'

    row = ROWS.index(cell[1])
    column = COLUMNS.index(cell[0])

    if grid[row][column] == '.':
        return 'Miss!'

    grid[row][column] = '.'

    return 'You sunk my battleship!'

if __name__ == '__main__':
    import doctest
    doctest.testmod()
