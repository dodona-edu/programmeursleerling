import sys
import random
import importlib.util
from test_utils import *

# set fixed seed for generating test cases
random.seed(20260729)

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

# ---------------------------------------------------------------------
# tab 0: Strategy -- the base class itself (name/score/incscore work,
# choice()/lastmove() are unimplemented placeholders)
# ---------------------------------------------------------------------
sys.stdout = open(os.path.join('..', 'evaluation', '0.in'), 'w', encoding='utf-8')

scenarios = [
    ('Sam', [3]),
    ('', [1, 1, 4]),
    ('Priya', [6, 0]),
    ('Zoe', [0, 3, 3, 1]),
]

for index, (name, increments) in enumerate(scenarios):

    varname = f'strategy_{index + 1:02d}'
    context = ' # doctest: +NEWCONTEXT'
    if name:
        print(f'>>> {varname} = Strategy({name!r}){context}')
    else:
        print(f'>>> {varname} = Strategy(){context}')
    obj = Strategy(name) if name else Strategy()

    test_property(obj, 'name', varname=varname)
    test_property(obj, 'score', varname=varname)
    test_method(obj, 'choice', varname=varname)

    mymove, oppmove = ('C', 'D') if index % 2 == 0 else ('D', 'C')
    test_method(obj, 'lastmove', mymove, oppmove, varname=varname)

    for n in increments:
        test_method(obj, 'incscore', n, varname=varname)
        test_property(obj, 'score', varname=varname)

    print()

# ---------------------------------------------------------------------
# tab 1: AlwaysDefect -- overrides choice(), inherits everything else
# (name, score, incscore, lastmove) unchanged from Strategy
# ---------------------------------------------------------------------
sys.stdout = open(os.path.join('..', 'evaluation', '1.in'), 'w', encoding='utf-8')

scenarios = [
    ('Al', 3, [('D', 'C'), ('D', 'C')], [6]),
    ('Beth', 2, [('D', 'D')], [1, 1]),
    ('', 4, [('D', 'C'), ('D', 'D'), ('D', 'C')], [6, 1, 0]),
    ('Chuy', 2, [('D', 'C')], [6, 6]),
]

for index, (name, ncalls, lastmoves, increments) in enumerate(scenarios):

    varname = f'player_{index + 1:02d}'
    obj = test_instantiation(AlwaysDefect, name, varname=varname)

    test_property(obj, 'name', varname=varname)

    for _ in range(ncalls):
        test_method(obj, 'choice', varname=varname)

    for mymove, oppmove in lastmoves:
        test_method(obj, 'lastmove', mymove, oppmove, varname=varname)

    for n in increments:
        test_method(obj, 'incscore', n, varname=varname)

    test_property(obj, 'score', varname=varname)

    print()

# ---------------------------------------------------------------------
# tab 2: Random -- overrides choice() using the random module; tested
# with a fixed seed so the outcomes are reproducible
# ---------------------------------------------------------------------
sys.stdout = open(os.path.join('..', 'evaluation', '2.in'), 'w', encoding='utf-8')

seeds_and_names = [(11, 'Rae'), (202, 'Noor'), (37, ''), (9001, 'Kofi'), (555, 'Ida')]

for index, (seed, name) in enumerate(seeds_and_names):

    varname = f'gambler_{index + 1:02d}'
    print(f'>>> random.seed({seed}) # doctest: +NEWCONTEXT')
    random.seed(seed)

    if name:
        print(f'>>> {varname} = Random({name!r})')
        obj = Random(name)
    else:
        print(f'>>> {varname} = Random()')
        obj = Random()

    for _ in range(5):
        test_method(obj, 'choice', varname=varname)

    print()

# ---------------------------------------------------------------------
# tab 3: TitForTat -- overrides both choice() and lastmove(); starts
# with COOPERATE, then mirrors the opponent's previous move
# ---------------------------------------------------------------------
sys.stdout = open(os.path.join('..', 'evaluation', '3.in'), 'w', encoding='utf-8')

scenarios = [
    ('Tia', ['D', 'D', 'C']),
    ('Umar', ['C', 'D', 'D', 'C']),
    ('', ['D', 'C']),
    ('Wren', ['C', 'C', 'D']),
]

for index, (name, opponent_moves) in enumerate(scenarios):

    varname = f'mimic_{index + 1:02d}'
    obj = test_instantiation(TitForTat, name, varname=varname)

    test_method(obj, 'choice', varname=varname)

    for oppmove in opponent_moves:
        test_method(obj, 'lastmove', 'C', oppmove, varname=varname)
        test_method(obj, 'choice', varname=varname)

    test_method(obj, 'incscore', 3, varname=varname)
    test_property(obj, 'score', varname=varname)
    test_property(obj, 'name', varname=varname)

    print()

