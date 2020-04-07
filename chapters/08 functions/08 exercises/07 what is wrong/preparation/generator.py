import os
import sys
import imp
import random
import string

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
solution = imp.load_source(
    'solution',
    os.path.join(solutiondir, 'solution.en.py')
)
for name in dir(solution):
    if not (name.startswith('__') and name.endswith('__')):
        globals()[name] = eval('solution.{}'.format(name))

# generate test data for function area_of_triangle
cases = [(4.5, 1.0)]
max_value = 50
while len(cases) < 50:
    if random.choice((True, False)):
        n = float(random.randint(1, max_value))
    else:
        n = random.randint(1, 2 * max_value) / 2
    if random.choice((True, False)):
        k = float(random.randint(1, max_value))
    else:
        k = random.randint(1, 2 * max_value) / 2
    if (n, k) not in cases:
        cases.append((n, k))

# generate unit tests for function area_of_triangle
sys.stdout = open(os.path.join('..', 'evaluation', '0.in'), 'w', encoding='utf-8')
for n, k in cases:

    # generate test expression
    print(f'>>> print(area_of_triangle({n}, {k})) # doctest: +STDOUT')

    # generate return value
    try:
        print(f'{area_of_triangle(n, k)}')
    except Exception as e:
        print('Traceback (most recent call last):\n{}: {}'.format(e.__class__.__name__, e))

    print()
