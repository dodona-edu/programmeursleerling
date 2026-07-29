import sys
import random
import importlib.util
from test_utils import *

# set fixed seed for generating test cases
random.seed(21020729)

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

def random_card():

    return Card(random.choice(SUITS), random.choice(RANKS))

def test_operator(left_name, left, operator, right_name, right):

    print(f'>>> {left_name} {operator} {right_name}')
    print(repr(eval(f'left {operator} right')))

# ---------------------------------------------------------------------------
# class Card (needed again for this exercise, so it is tested again)
# ---------------------------------------------------------------------------

cases = [
    (('Hearts', 'Ace'), ('Spades', 2)),
    (('Clubs', 10), ('Diamonds', 'Jack')),
    (('Hearts', 'King'), ('Clubs', 'King')),
    (('Diamonds', 'Queen'), ('Spades', 6)),
]
while len(cases) < 10:
    cases.append((
        (random.choice(SUITS), random.choice(RANKS)),
        (random.choice(SUITS), random.choice(RANKS)),
    ))

sys.stdout = open(os.path.join(evaldir, '0.in'), 'w', encoding='utf-8')

for index, (left, right) in enumerate(cases):

    left_name = f'card_{2 * index + 1:02d}'
    right_name = f'card_{2 * index + 2:02d}'

    left_card = test_instantiation(Card, *left, varname=left_name)
    right_card = test_instantiation(
        Card, *right, varname=right_name, newcontext=False
    )

    tests = ['repr', 'str'] + list(OPERATORS)
    if index:
        random.shuffle(tests)

    for test in tests:
        if test == 'repr':
            test_repr(left_card, varname=left_name, call=None if index else False)
        elif test == 'str':
            test_str(right_card, varname=right_name, call=None if index else False)
        else:
            test_operator(left_name, left_card, test, right_name, right_card)

    print()

# an invalid card must still be rejected
for index, (suit, rank) in enumerate((('Trees', 7), ('Hearts', 'Joker'))):

    varname = f'card_{2 * len(cases) + index + 1:02d}'
    try:
        test_instantiation(Card, suit, rank, varname=varname)
    except Exception as e:
        print('Traceback (most recent call last):\n{}: {}'.format(
            e.__class__.__name__, e
        ))

    print()

# ---------------------------------------------------------------------------
# class Drawpile
# ---------------------------------------------------------------------------

# the first scenarios cover the boundary cases: an empty pile (drawing from
# it must yield None), a pile with a single card that gets drained, and the
# two piles of the "War!" exercise that follows
scenarios = [
    [Card('Hearts', 4), Card('Clubs', 7), Card('Spades', 'Queen')],
    [],
    [Card('Diamonds', 'Ace')],
    [Card('Diamonds', 2), Card('Hearts', 'King'), Card('Clubs', 7)],
    [Card('Hearts', 4), Card('Hearts', 3), Card('Spades', 8)],
]
while len(scenarios) < 14:
    scenarios.append([random_card() for _ in range(random.randint(2, 6))])

sys.stdout = open(os.path.join(evaldir, '1.in'), 'w', encoding='utf-8')

for index, cards in enumerate(scenarios):

    varname = f'pile_{index + 1:02d}'
    pile = test_instantiation(Drawpile, cards, varname=varname)

    tests = ['repr', 'str', 'len', 'getitem', 'compare', 'add', 'draw']
    if index:
        random.shuffle(tests)

    # always end on a full picture of the pile, so that every mutation done
    # along the way is checked
    tests = tests + ['repr']

    for test in tests:

        if test == 'repr':
            test_repr(pile, varname=varname, call=False)

        elif test == 'str':
            test_str(pile, varname=varname, call=True)

        elif test == 'len':
            print(f'>>> len({varname})')
            print(repr(len(pile)))

        elif test == 'getitem':
            if len(pile) == 0:
                continue
            for position in sorted(random.sample(
                range(len(pile)), min(2, len(pile))
            )):
                print(f'>>> {varname}[{position}] # doctest: +REPR')
                print(repr(pile[position]))

        elif test == 'compare':
            if len(pile) < 2:
                continue
            first, second = sorted(random.sample(range(len(pile)), 2))
            operator = random.choice(OPERATORS)
            test_operator(
                f'{varname}[{first}]', pile[first],
                operator,
                f'{varname}[{second}]', pile[second],
            )

        elif test == 'add':
            card = random_card()
            print(f'>>> {varname}.add({card!r})')
            pile.add(card)

        else:
            print(f'>>> {varname}.draw()'
                  + (' # doctest: +REPR' if len(pile) else ''))
            card = pile.draw()
            if card is not None:
                print(repr(card))

    # drain what is left of the pile, one card at a time, and check that
    # drawing from the empty pile yields None
    while len(pile):
        print(f'>>> {varname}.draw() # doctest: +REPR')
        print(repr(pile.draw()))
    print(f'>>> len({varname})')
    print(repr(len(pile)))
    print(f'>>> {varname}.draw()')
    pile.draw()

    print()
