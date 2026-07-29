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

# Every test case is a list of one or more Python statements/expressions
# (REPL lines). All cases share a single namespace across the whole file,
# so a case can bind a generator to a variable and then advance it with
# next() in a later line. The solution's results depend on the order in
# which permutations() produces candidate boards, so every expression
# below is written to be independent of that order (sorted/len/min/max/in).
cases = [
    ['sorted(queens(1))'],
    ['sorted(queens(2))'],
    ['sorted(queens(3))'],
    ['sorted(queens(4))'],
    ['sorted(queens(5))'],
    ['sorted(queens(6))'],
    ['len(list(queens(7)))'],
    ['len(list(queens(8)))'],
    ['len(list(queens(9)))'],
    ['len(list(queens()))'],
    ['min(queens(8))'],
    ['max(queens(8))'],
    ['(3, 1, 6, 2, 5, 7, 4, 0) in list(queens(8))'],
    [
        'g = queens(4)',
        's = next(g)',
        'sorted(s) == sorted(range(4))',
        's2 = next(g)',
        'sorted(s2) == sorted(range(4))',
        's == s2',
    ],
]

# shared namespace, reused (and mutated) across every case in the file
namespace = dict(globals())

# generate unit tests for function queens
sys.stdout = open(os.path.join('..', 'evaluation', '0.in'), 'w', encoding='utf-8')
for case in cases:
    for line in case:

        # generate test expression
        print(f'>>> {line}')

        # generate return value
        try:
            try:
                result = eval(line, namespace)
            except SyntaxError:
                # not an expression (e.g. an assignment): execute it instead
                exec(line, namespace)
                result = None
            if result is not None:
                print(repr(result))
        except Exception as e:
            print('Traceback (most recent call last):\n{}: {}'.format(e.__class__.__name__, e))

        print()
