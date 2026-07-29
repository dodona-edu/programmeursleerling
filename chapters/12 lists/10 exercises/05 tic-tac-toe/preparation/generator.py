import os
import sys
import importlib.util
import random

# set fixed seed for generating test cases
random.seed(123456789)

# locate evaldir
evaldir = os.path.join('..', 'evaluation')
if not os.path.exists(evaldir):
    os.makedirs(evaldir)

# locate solutiondir
solutiondir = os.path.join('..', 'solution')
if not os.path.exists(solutiondir):
    os.makedirs(solutiondir)

# load functionality defined in sample solution
module_name = 'solution'
file_path = os.path.join(solutiondir, 'solution.en.py')
spec = importlib.util.spec_from_file_location(module_name, file_path)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

for name in dir(module):
    if not (name.startswith('__') and name.endswith('__')):
        globals()[name] = eval(f'module.{name}')

EMPTY = [['.'] * 3 for _ in range(3)]

def empty_board():

    return [['.'] * 3 for _ in range(3)]

def random_board(moves=None, stop_at_winner=True):

    """
    Play a random game of tic-tac-toe, and return the board as it looks after
    the given number of moves (or after a random number of moves).
    """

    board = empty_board()
    cells = [(row, column) for row in range(1, 4) for column in range(1, 4)]
    random.shuffle(cells)

    if moves is None:
        moves = random.randint(0, 9)

    player = 'X'
    for row, column in cells[:moves]:
        place(board, player, row, column)
        player = opponent(player)
        if stop_at_winner and winner(board) is not None:
            break

    return board

# ---------------------------------------------------------------------------
# function opponent
# ---------------------------------------------------------------------------

sys.stdout = open(os.path.join(evaldir, '0.in'), 'w', encoding='utf-8')
for index, source in enumerate((
    "opponent('X')",
    "opponent('O')",
    "opponent(opponent('X'))",
    "opponent(opponent('O'))",
    "opponent(opponent(opponent('X')))",
    "opponent(opponent(opponent(opponent('O'))))",
)):
    context = ' # doctest: +NEWCONTEXT' if index == 0 else ''
    print(f'>>> {source}{context}')
    print(repr(eval(source)))
    print()

# a player marker that is stored in a variable, just like the main program does
print(">>> player = 'X' # doctest: +NEWCONTEXT")
print()
for _ in range(4):
    print('>>> player = opponent(player)')
    print('>>> player')
    print(repr(eval("opponent('X')" if _ % 2 == 0 else "opponent('O')")))
    print()

# ---------------------------------------------------------------------------
# function display_board
# ---------------------------------------------------------------------------

cases = [
    empty_board(),
    [['X', 'O', '.'], ['.', 'X', '.'], ['O', '.', 'X']],
    [['X', 'O', 'X'], ['X', 'O', 'O'], ['O', 'X', 'X']],
    [['O', 'O', 'O'], ['X', 'X', '.'], ['.', '.', '.']],
    [['.', '.', 'X'], ['.', 'X', '.'], ['X', '.', '.']],
]
while len(cases) < 20:
    board = random_board(stop_at_winner=False)
    if board not in cases:
        cases.append(board)

sys.stdout = open(os.path.join(evaldir, '1.in'), 'w', encoding='utf-8')
for board in cases:
    print(f'>>> display_board({board!r}) # doctest: +STDOUT')
    display_board(board)
    print()

# ---------------------------------------------------------------------------
# function winner
# ---------------------------------------------------------------------------