# ---------------------------------------------------------------------
# tab 4: TitForTwoTats -- starts with two COOPERATEs, then only plays
# DEFECT after the opponent defected on both of the last two moves
# ---------------------------------------------------------------------
sys.stdout = open(os.path.join('..', 'evaluation', '4.in'), 'w', encoding='utf-8')

scenarios = [
    ('Toby', ['D', 'D', 'C', 'D', 'D']),
    ('Vic', ['C', 'D', 'D']),
    ('', ['D', 'C', 'D', 'C']),
    ('Yara', ['D', 'D', 'D', 'D']),
]

for index, (name, opponent_moves) in enumerate(scenarios):

    varname = f'grudge_{index + 1:02d}'
    obj = test_instantiation(TitForTwoTats, name, varname=varname)

    test_method(obj, 'choice', varname=varname)

    for oppmove in opponent_moves:
        test_method(obj, 'lastmove', 'C', oppmove, varname=varname)
        test_method(obj, 'choice', varname=varname)

    print()

# ---------------------------------------------------------------------
# tab 5: Majority -- starts with COOPERATE, then plays whatever the
# opponent played most often so far (ties favour COOPERATE)
# ---------------------------------------------------------------------
sys.stdout = open(os.path.join('..', 'evaluation', '5.in'), 'w', encoding='utf-8')

scenarios = [
    ('Mia', ['D', 'D', 'C']),
    ('Nils', ['C', 'C', 'D', 'D']),
    ('', ['D', 'C', 'D', 'C', 'D']),
    ('Pia', ['C', 'D', 'D', 'D']),
]

for index, (name, opponent_moves) in enumerate(scenarios):

    varname = f'poll_{index + 1:02d}'
    obj = test_instantiation(Majority, name, varname=varname)

    test_method(obj, 'choice', varname=varname)

    for oppmove in opponent_moves:
        test_method(obj, 'lastmove', 'C', oppmove, varname=varname)
        test_method(obj, 'choice', varname=varname)

    print()

# ---------------------------------------------------------------------
# tab 6: Match -- two different concrete strategies play a few rounds
# of the actual game against each other, driven purely through the
# common Strategy interface (choice/incscore/lastmove); this exercises
# polymorphism: the same calling code works correctly regardless of
# which concrete Strategy subclass is behind strategy1/strategy2
# ---------------------------------------------------------------------
sys.stdout = open(os.path.join('..', 'evaluation', '6.in'), 'w', encoding='utf-8')

def play_round(varname1, obj1, varname2, obj2):

    print(f'>>> c1 = {varname1}.choice()')
    c1 = obj1.choice()
    print(f'>>> c2 = {varname2}.choice()')
    c2 = obj2.choice()
    print('>>> c1, c2')
    print(repr((c1, c2)))

    if c1 == c2:
        n1 = 3 if c1 == COOPERATE else 1
        n2 = 3 if c2 == COOPERATE else 1
    else:
        n1 = 0 if c1 == COOPERATE else 6
        n2 = 0 if c2 == COOPERATE else 6

    print(f'>>> {varname1}.incscore({n1})')
    obj1.incscore(n1)
    print(f'>>> {varname2}.incscore({n2})')
    obj2.incscore(n2)
    print(f'>>> {varname1}.lastmove(c1, c2)')
    obj1.lastmove(c1, c2)
    print(f'>>> {varname2}.lastmove(c2, c1)')
    obj2.lastmove(c2, c1)
    print(f'>>> {varname1}.score')
    print(repr(obj1.score))
    print(f'>>> {varname2}.score')
    print(repr(obj2.score))

matches = [
    ('TitForTat', 'Tessa', 'AlwaysDefect', 'Aiden', None, 4),
    ('TitForTwoTats', 'Deon', 'AlwaysDefect', 'Femke', None, 5),
    ('Random', 'Kai', 'Majority', 'Lina', 4242, 4),
]

for varname1_class, name1, varname2_class, name2, seed, rounds in matches:

    if seed is not None:
        print(f'>>> random.seed({seed}) # doctest: +NEWCONTEXT')
        random.seed(seed)
        newcontext = False
    else:
        newcontext = True

    varname1 = name1.lower()
    varname2 = name2.lower()

    context = ' # doctest: +NEWCONTEXT' if newcontext else ''
    print(f'>>> {varname1} = {varname1_class}({name1!r}){context}')
    obj1 = eval(varname1_class)(name1)
    print(f'>>> {varname2} = {varname2_class}({name2!r})')
    obj2 = eval(varname2_class)(name2)

    for _ in range(rounds):
        play_round(varname1, obj1, varname2, obj2)

    print(f'>>> isinstance({varname1}, Strategy) and isinstance({varname2}, Strategy)')
    print(repr(isinstance(obj1, Strategy) and isinstance(obj2, Strategy)))

    print()
