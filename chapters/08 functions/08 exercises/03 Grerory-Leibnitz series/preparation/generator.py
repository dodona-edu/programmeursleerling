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

# generate test data for function gregory_leibnitz
cases = [1, 10, 100, 1000, 10000]
while len(cases) < 50:
    number = random.randint(1, 100000)
    if number not in cases:
        cases.append(number)
cases.sort()

# generate unit tests for function gregory_leibnitz
sys.stdout = open(os.path.join('..', 'evaluation', '0.in'), 'w', encoding='utf-8')
for terms in cases:

    # generate test expression
    print(f'>>> gregory_leibnitz({terms})')

    # generate return value
    try:
        print(f'{gregory_leibnitz(terms)}')
    except Exception as e:
        print('Traceback (most recent call last):\n{}: {}'.format(e.__class__.__name__, e))

    print()