cases = [
    empty_board(),
    # every possible line, won by alternating players
    [['X', 'X', 'X'], ['O', 'O', '.'], ['.', '.', '.']],
    [['O', 'X', '.'], ['O', 'O', 'O'], ['X', '.', 'X']],
    [['O', 'X', '.'], ['O', '.', 'X'], ['X', 'X', 'X']],
    [['X', 'O', '.'], ['X', 'O', '.'], ['X', '.', '.']],
    [['X', 'O', 'X'], ['.', 'O', 'X'], ['.', 'O', '.']],
    [['O', '.', 'X'], ['O', '.', 'X'], ['.', 'O', 'X']],
    [['X', 'O', 'O'], ['.', 'X', '.'], ['O', '.', 'X']],
    [['O', 'X', 'X'], ['.', 'X', 'O'], ['X', '.', 'O']],
    # boards that come close to a win, but are not won
    [['X', 'X', 'O'], ['O', 'O', 'X'], ['X', 'O', 'X']],
    [['X', 'X', '.'], ['O', 'O', '.'], ['.', '.', '.']],
    [['X', '.', 'X'], ['.', 'O', '.'], ['O', '.', 'X']],
    [['.', '.', '.'], ['X', 'X', '.'], ['O', 'O', '.']],
    # a full board without a winner (a draw)
    [['X', 'O', 'X'], ['X', 'O', 'O'], ['O', 'X', 'X']],
]
while len(cases) < 35:
    board = random_board()
    if board not in cases:
        cases.append(board)

sys.stdout = open(os.path.join(evaldir, '2.in'), 'w', encoding='utf-8')
for board in cases:
    print(f'>>> winner({board!r})')
    result = winner(board)
    if result is not None:
        print(repr(result))
    print()

# ---------------------------------------------------------------------------
# function full
# ---------------------------------------------------------------------------

cases = [
    empty_board(),
    [['X', 'O', 'X'], ['X', 'O', 'O'], ['O', 'X', 'X']],
    [['X', 'O', 'X'], ['X', 'O', 'O'], ['O', 'X', '.']],
    [['.', 'O', 'X'], ['X', 'O', 'O'], ['O', 'X', 'X']],
    [['X', 'O', 'X'], ['X', '.', 'O'], ['O', 'X', 'X']],
    [['X', 'X', 'X'], ['O', 'O', 'O'], ['X', 'O', 'X']],
]
while len(cases) < 20:
    board = random_board(moves=random.randint(0, 9), stop_at_winner=False)
    if board not in cases:
        cases.append(board)

sys.stdout = open(os.path.join(evaldir, '3.in'), 'w', encoding='utf-8')
for board in cases:
    print(f'>>> full({board!r})')
    print(repr(full(board)))
    print()

# ---------------------------------------------------------------------------
# function place
# ---------------------------------------------------------------------------

# each scenario plays a full game, with illegal moves mixed in: moves onto an
# occupied cell, and moves onto a row or column that is not on the board
OFF_BOARD = [
    (0, 1), (4, 2), (1, 0), (3, 4), (0, 0), (4, 4), (-1, 2), (2, -3), (7, 7),
]

sys.stdout = open(os.path.join(evaldir, '4.in'), 'w', encoding='utf-8')
for index in range(15):

    varname = f'board_{index + 1:02d}'
    board = empty_board()
    print(f'>>> {varname} = {board!r} # doctest: +NEWCONTEXT')

    cells = [(row, column) for row in range(1, 4) for column in range(1, 4)]
    random.shuffle(cells)

    player = 'X'
    played = []
    for row, column in cells:

        # occasionally attempt an illegal move first
        if played and random.random() < 0.4:
            if random.random() < 0.5:
                bad_row, bad_column = random.choice(played)
            else:
                bad_row, bad_column = random.choice(OFF_BOARD)
            print(f'>>> place({varname}, {player!r}, {bad_row}, {bad_column})')
            print(repr(place(board, player, bad_row, bad_column)))

        print(f'>>> place({varname}, {player!r}, {row}, {column})')
        print(repr(place(board, player, row, column)))
        played.append((row, column))

        print(f'>>> {varname}')
        print(repr(board))

        if winner(board) is not None or full(board):
            break

        player = opponent(player)

    print(f'>>> display_board({varname}) # doctest: +STDOUT')
    display_board(board)

    print(f'>>> winner({varname})')
    result = winner(board)
    if result is not None:
        print(repr(result))

    print(f'>>> full({varname})')
    print(repr(full(board)))

    print()
