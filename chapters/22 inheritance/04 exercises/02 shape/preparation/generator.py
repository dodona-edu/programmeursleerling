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
# tab 0: Shape -- the (mostly unusable) interface class itself
# ---------------------------------------------------------------------
sys.stdout = open(os.path.join('..', 'evaluation', '0.in'), 'w', encoding='utf-8')

for index in range(4):
    varname = f'shape_{index + 1:02d}'
    obj = test_instantiation(Shape, varname=varname)
    tests = ['area', 'circumference']
    if index:
        random.shuffle(tests)
    for test in tests:
        test_method(obj, test, varname=varname)
    print()

# ---------------------------------------------------------------------
# tab 1: Rectangle -- a Shape subclass (inherited behaviour)
# ---------------------------------------------------------------------
def generate_rectangle():
    x = random.randint(-10, 10)
    y = random.randint(-10, 10)
    w = random.randint(1, 12)
    h = random.randint(1, 12)
    return (x, y, w, h)

cases = [(1, 1, 8, 5), (-3, 4, 1, 9)]
while len(cases) < 6:
    cases.append(generate_rectangle())

sys.stdout = open(os.path.join('..', 'evaluation', '1.in'), 'w', encoding='utf-8')
for index, (x, y, w, h) in enumerate(cases):

    varname = f'rectangle_{index + 1:02d}'
    obj = test_instantiation(Rectangle, x, y, w, h, varname=varname)

    tests = ['repr', 'str', 'area', 'circumference', 'isshape']
    if index:
        random.shuffle(tests)

    for test in tests:
        if test == 'repr':
            test_repr(obj, varname=varname, call=None if index else False)
        elif test == 'str':
            test_str(obj, varname=varname, call=None if index else False)
        elif test == 'isshape':
            print(f'>>> isinstance({varname}, Shape)')
            print(repr(isinstance(obj, Shape)))
        else:
            test_method(obj, test, varname=varname)

    print()

# ---------------------------------------------------------------------
# tab 2: Square -- a sub(sub)class of Shape (two levels of inheritance)
# ---------------------------------------------------------------------
def generate_square():
    x = random.randint(-10, 10)
    y = random.randint(-10, 10)
    side = random.randint(1, 12)
    return (x, y, side)

cases = [(2, 3, 4), (0, 0, 1)]
while len(cases) < 8:
    cases.append(generate_square())

sys.stdout = open(os.path.join('..', 'evaluation', '2.in'), 'w', encoding='utf-8')
for index, (x, y, side) in enumerate(cases):

    varname = f'square_{index + 1:02d}'
    obj = test_instantiation(Square, x, y, side, varname=varname)

    tests = ['repr', 'str', 'area', 'circumference', 'isrectangle', 'isshape']
    if index:
        random.shuffle(tests)

    for test in tests:
        if test == 'repr':
            test_repr(obj, varname=varname, call=None if index else False)
        elif test == 'str':
            test_str(obj, varname=varname, call=None if index else False)
        elif test == 'isrectangle':
            print(f'>>> isinstance({varname}, Rectangle)')
            print(repr(isinstance(obj, Rectangle)))
        elif test == 'isshape':
            print(f'>>> isinstance({varname}, Shape)')
            print(repr(isinstance(obj, Shape)))
        else:
            test_method(obj, test, varname=varname)

    print()

# ---------------------------------------------------------------------
# tab 3: Circle -- a direct Shape subclass with its own formulas
# (overridden/polymorphic behaviour compared to Rectangle/Square)
# ---------------------------------------------------------------------
def generate_circle():
    x = random.randint(-10, 10)
    y = random.randint(-10, 10)
    r = random.randint(1, 9)
    return (x, y, r)

cases = [(0, 0, 3), (5, -2, 1)]
while len(cases) < 8:
    cases.append(generate_circle())

sys.stdout = open(os.path.join('..', 'evaluation', '3.in'), 'w', encoding='utf-8')
for index, (x, y, r) in enumerate(cases):

    varname = f'circle_{index + 1:02d}'
    obj = test_instantiation(Circle, x, y, r, varname=varname)

    tests = ['repr', 'str', 'area', 'circumference', 'isshape', 'isrectangle']
    if index:
        random.shuffle(tests)

    for test in tests:
        if test == 'repr':
            test_repr(obj, varname=varname, call=None if index else False)
        elif test == 'str':
            test_str(obj, varname=varname, call=None if index else False)
        elif test == 'isshape':
            print(f'>>> isinstance({varname}, Shape)')
            print(repr(isinstance(obj, Shape)))
        elif test == 'isrectangle':
            print(f'>>> isinstance({varname}, Rectangle)')
            print(repr(isinstance(obj, Rectangle)))
        else:
            test_method(obj, test, varname=varname)

    print()

# ---------------------------------------------------------------------
# tab 4: Polymorphism -- process a heterogeneous list of Rectangle,
# Square and Circle instances purely through the Shape interface
# ---------------------------------------------------------------------
sys.stdout = open(os.path.join('..', 'evaluation', '4.in'), 'w', encoding='utf-8')

scenarios = [
    [('Rectangle', 1, 1, 6, 4), ('Circle', 0, 0, 2), ('Square', -2, 5, 3), ('Circle', 4, -1, 1)],
    [('Circle', -4, -4, 5), ('Rectangle', 2, 2, 9, 1), ('Square', 6, 6, 2), ('Circle', -8, 3, 3)],
    [('Square', 0, 0, 10), ('Circle', 1, 1, 4), ('Rectangle', -5, -5, 3, 6), ('Square', 5, 5, 5)],
]

constructors = {'Rectangle': Rectangle, 'Square': Square, 'Circle': Circle}

for index, spec_list in enumerate(scenarios):

    call_texts = [
        f'{name}({", ".join(str(a) for a in args)})'
        for name, *args in spec_list
    ]
    print(f'>>> shapes = [{", ".join(call_texts)}] # doctest: +NEWCONTEXT')
    shapes = [constructors[name](*args) for name, *args in spec_list]

    print('>>> [round(shape.area(), 2) for shape in shapes]')
    print(repr([round(shape.area(), 2) for shape in shapes]))

    print('>>> [round(shape.circumference(), 2) for shape in shapes]')
    print(repr([round(shape.circumference(), 2) for shape in shapes]))

    print('>>> round(sum(shape.area() for shape in shapes), 2)')
    print(repr(round(sum(shape.area() for shape in shapes), 2)))

    print('>>> [isinstance(shape, Shape) for shape in shapes]')
    print(repr([isinstance(shape, Shape) for shape in shapes]))

    print()
