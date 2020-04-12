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

# generate unit test for function deck
sys.stdout = open(os.path.join('..', 'evaluation', '0.in'), 'w', encoding='utf-8')

# generate test expression
print(f'>>> deck()')

# define custom checker
print('<DEFINITION>')
handle = open('deckchecker.py', 'r')
print(handle.read().strip())
handle.close()
print('</DEFINITION>')

# call custom checker
print('<OUTPUTPROCESSOR>')
print('DeckChecker(expected_type=[str])')
print('</OUTPUTPROCESSOR>')

# generate return value
try:
    print(f'{deck()}')
except Exception as e:
    print('Traceback (most recent call last):\n{}: {}'.format(e.__class__.__name__, e))
