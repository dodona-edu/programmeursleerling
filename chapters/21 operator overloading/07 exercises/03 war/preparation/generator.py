import sys
import random
import importlib.util
from test_utils import *

# set fixed seed for generating test cases
random.seed(21030729)

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
    (('Diamonds', 2), ('Hearts', 'King')),
    (('Clubs', 7), ('Spades', 8)),
    (('Hearts', 'Ace'), ('Diamonds', 'Ace')),
    (('Spades', 10), ('Clubs', 'Jack')),
]
while len(cases) < 8:
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

# ---------------------------------------------------------------------------
# class Drawpile (needed again for this exercise, so it is tested again)
# ---------------------------------------------------------------------------

scenarios = [
    [Card('Diamonds', 2), Card('Hearts', 'King'), Card('Clubs', 7)],
    [],
    [Card('Hearts', 4), Card('Hearts', 3), Card('Spades', 8)],
]
while len(scenarios) < 8:
    scenarios.append([random_card() for _ in range(random.randint(2, 5))])

sys.stdout = open(os.path.join(evaldir, '1.in'), 'w', encoding='utf-8')

for index, cards in enumerate(scenarios):

    varname = f'pile_{index + 1:02d}'
    pile = test_instantiation(Drawpile, cards, varname=varname)

    tests = ['repr', 'len', 'getitem', 'add', 'draw']
    if index:
        random.shuffle(tests)

    for test in tests:

        if test == 'repr':
            test_repr(pile, varname=varname, call=False)

        elif test == 'len':
            print(f'>>> len({varname})')
            print(repr(len(pile)))

        elif test == 'getitem':
            if len(pile) == 0:
                continue
            position = random.randrange(len(pile))
            print(f'>>> {varname}[{position}] # doctest: +REPR')
            print(repr(pile[position]))

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

    test_repr(pile, varname=varname, call=False)

    print()

# ---------------------------------------------------------------------------
# function war
# ---------------------------------------------------------------------------

def play(cards_1, cards_2, swapped=False, limit=1000):

    """
    Play a game on a copy of the two piles, so that the generator can check
    beforehand that the game actually ends. Returns the number of rounds, or
    None if the game did not end within the given number of rounds.

    With swapped=True the two cards of a round are picked up in the wrong
    order (the losing card first). That is the most common way to get this
    exercise subtly wrong, and it easily turns a game into an endless one, so
    the generated games are picked such that they also end that way. A
    student making that mistake then gets a wrong answer to look at instead
    of an unhelpful time limit exceeded.
    """

    pile_1 = Drawpile(list(cards_1))
    pile_2 = Drawpile(list(cards_2))

    rounds = 0
    while len(pile_1) > 0 and len(pile_2) > 0:
        if rounds >= limit:
            return None
        rounds += 1
        card_1, card_2 = pile_1.draw(), pile_2.draw()
        winner, cards = (
            (pile_1, [card_1, card_2]) if card_1 > card_2
            else (pile_2, [card_2, card_1])
        )
        if swapped:
            cards.reverse()
        for card in cards:
            winner.add(card)

    return rounds

def random_game():

    """
    Deal cards with pairwise different ranks over two piles, so that the
    special rules for equal ranks never come into play, and only keep games
    that actually end.
    """

    while True:

        size = random.randint(4, 9)
        ranks = random.sample(RANKS, size)
        cards = [Card(random.choice(SUITS), rank) for rank in ranks]
        split = random.randint(1, size - 1)
        cards_1, cards_2 = cards[:split], cards[split:]

        if (
            play(cards_1, cards_2) is not None
            and
            play(cards_1, cards_2, swapped=True) is not None
        ):
            return cards_1, cards_2

# two short games that already tell apart the order in which the winner of a
# round picks up the two cards, then the game from the assignment, then the
# boundary cases (an empty pile on either side, a single card on either side,
# and a pile holding the ace that can never be beaten)
games = [
    (
        [Card('Hearts', 'Jack'), Card('Diamonds', 3)],
        [Card('Diamonds', 6)],
    ),
    (
        [Card('Hearts', 3), Card('Diamonds', 7)],
        [Card('Spades', 2), Card('Diamonds', 'Queen'), Card('Hearts', 'Jack')],
    ),
    (
        [Card('Diamonds', 2), Card('Hearts', 'King'), Card('Clubs', 7)],
        [Card('Hearts', 4), Card('Hearts', 3), Card('Spades', 8)],
    ),
    ([], [Card('Clubs', 9), Card('Diamonds', 'Queen')]),
    ([Card('Spades', 6), Card('Hearts', 'Jack')], []),
    ([Card('Hearts', 5)], [Card('Spades', 'Jack')]),
    ([Card('Diamonds', 'Ace')], [Card('Clubs', 'King'), Card('Hearts', 4)]),
    (
        [Card('Clubs', 'Ace'), Card('Spades', 3)],
        [Card('Diamonds', 'Queen'), Card('Hearts', 8), Card('Spades', 5)],
    ),
]
while len(games) < 14:
    games.append(random_game())

sys.stdout = open(os.path.join(evaldir, '2.in'), 'w', encoding='utf-8')

for index, (cards_1, cards_2) in enumerate(games):

    name_1 = f'pile_{2 * index + 1:02d}'
    name_2 = f'pile_{2 * index + 2:02d}'

    pile_1 = test_instantiation(Drawpile, cards_1, varname=name_1)
    pile_2 = test_instantiation(
        Drawpile, cards_2, varname=name_2, newcontext=False
    )

    print(f'>>> winner = war({name_1}, {name_2})')
    winner = war(pile_1, pile_2)

    tests = ['identity', 'winner', 'len_1', 'len_2']
    if index:
        random.shuffle(tests)

    for test in tests:

        if test == 'identity':
            print(f'>>> winner is {name_1}')
            print(repr(winner is pile_1))
            print(f'>>> winner is {name_2}')
            print(repr(winner is pile_2))
        elif test == 'winner':
            print('>>> winner # doctest: +REPR')
            print(repr(winner))
        elif test == 'len_1':
            print(f'>>> len({name_1})')
            print(repr(len(pile_1)))
        else:
            print(f'>>> len({name_2})')
            print(repr(len(pile_2)))

    print()
