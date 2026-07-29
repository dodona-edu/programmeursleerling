import os
import sys
import importlib
import importlib.util

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

# handcrafted test cases for zero_subsets, all with distinct values so
# that the result is unambiguous regardless of which indices a correct
# solution happens to pick; every case is checked for repeated values
cases = [
    [],
    [0],
    [5],
    [-5],
    [1, 4, -3, 7],
    [1, 4, -3, -5, 7],
    [1, 2, 3, 4, 5],
    [-1, -2, -3, -4],
    [1, -1],
    [1, -1, 2, -2, 3, -3],
    [0, 1, -1],
    [10, -3, -7, 15, -100, 85],
    [2, 4, 6, 8, 10, -30],
    [3, 5, -8, 100],
    [6, -2, -4, 9, -11, 2, 100],
    [1, 2, 3, -6, 4, -5, 12, -11],
    [50, -20, -30, 17, -17, 8],
    [0, 5, -5, 3, -3, 100],
    [7, -7, 0],
    [1, 3, 5, 7, 9, 11],
    [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, -2047],
]

for numbers in cases:
    assert len(numbers) == len(set(numbers)), f'repeated value in {numbers}'
    assert len(numbers) <= 12, f'list too long for exhaustive search: {numbers}'

# generate unit tests for function zero_subsets
sys.stdout = open(os.path.join('..', 'evaluation', '0.in'), 'w', encoding='utf-8')

for numbers in cases:

    # generate test expression
    print(f'>>> sorted(zero_subsets({numbers!r}))')

    # generate return value
    print(f'{sorted(zero_subsets(numbers))!r}')

    print()

# a couple of cases that bind the generator to a variable, to show that
# it is lazy, and that answer the "is there a solution at all?" question
# without generating every solution first

print(f'>>> g = zero_subsets({[4, 9, -13, 20]!r})')
print()

g = zero_subsets([4, 9, -13, 20])
print('>>> next(g, None)')
print(f'{next(g, None)!r}')
print()

print('>>> next(g, None)')
print(f'{next(g, None)!r}')
print()

print(f'>>> g = zero_subsets({[2, 4, 8, 16]!r})')
print()

g = zero_subsets([2, 4, 8, 16])
print('>>> next(g, None)')
print(f'{next(g, None)!r}')
print()

print(f'>>> any(zero_subsets({[1, 4, -3, -5, 7]!r}))')
print(f'{any(zero_subsets([1, 4, -3, -5, 7]))!r}')
print()

print(f'>>> any(zero_subsets({[1, 4, -3, 7]!r}))')
print(f'{any(zero_subsets([1, 4, -3, 7]))!r}')
