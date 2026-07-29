import sys
import random
import importlib.util
from test_utils import *

# set fixed seed for generating test cases
random.seed(21010729)

# exercise directories
evaldir = create_dir('..', 'evaluation')         # evaluation
solutiondir = create_dir('..', 'solution')       # solution

# load functionality defined in sample solution
module_name = 'solution'
file_path = os.path.join(solutiondir, 'solution.en.py')
spec = importlib.util.spec_from_file_location(module_name, file_path)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

for name in dir(module):
    if not (name.startswith('__') and name.endswith('__')):
        globals()[name] = eval(f'module.{name}')

OPERATORS = ('==', '!=', '<', '<=', '>', '>=')

def test_operator(left_name, left, operator, right_name, right):

    """
    Emit a doctest example that applies a binary operator on two cards, so
    that the overloaded operator itself is exercised (and not some named
    method that happens to implement it).
    """

    print(f'>>> {left_name} {operator} {right_name}')
    print(repr(eval(f'left {operator} right')))

def random_card():

    return (random.choice(SUITS), random.choice(RANKS))

# ---------------------------------------------------------------------------
# class Card: construction and string conversion
# ---------------------------------------------------------------------------

# cards covering both ends of the rank order, the switch from numeric to
# named ranks, and every suit
cases = [
    ('Hearts', 'Ace'),
    ('Spades', 2),
    ('Clubs', 10),
    ('Diamonds', 'Jack'),
    ('Hearts', 'Queen'),
    ('Clubs', 'King'),
    ('Diamonds', 7),
    ('Spades', 9),
]
while len(cases) < 16:
    case = random_card()
    if case not in cases:
        cases.append(case)

# invalid cards: unknown suit, unknown rank, rank 1 (no ace as a number),
# rank as a string, lowercase suit
invalid = [
    ('Trees', 7),
    ('Hearts', 1),
    ('Diamonds', 'Joker'),
    ('hearts', 'Ace'),
    ('Spades', '9'),
]

sys.stdout = open(os.path.join(evaldir, '0.in'), 'w', encoding='utf-8')

for index, (suit, rank) in enumerate(cases):

    varname = f'card_{index + 1:02d}'
    obj = test_instantiation(Card, suit, rank, varname=varname)

    tests = ['repr', 'str']
    if index:
        random.shuffle(tests)

    for test in tests:
        if test == 'repr':
            test_repr(obj, varname=varname, call=None if index else False)
        else:
            test_str(obj, varname=varname, call=None if index else False)

    print()

for index, (suit, rank) in enumerate(invalid):

    varname = f'card_{len(cases) + index + 1:02d}'
    try:
        test_instantiation(Card, suit, rank, varname=varname)
    except Exception as e:
        print('Traceback (most recent call last):\n{}: {}'.format(
            e.__class__.__name__, e
        ))

    print()

# ---------------------------------------------------------------------------
# class Card: comparison operators
# ---------------------------------------------------------------------------

# pairs covering the extremes of the rank order, the boundary between the
# numeric and the named ranks, equal ranks with different suits, and two
# references to a card of the very same suit and rank
pairs = [
    (('Hearts', 'Ace'), ('Spades', 2)),
    (('Clubs', 10), ('Diamonds', 'Jack')),
    (('Hearts', 'King'), ('Clubs', 'King')),
    (('Spades', 7), ('Spades', 7)),
    (('Diamonds', 'Queen'), ('Hearts', 'King')),
    (('Clubs', 3), ('Clubs', 9)),
    (('Spades', 'Ace'), ('Diamonds', 'Ace')),
    (('Hearts', 2), ('Clubs', 3)),
]
while len(pairs) < 16:
    pairs.append((random_card(), random_card()))

sys.stdout = open(os.path.join(evaldir, '1.in'), 'w', encoding='utf-8')

for index, (left, right) in enumerate(pairs):

    left_name = f'card_{3 * index + 1:02d}'
    right_name = f'card_{3 * index + 2:02d}'

    left_card = test_instantiation(Card, *left, varname=left_name)
    right_card = test_instantiation(
        Card, *right, varname=right_name, newcontext=False
    )

    # all six comparison operators, in a shuffled order for every pair but
    # the first one
    operators = list(OPERATORS)
    if index:
        random.shuffle(operators)

    for operator in operators:
        test_operator(left_name, left_card, operator, right_name, right_card)

    # the operators are also what min, max and sorted rely on
    third = random_card()
    while third[1] in (left[1], right[1]):
        third = random_card()

    third_name = f'card_{3 * index + 3:02d}'
    third_card = test_instantiation(
        Card, *third, varname=third_name, newcontext=False
    )

    cards = [left_card, right_card, third_card]
    names = [left_name, right_name, third_name]

    extras = ['sorted', 'max', 'min', 'chain']
    if index:
        random.shuffle(extras)

    for extra in extras:
        if extra == 'sorted':
            print(f'>>> sorted([{", ".join(names)}]) # doctest: +REPR')
            print(repr(sorted(cards)))
        elif extra == 'max':
            print(f'>>> max({", ".join(names)}) # doctest: +REPR')
            print(repr(max(*cards)))
        elif extra == 'min':
            print(f'>>> min({", ".join(names)}) # doctest: +REPR')
            print(repr(min(*cards)))
        else:
            print(f'>>> {left_name} <= {right_name} <= {third_name}')
            print(repr(left_card <= right_card <= third_card))

    print()
