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

CELLS = [column + row for row in '123' for column in 'ABCD']

# cells that are not on the grid, in one way or another
INVALID_CELLS = [
    'E1', 'A4', 'a1', 'd3', '3D', '1A', 'A', '3', '', 'AA', '11', 'A10',
    'C 2', 'B0', 'Z9',
]

def make_grid(*cells):

    """
    Build a grid that hides a battleship in each of the given cells.
    """

    grid = [['.'] * 4 for _ in range(3)]
    for cell in cells:
        grid['123'.index(cell[1])]['ABCD'.index(cell[0])] = 'X'

    return grid

def random_grid(count=3):

    """
    Build a grid that hides the given number of battleships in random cells,
    without bothering about battleships touching each other.
    """

    return make_grid(*random.sample(CELLS, count))

# ---------------------------------------------------------------------------
# function place_ships
# ---------------------------------------------------------------------------

# read the custom output processor that checks the return value; the placement
# of the battleships is random, so the return value of the submitted solution
# cannot simply be compared to the one of the sample solution
with open('gridchecker.py', 'r', encoding='utf-8') as handle:
    CHECKER = handle.read().strip()

sys.stdout = open(os.path.join(evaldir, '0.in'), 'w', encoding='utf-8')

print('>>> place_ships()')

# define custom checker
print('<DEFINITION>')
print(CHECKER)
print('</DEFINITION>')

# call custom checker
print('<OUTPUTPROCESSOR>')
print('GridChecker(expected_type=[[str]])')
print('</OUTPUTPROCESSOR>')

# generate return value
print(f'{place_ships()}')

# ---------------------------------------------------------------------------
# function display_grid
# ---------------------------------------------------------------------------

cases = [
    make_grid(),
    make_grid('C1', 'A2', 'C3'),
    make_grid('A1', 'B1', 'C1', 'D1'),
    make_grid('D3'),
    make_grid(*CELLS),
]
while len(cases) < 20:
    grid = random_grid(random.randint(0, 6))
    if grid not in cases:
        cases.append(grid)

sys.stdout = open(os.path.join(evaldir, '1.in'), 'w', encoding='utf-8')
for grid in cases:
    print(f'>>> display_grid({grid!r}) # doctest: +STDOUT')
    display_grid(grid)
    print()

# ---------------------------------------------------------------------------
# function ships
# ---------------------------------------------------------------------------

cases = [
    make_grid(),
    make_grid('C1', 'A2', 'C3'),
    make_grid('B2'),
    make_grid(*CELLS),
    make_grid('A1', 'D1', 'A3', 'D3'),
]
while len(cases) < 20:
    grid = random_grid(random.randint(0, 8))
    if grid not in cases:
        cases.append(grid)

sys.stdout = open(os.path.join(evaldir, '2.in'), 'w', encoding='utf-8')
for grid in cases:
    print(f'>>> ships({grid!r})')
    print(repr(ships(grid)))
    print()

# ---------------------------------------------------------------------------
# function shoot
# ---------------------------------------------------------------------------

# each scenario shoots at the cells of a grid until every battleship is sunk,
# with shots at cells that are not on the grid mixed in
scenarios = [
    (['C1', 'A2', 'C3'], ['C1', 'C1', 'B2', 'A2', 'E1', 'C3']),
    (['B2'], ['A1', 'B1', 'C1', 'D1', 'A2', 'B2', 'B2']),
    ([], ['A1', 'D3', 'B2']),
    (['A1', 'D1', 'A3'], ['a1', 'A1', 'A1', 'D1', 'A3', 'A3']),
    (['A1', 'C1', 'A3', 'C3'], ['A4', 'A3', 'C3', 'C1', 'A1', 'B2']),
]
while len(scenarios) < 15:
    ships_placed = random.sample(CELLS, random.randint(1, 4))
    shots = []
    remaining = list(ships_placed)
    while remaining:
        choice = random.random()
        if choice < 0.15:
            shots.append(random.choice(INVALID_CELLS))
        elif choice < 0.55:
            shots.append(random.choice(CELLS))
        else:
            shots.append(random.choice(remaining))
        if shots[-1] in remaining:
            remaining.remove(shots[-1])
    scenarios.append((ships_placed, shots))

sys.stdout = open(os.path.join(evaldir, '3.in'), 'w', encoding='utf-8')
for index, (ships_placed, shots) in enumerate(scenarios):

    varname = f'grid_{index + 1:02d}'
    grid = make_grid(*ships_placed)
    print(f'>>> {varname} = {grid!r} # doctest: +NEWCONTEXT')

    print(f'>>> ships({varname})')
    print(repr(ships(grid)))

    for shot in shots:
        print(f'>>> shoot({varname}, {shot!r})')
        try:
            print(repr(shoot(grid, shot)))
        except Exception as e:
            print('Traceback (most recent call last):\n{}: {}'.format(e.__class__.__name__, e))

        print(f'>>> ships({varname})')
        print(repr(ships(grid)))

    print(f'>>> display_grid({varname}) # doctest: +STDOUT')
    display_grid(grid)

    print()
