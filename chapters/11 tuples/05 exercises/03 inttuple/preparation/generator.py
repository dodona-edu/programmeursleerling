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

# helper function for generating inttuples
def generate_inttuples():

    next_value = [0]

    def int_or_tuple(probability=0.5):
        if random.random() <= probability:
            return tuple(int_or_tuple(probability ** 2) for _ in range(2, 5))
        else:
            next_value[0] += 1
            return next_value[0]

    return tuple(int_or_tuple(0.25 + 0.5 * random.random()) for _ in range(2, 5))

# generate test data for function multiplication table
cases = [
    (1, 2, (3, 4), 5, ((6, 7, 8, (9, 10), 11), 12, 13), ((14, 15, 16), (17, 18, 19, 20))),
]
while len(cases) < 50:
    inttuple = generate_inttuples()
    if inttuple not in cases:
        cases.append(inttuple)

# generate unit tests for function flatten
sys.stdout = open(os.path.join('..', 'evaluation', '0.in'), 'w', encoding='utf-8')
for inttuple in cases:

    # generate test expression
    print(f'>>> flatten({inttuple})')

    # generate return value
    try:
        print(f'{flatten(inttuple)}')
    except Exception as e:
        print('Traceback (most recent call last):\n{}: {}'.format(e.__class__.__name__, e))

    print()
