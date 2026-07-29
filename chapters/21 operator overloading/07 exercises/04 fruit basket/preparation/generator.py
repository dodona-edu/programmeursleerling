import sys
import random
import importlib.util
from test_utils import *

# set fixed seed for generating test cases
random.seed(21040729)

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

# fruits whose name is spelled the same in English and in Dutch, so that the
# test data does not have to be translated along with the class name
FRUITS = (
    'mango', 'kiwi', 'papaya', 'avocado',
    'nectarine', 'lychee', 'kumquat', 'cranberry',
)

def random_fruits(minimum=1, maximum=4):

    return {
        fruit: random.randint(1, 12)
        for fruit in random.sample(FRUITS, random.randint(minimum, maximum))
    }

def test_len(name, basket):

    print(f'>>> len({name})')
    print(repr(len(basket)))

def test_contains(name, basket, fruit):

    print(f'>>> {fruit!r} in {name}')
    print(repr(fruit in basket))

def test_getitem(name, basket, fruit):

    print(f'>>> {name}[{fruit!r}]')
    print(repr(basket[fruit]))

def test_setitem(name, basket, fruit, number):

    print(f'>>> {name}[{fruit!r}] = {number}')
    basket[fruit] = number

def test_binary(name, basket, operator, fruit):

    print(f'>>> {name} {operator} {fruit!r} # doctest: +REPR')
    print(repr(eval(f'basket {operator} fruit')))

def test_inplace(name, basket, operator, fruit):

    print(f'>>> {name} {operator}= {fruit!r}')
    if operator == '+':
        basket += fruit
    else:
        basket -= fruit
    return basket

# ---------------------------------------------------------------------------
# class FruitBasket: size, membership and indexing
# ---------------------------------------------------------------------------

# an empty basket, a basket with a single kind of fruit and a basket that
# holds one piece of a fruit (so that removing it empties that key) come
# first, followed by randomly filled baskets
cases = [
    {},
    {'mango': 5},
    {'kiwi': 1, 'papaya': 9},
    {'avocado': 3, 'nectarine': 1, 'lychee': 12},
]
while len(cases) < 12:
    cases.append(random_fruits())

sys.stdout = open(os.path.join(evaldir, '0.in'), 'w', encoding='utf-8')

for index, fruits in enumerate(cases):

    varname = f'basket_{index + 1:02d}'
    basket = test_instantiation(FruitBasket, fruits, varname=varname)

    tests = [
        'repr', 'str', 'len',
        'contains', 'missing', 'getitem', 'absent', 'setitem', 'clear',
    ]
    if index:
        random.shuffle(tests)

    # always finish with the full picture of the basket
    tests = tests + ['len', 'repr']

    for test in tests:

        present = sorted(basket.fruits) if len(basket) else []
        missing = [fruit for fruit in FRUITS if fruit not in basket]

        if test == 'repr':
            test_repr(basket, varname=varname, call=False)

        elif test == 'str':
            test_str(basket, varname=varname, call=True)

        elif test == 'len':
            test_len(varname, basket)

        elif test == 'contains':
            if not present:
                continue
            test_contains(varname, basket, random.choice(present))

        elif test == 'missing':
            test_contains(varname, basket, random.choice(missing))

        elif test == 'getitem':
            if not present:
                continue
            test_getitem(varname, basket, random.choice(present))

        elif test == 'absent':
            test_getitem(varname, basket, random.choice(missing))

        elif test == 'setitem':
            # set a fruit that is already in the basket to a new number, or
            # put a brand new fruit in the basket
            fruit = random.choice(present + missing)
            number = random.randint(1, 15)
            test_setitem(varname, basket, fruit, number)
            test_getitem(varname, basket, fruit)

        else:
            # setting a fruit to zero (or less) takes it out of the basket
            if not present:
                continue
            fruit = random.choice(present)
            test_setitem(varname, basket, fruit, random.choice((0, 0, -3)))
            test_contains(varname, basket, fruit)
            test_getitem(varname, basket, fruit)

    print()

# ---------------------------------------------------------------------------
# class FruitBasket: adding and removing pieces of fruit
# ---------------------------------------------------------------------------

cases = [
    {},
    {'mango': 1},
    {'kiwi': 4, 'papaya': 1},
    {'avocado': 2, 'lychee': 7, 'kumquat': 1},
]
while len(cases) < 12:
    cases.append(random_fruits())

sys.stdout = open(os.path.join(evaldir, '1.in'), 'w', encoding='utf-8')

for index, fruits in enumerate(cases):

    varname = f'basket_{index + 1:02d}'
    basket = test_instantiation(FruitBasket, fruits, varname=varname)

    tests = ['add', 'iadd', 'sub', 'isub', 'sub_missing', 'isub_last', 'copy']
    if index:
        random.shuffle(tests)

    tests = tests + ['repr', 'len']

    for test in tests:

        present = sorted(basket.fruits) if len(basket) else []
        missing = [fruit for fruit in FRUITS if fruit not in basket]

        if test == 'repr':
            test_repr(basket, varname=varname, call=False)

        elif test == 'len':
            test_len(varname, basket)

        elif test == 'add':
            # the basket itself must not change
            fruit = random.choice(present + missing)
            test_binary(varname, basket, '+', fruit)
            test_repr(basket, varname=varname, call=False)

        elif test == 'iadd':
            fruit = random.choice(present + missing)
            basket = test_inplace(varname, basket, '+', fruit)
            test_getitem(varname, basket, fruit)

        elif test == 'sub':
            if not present:
                continue
            fruit = random.choice(present)
            test_binary(varname, basket, '-', fruit)
            test_repr(basket, varname=varname, call=False)

        elif test == 'isub':
            if not present:
                continue
            fruit = random.choice(present)
            basket = test_inplace(varname, basket, '-', fruit)
            test_getitem(varname, basket, fruit)

        elif test == 'sub_missing':
            # taking away a fruit that is not in the basket changes nothing
            fruit = random.choice(missing)
            test_binary(varname, basket, '-', fruit)
            basket = test_inplace(varname, basket, '-', fruit)
            test_contains(varname, basket, fruit)
            test_len(varname, basket)

        elif test == 'isub_last':
            # taking away the last piece of a fruit takes the fruit itself
            # out of the basket
            last = [fruit for fruit in present if basket[fruit] == 1]
            if not last:
                continue
            fruit = random.choice(last)
            basket = test_inplace(varname, basket, '-', fruit)
            test_contains(varname, basket, fruit)
            test_getitem(varname, basket, fruit)

        else:
            # a basket built with + is a new basket, and changing it must
            # leave the basket it was built from alone
            fruit = random.choice(present + missing)
            other = f'other_{index + 1:02d}'
            print(f'>>> {other} = {varname} + {fruit!r}')
            copy = basket + fruit
            print(f'>>> {other} is {varname}')
            print(repr(copy is basket))
            copy = test_inplace(other, copy, '+', random.choice(FRUITS))
            test_repr(copy, varname=other, call=False)
            test_repr(basket, varname=varname, call=False)

    print()
