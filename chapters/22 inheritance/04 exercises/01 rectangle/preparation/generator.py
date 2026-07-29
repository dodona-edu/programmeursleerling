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

# generate test data for class Rectangle
def generate_rectangle():
    x = random.randint(-10, 10)
    y = random.randint(-10, 10)
    w = random.randint(1, 12)
    h = random.randint(1, 12)
    return (x, y, w, h)

cases = [(1, 1, 8, 5), (-3, 4, 1, 9)]
while len(cases) < 8:
    cases.append(generate_rectangle())

# generate unit tests for class Rectangle (given, unmodified base class)
sys.stdout = open(os.path.join('..', 'evaluation', '0.in'), 'w', encoding='utf-8')
for index, (x, y, w, h) in enumerate(cases):

    varname = f'rectangle_{index + 1:02d}'
    obj = test_instantiation(Rectangle, x, y, w, h, varname=varname)

    tests = ['repr', 'str', 'area', 'circumference']
    if index:
        random.shuffle(tests)

    for test in tests:
        if test == 'repr':
            test_repr(obj, varname=varname, call=None if index else False)
        elif test == 'str':
            test_str(obj, varname=varname, call=None if index else False)
        else:
            test_method(obj, test, varname=varname)

    print()

# generate test data for class Square
def generate_square():
    x = random.randint(-10, 10)
    y = random.randint(-10, 10)
    side = random.randint(1, 12)
    return (x, y, side)

cases = [(2, 3, 4), (0, 0, 1)]
while len(cases) < 10:
    cases.append(generate_square())

# generate unit tests for class Square: exercise both inherited (area,
# circumference, repr) and constructor (overridden) behaviour
sys.stdout = open(os.path.join('..', 'evaluation', '1.in'), 'w', encoding='utf-8')
for index, (x, y, side) in enumerate(cases):

    varname = f'square_{index + 1:02d}'
    obj = test_instantiation(Square, x, y, side, varname=varname)

    tests = ['repr', 'str', 'area', 'circumference', 'isinstance']
    if index:
        random.shuffle(tests)

    for test in tests:
        if test == 'repr':
            test_repr(obj, varname=varname, call=None if index else False)
        elif test == 'str':
            test_str(obj, varname=varname, call=None if index else False)
        elif test == 'isinstance':
            print(f'>>> isinstance({varname}, Rectangle)')
            print(repr(isinstance(obj, Rectangle)))
        else:
            test_method(obj, test, varname=varname)

    print()

# generate a polymorphism scenario: mix Rectangle and Square instances in a
# single list and process them through the shared interface inherited from
# Rectangle, showing that Square instances behave correctly even though the
# code calling area()/circumference() does not know about Square at all
sys.stdout = open(os.path.join('..', 'evaluation', '2.in'), 'w', encoding='utf-8')

scenarios = [
    [(1, 1, 6, 4), (0, 0, 3), (-2, 5, 2, 9), (4, -1, 7)],
    [(-4, -4, 5), (2, 2, 9, 1), (6, 6, 2), (-8, 3, 4, 4)],
    [(0, 0, 10, 10), (1, 1, 1), (-5, -5, 3, 6), (5, 5, 5)],
]

for index, spec_list in enumerate(scenarios):

    print(f'>>> shapes = [{", ".join("Rectangle" + repr(args) if len(args) == 4 else "Square" + repr(args) for args in spec_list)}] # doctest: +NEWCONTEXT')
    shapes = [
        Rectangle(*args) if len(args) == 4 else Square(*args)
        for args in spec_list
    ]

    print('>>> [shape.area() for shape in shapes]')
    print(repr([shape.area() for shape in shapes]))

    print('>>> [shape.circumference() for shape in shapes]')
    print(repr([shape.circumference() for shape in shapes]))

    print('>>> sum(shape.area() for shape in shapes)')
    print(repr(sum(shape.area() for shape in shapes)))

    print('>>> [isinstance(shape, Rectangle) for shape in shapes]')
    print(repr([isinstance(shape, Rectangle) for shape in shapes]))

    print()
