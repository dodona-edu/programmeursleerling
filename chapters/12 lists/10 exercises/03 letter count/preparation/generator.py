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

# handpicked test cases that cover the boundary conditions: no letters at all,
# a single letter, letters that only differ in case, and lots of ties that can
# only be broken alphabetically
cases = [
    'Hello, World!',
    '',
    '   ',
    '12345 + 67890 = ?',
    'z',
    'ZzZzZ',
    'aA bB cC',
    'The quick brown fox jumps over the lazy dog.',
    'abcdefghijklmnopqrstuvwxyz',
    'Mississippi',
    "It's a UNIX system! I know this!",
    'A man, a plan, a canal: Panama',
    'x' * 37,
    'Portez ce vieux whisky au juge blond qui fume',
    'Als de kat van huis is, dansen de muizen op tafel.',
    'aabbccddee',
    'tic-tac-toe',
    '3.14159265358979',
    'Sphinx of black quartz, judge my vow',
    'wxyz WXYZ wxy WX w',
]

# add randomly assembled sentences so the expected output cannot be looked up
words = [
    'lorem', 'ipsum', 'dolor', 'sit', 'amet', 'consectetur', 'adipiscing',
    'elit', 'sed', 'do', 'eiusmod', 'tempor', 'incididunt', 'ut', 'labore',
    'magna', 'aliqua', 'enim', 'minim', 'veniam', 'quis', 'nostrud',
]
punctuation = ['.', '!', '?', ',', ';', ' ', '...', '-']
while len(cases) < 40:
    sentence = ' '.join(
        random.choice(words).upper() if random.random() < 0.3 else random.choice(words)
        for _ in range(random.randint(1, 9))
    ) + random.choice(punctuation)
    if sentence not in cases:
        cases.append(sentence)

# generate unit tests for function letter_count
sys.stdout = open(os.path.join(evaldir, '0.in'), 'w', encoding='utf-8')
for text in cases:

    # generate test expression
    print(f'>>> letter_count({text!r}) # doctest: +STDOUT')

    # generate expected output
    try:
        letter_count(text)
    except Exception as e:
        print('Traceback (most recent call last):\n{}: {}'.format(e.__class__.__name__, e))

    print()
