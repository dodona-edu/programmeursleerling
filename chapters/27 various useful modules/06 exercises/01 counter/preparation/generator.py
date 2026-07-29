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

# generate test data for function most_common_letters
cases = [
    'mississippi',
    'The quick brown fox jumps over the lazy dog, again and again!',
    'AaAaBbBcCcC',
    'Hello, World! 2024 edition.',
    '',
]

# generate unit tests for function most_common_letters
sys.stdout = open(os.path.join('..', 'evaluation', '0.in'), 'w', encoding='utf-8')
for text in cases:

    # generate test expression
    print(f'>>> most_common_letters({text!r})')

    # generate return value
    try:
        print(f'{most_common_letters(text)!r}')
    except Exception as e:
        print('Traceback (most recent call last):\n{}: {}'.format(e.__class__.__name__, e))

    print()
