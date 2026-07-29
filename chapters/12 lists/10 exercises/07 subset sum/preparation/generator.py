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

# read the custom output processor that checks the return value; the subset
# that solves the problem is not unique, so the return value of the submitted
# solution cannot simply be compared to the one of the sample solution
with open('subsetchecker.py', 'r', encoding='utf-8') as handle:
    CHECKER = handle.read().strip()

# handpicked test cases that cover the boundary conditions: no numbers at all,
# a single number, a single zero, duplicate numbers and numbers that only add
# up to zero if every single one of them is used
cases = [
    [1, 4, -3, -5, 7],
    [1, 4, -3, 7],
    [],
    [0],
    [13],
    [-13],
    [6, -6],
    [6, 6, -6],
    [-8, 3, 5],
    [-8, 3, 6],
    [17, -4, -4, -4, -4, -1],
    [2, 4, 8, 16, 32, 64, -126],
    [2, 4, 8, 16, 32, 64, -127],
    [0, 0],
    [-1, -2, -3, -4, -5],
    [1, 2, 3, 4, 5],
    [-19, 7, 7, 7, -2],
]

# add randomly generated lists, keeping solvable and unsolvable ones balanced;
# the lists stay short enough for an exhaustive search to remain fast
solvable = unsolvable = 0
while solvable + unsolvable < 33:
    size = random.randint(1, 14)
    spread = random.choice((3, 7, 20, 60, 250))
    numbers = [random.randint(-spread, spread) for _ in range(size)]
    if numbers in cases:
        continue
    if subset_sum(numbers) is None:
        if unsolvable == 16:
            continue
        unsolvable += 1
    else:
        if solvable == 17:
            continue
        solvable += 1
    cases.append(numbers)

# generate unit tests for function subset_sum
sys.stdout = open(os.path.join(evaldir, '0.in'), 'w', encoding='utf-8')
for numbers in cases:

    # generate test expression
    print(f'>>> subset_sum({numbers!r})')

    solution = subset_sum(numbers)

    if solution is not None:

        # define custom checker
        print('<DEFINITION>')
        print(CHECKER)
        print('</DEFINITION>')

        # call custom checker
        print('<OUTPUTPROCESSOR>')
        print(f'SubsetChecker(expected_type=[int], numbers={numbers!r})')
        print('</OUTPUTPROCESSOR>')

        # generate return value
        print(f'{solution}')

    print()
