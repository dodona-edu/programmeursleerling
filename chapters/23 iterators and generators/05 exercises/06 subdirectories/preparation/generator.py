import os
import sys
import importlib.util
import random

# set fixed seed for generating test cases
random.seed(987654321)

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

# dictionaries whose sub-dictionaries are checked in full (kept to at most
# 4 key/value pairs so the expected output stays readable)
full_check_dicts = [
    {},
    {'a': 1},
    {'z': 7},
    {'a': 1, 'b': 2},
    {'p': 9, 'q': 4},
    {'x': 3, 'y': 8, 'z': 3},
    {'red': 1, 'green': 2, 'blue': 3},
    {'a': 5, 'b': 5, 'c': 5, 'd': 5},
    {'k1': 10, 'k2': 20, 'k3': 30, 'k4': 40},
]

# dictionaries for which only the number of sub-dictionaries is checked
length_check_dicts = [
    {},
    {'p': 9, 'q': 4},
    {'k1': 10, 'k2': 20, 'k3': 30, 'k4': 40},
    {f'key{i}': i * i for i in range(5)},
    {f'key{i}': i * i for i in range(8)},
    {f'key{i}': i * i for i in range(10)},
]

# generate unit tests for function sub_dictionaries
sys.stdout = open(os.path.join('..', 'evaluation', '0.in'), 'w', encoding='utf-8')

for dictionary in full_check_dicts:

    # generate test expression
    print(f'>>> sorted(sorted(sub.items()) for sub in sub_dictionaries({dictionary!r}))')

    # generate return value
    normalised = sorted(sorted(sub.items()) for sub in sub_dictionaries(dictionary))
    print(f'{normalised!r}')

    print()

for dictionary in length_check_dicts:

    # generate test expression
    print(f'>>> len(sub_dictionaries({dictionary!r}))')

    # generate return value
    print(f'{len(sub_dictionaries(dictionary))}')

    print()
