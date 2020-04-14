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
    [
        ('Monty Python and the Holy Grail', (9, 10, 9.5, 8.5, 3, 7.5, 8)),
        ("Monty Python's Life of Brian", (10, 10, 0, 9, 1, 8, 7.5, 8, 6, 9)),
        ("Monty Python's Meaning of Life", (7, 6, 5)),
        ('And Now For Something Completely Different', (6, 5, 6, 6)),
    ],
]

# generate unit tests for function list2dict
sys.stdout = open(os.path.join('..', 'evaluation', '0.in'), 'w', encoding='utf-8')
for movies_list in cases:

    # generate test expression
    print(f'>>> list2dict({movies_list!r})')

    # generate return value
    try:
        print(f'{list2dict(movies_list)!r}')
    except Exception as e:
        print('Traceback (most recent call last):\n{}: {}'.format(e.__class__.__name__, e))

    print()

# generate unit tests for function list2dict
sys.stdout = open(os.path.join('..', 'evaluation', '1.in'), 'w', encoding='utf-8')
for index, movies_list in enumerate(cases):

    # one-based indexing
    index += 1

    # generate test expression
    movies_dict = list2dict(movies_list)
    print(f'>>> movies_dict_{index:02d} = list2dict({movies_list!r}) # doctest: +NOEXEC')
    print(f'>>> movies_dict_{index:02d} = {movies_dict!r} # doctest: +NOSHOW')
    print(f'>>> list2dict(movies_dict_{index:02d})')

    # generate return value
    try:
        print(f'{average_rating(movies_dict)!r}')
    except Exception as e:
        print('Traceback (most recent call last):\n{}: {}'.format(e.__class__.__name__, e))

    print()
