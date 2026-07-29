import os
import sys
import importlib
import importlib.util
import random

# set fixed seed for generating test cases
random.seed(20260729)

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

# fixed cases covering the required corner cases: no divisors, a single
# divisor, several divisors, a divisor of 1 (empty result), a divisor
# larger than 100, overlapping/duplicate divisors and larger primes
fixed_cases = [
    [7, 11],
    [],
    [1],
    [137],
    [4, 4, 6, 6],
    [83, 89, 97],
    [12, 18, 30],
    [13, 13, 13],
    [100],
    [99, 98],
    [2, 1000000007],
]

# a couple of extra, randomly generated cases with varied, non-round
# divisors, to avoid the whole test suite being guessable from a lookup
# table
random_cases = []
while len(random_cases) < 3:
    size = random.randint(1, 4)
    divisors = sorted(random.sample(range(2, 100), size))
    if divisors not in fixed_cases and divisors not in random_cases:
        random_cases.append(divisors)

cases = fixed_cases + random_cases

# generate unit tests for function not_divisible
sys.stdout = open(os.path.join('..', 'evaluation', '0.in'), 'w', encoding='utf-8')
for divisors in cases:

    # generate test expression
    print(f'>>> list(not_divisible({divisors}))')

    # generate return value
    try:
        print(f'{list(not_divisible(divisors))}')
    except Exception as e:
        print('Traceback (most recent call last):\n{}: {}'.format(e.__class__.__name__, e))

    print()

# generate a test case that proves the function is a lazy generator: it
# binds the result to a variable, pulls a couple of values with next(),
# and only then drains the rest with list()
divisors = [6, 35]
print(f'>>> g = not_divisible({divisors})')
print()
gen = not_divisible(divisors)
for _ in range(3):
    print('>>> next(g)')
    print(f'{next(gen)}')
    print()
print('>>> list(g)')
print(f'{list(gen)}')
