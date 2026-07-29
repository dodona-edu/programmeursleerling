import os
import sys
import importlib.util
import traceback

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

# shared namespace, mirroring the shared namespace the doctest judge uses for
# every example in a single .in file
namespace = {'factorials': module.factorials}


def run_statement(statement, namespace):

    """
    Execute a single REPL-style statement in the given namespace, and return
    its interactive return echo (as a repr string) or its reduced traceback
    (as a two-line string), mirroring what the doctest judge expects.
    Statements that return None (e.g. assignments) produce neither.
    """

    try:
        code = compile(statement, '<doctest>', 'eval')
    except SyntaxError:
        code = compile(statement, '<doctest>', 'exec')
        try:
            exec(code, namespace)
        except Exception as e:
            return None, format_exception(e)
        return None, None

    try:
        result = eval(code, namespace)
    except Exception as e:
        return None, format_exception(e)

    return result, None


def format_exception(e):
    lines = traceback.format_exception_only(type(e), e)
    message = ''.join(lines).strip('\n')
    return 'Traceback (most recent call last):\n{}'.format(message)


# each test case is a list of statements executed in sequence, sharing the
# single namespace above; a blank line in the .in file separates cases
cases = [
    ['list(factorials())'],
    ['list(factorials(0))'],
    ['list(factorials(1))'],
    ['list(factorials(7))'],
    ['list(factorials(13))'],
    ['list(factorials(17))'],
    ['list(factorials(23))'],
    ['list(factorials(40))'],
    [
        'g = factorials(5)',
        'next(g)',
        'next(g)',
        'next(g)',
        'list(g)',
    ],
    [
        'g = factorials(10)',
        'next(g)',
        'next(g)',
        'list(g)',
    ],
    [
        'g1 = factorials(4)',
        'g2 = factorials(4)',
        'next(g1)',
        'next(g1)',
        'next(g2)',
        'list(g1)',
        'list(g2)',
    ],
    [
        'g = factorials(0)',
        'next(g)',
    ],
]

# generate unit tests for the factorials generator
sys.stdout = open(os.path.join('..', 'evaluation', '0.in'), 'w', encoding='utf-8')
for case in cases:

    for statement in case:

        # generate test expression
        print(f'>>> {statement}')

        # generate return value or exception
        result, exc_text = run_statement(statement, namespace)
        if exc_text is not None:
            print(exc_text)
        elif result is not None:
            print(f'{result!r}')

    print()
