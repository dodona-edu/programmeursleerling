import os
import sys
import importlib
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

# generate test data for function mode
cases = [
    [4, 8, 15, 16, 23, 8, 4, 8],
    [7, 2, 9, 2, 9, 3],
    [5, 10, 15],
    [-3, -3, 0, 0, 5, -3],
    [1],
    [2, 2, 2, 3, 3, 3],
    [],
]

# generate unit tests for function mode
sys.stdout = open(os.path.join('..', 'evaluation', '0.in'), 'w', encoding='utf-8')
for numbers in cases:

    # generate test expression
    print(f'>>> mode({numbers!r})')

    # generate return value
    try:
        print(f'{mode(numbers)!r}')
    except Exception as e:
        print('Traceback (most recent call last):\n{}: {}'.format(e.__class__.__name__, e))

    print()
