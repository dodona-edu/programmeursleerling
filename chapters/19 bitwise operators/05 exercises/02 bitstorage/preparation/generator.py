import os
import sys
import random
import importlib

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

# generate test data for functions discriminant and solutions
cases = [
    (n, random.randrange(8), random.choice((True, False)))
    for n in random.sample(list(range(256)), 50)
]

# generate unit tests for function setbit
sys.stdout = open(os.path.join('..', 'evaluation', '0.in'), 'w', encoding='utf-8')
for n, i, b in cases:

    # generate test expression
    print(f'>>> setbit({n}, {i}, {b})')

    # generate return value
    try:
        print(f'{setbit(n, i, b)}')
    except Exception as e:
        print('Traceback (most recent call last):\n{}: {}'.format(e.__class__.__name__, e))

    print()

# generate unit tests for function getbit
sys.stdout = open(os.path.join('..', 'evaluation', '1.in'), 'w', encoding='utf-8')
for n, i, b in cases:

    # generate test expression
    print(f'>>> getbit({n}, {i})')

    # generate return value
    try:
        print(f'{getbit(n, i)}')
    except Exception as e:
        print('Traceback (most recent call last):\n{}: {}'.format(e.__class__.__name__, e))

    print()

# generate unit tests for function bitstring
sys.stdout = open(os.path.join('..', 'evaluation', '2.in'), 'w', encoding='utf-8')
for n, i, b in cases:

    # generate test expression
    print(f'>>> bitstring({n})')

    # generate return value
    try:
        print(f'{bitstring(n)!r}')
    except Exception as e:
        print('Traceback (most recent call last):\n{}: {}'.format(e.__class__.__name__, e))

    print()
