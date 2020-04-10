import os
import sys
import importlib
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

# generate test data for function multiplication table
cases = list(range(0, 11))

# generate unit tests for function multiplication_table
sys.stdout = open(os.path.join('..', 'evaluation', '0.in'), 'w', encoding='utf-8')
for number in cases:

    # generate test expression
    print(f'>>> fib({number}, 0) # doctest: +RETURN +STDOUT')

    # generate return value
    try:
        print(f'{fib(number, 0)!r}')
    except Exception as e:
        print('Traceback (most recent call last):\n{}: {}'.format(e.__class__.__name__, e))

    print()
