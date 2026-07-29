import os
import sys
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

# pool of elements that can be pushed onto a queue
ELEMENTS = [
    'apple', 'pear', 'fig', 'plum', 'kiwi', 'mango', 'papaya', 'lychee',
    'quince', 'apricot', '42', 'x', 'the whole shebang', '???', '!',
    'Miss Marple', 'a?b', '3.14', 'multiple  spaces',
]

def statement(source, result=None, newcontext=False, stdout=False):

    """
    Emit a single doctest example: the statement, followed by the interactive
    echo of its return value (or by its captured output, if stdout is set).
    """

    options = []
    if newcontext:
        options.append('+NEWCONTEXT')
    if stdout:
        options.append('+STDOUT')
    comment = ' # doctest: ' + ' '.join(options) if options else ''

    print(f'>>> {source}{comment}')
    if result is not None:
        print(result)

# ---------------------------------------------------------------------------
# function push
# ---------------------------------------------------------------------------

# each scenario is an initial queue, followed by the elements that get pushed
cases = [
    ([], ['apple', 'pear', 'fig']),
    (['plum'], ['kiwi']),
    ([], ['the whole shebang']),
    (['a', 'b', 'c', 'd', 'e', 'f', 'g'], ['h', 'i']),
]
while len(cases) < 15:
    queue = random.sample(ELEMENTS, random.randint(0, 4))
    pushes = random.sample(ELEMENTS, random.randint(1, 5))
    cases.append((queue, pushes))

sys.stdout = open(os.path.join(evaldir, '0.in'), 'w', encoding='utf-8')
for index, (initial, pushes) in enumerate(cases):

    varname = f'queue_{index + 1:02d}'
    queue = list(initial)
    statement(f'{varname} = {initial!r}', newcontext=True)

    for element in pushes:
        push(queue, element)
        statement(f'push({varname}, {element!r})')
        statement(varname, repr(queue))

    print()

# ---------------------------------------------------------------------------
# function pop
# ---------------------------------------------------------------------------

# each scenario is an initial queue, followed by the number of times an element
# gets popped from that queue (which may be more often than there are elements)
cases = [
    (['apple', 'pear', 'fig'], 4),
    ([], 2),
    (['plum'], 1),
    (['a', 'b', 'c', 'd', 'e', 'f'], 3),
    (['???', '!', 'a?b'], 5),
]
while len(cases) < 15:
    queue = random.sample(ELEMENTS, random.randint(0, 6))
    cases.append((queue, random.randint(1, len(queue) + 2)))

sys.stdout = open(os.path.join(evaldir, '1.in'), 'w', encoding='utf-8')
for index, (initial, pops) in enumerate(cases):

    varname = f'queue_{index + 1:02d}'
    queue = list(initial)
    statement(f'{varname} = {initial!r}', newcontext=True)

    for _ in range(pops):
        element = pop(queue)
        statement(f'pop({varname})', repr(element) if element is not None else None)
        statement(varname, repr(queue))

    print()

# ---------------------------------------------------------------------------
# function process
# ---------------------------------------------------------------------------

cases = [
    ['apple', 'pear', '?', 'fig', '?', '?', '?', '', 'plum'],
    [''],
    [],
    ['?'],
    ['?', '?', '?'],
    ['apple', 'pear', 'fig'],
    ['apple', '?', '?', 'pear', '?'],
    ['???', '?', 'a?b', '?', '?'],
    ['', '?', 'apple'],
    ['multiple  spaces', '?', '?'],
]
while len(cases) < 20:
    lines = []
    for _ in range(random.randint(3, 12)):
        choice = random.random()
        if choice < 0.45:
            lines.append(random.choice(ELEMENTS))
        elif choice < 0.9:
            lines.append('?')
        else:
            lines.append('')
    if lines not in cases:
        cases.append(lines)

sys.stdout = open(os.path.join(evaldir, '2.in'), 'w', encoding='utf-8')
for lines in cases:

    print(f'>>> process({lines!r}) # doctest: +STDOUT')
    try:
        process(lines)
    except Exception as e:
        print('Traceback (most recent call last):\n{}: {}'.format(e.__class__.__name__, e))

    print()
