import sys
import random
import importlib
from test_utils import *

# set fixed seed for generating test cases
random.seed(123456789)

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

# generate test data for class Point
cases = [(3, 4)]
while len(cases) < 50:
    cases.append((random.randint(-10, 10), random.randint(-10, 10)))

# generate unit tests for class Point
sys.stdout = open(os.path.join('..', 'evaluation', '0.in'), 'w', encoding='utf-8')
for index, (x, y) in enumerate(cases):

    # instantiation
    varname = f'point_{index + 1:02d}'
    obj = test_instantiation(Point, x, y, varname=varname)

    # test string conversion (str)
    tests = ['repr', 'str']
    if index:
        random.shuffle(tests)

    for test in tests:

        if test == 'repr':
            test_repr(obj, varname=varname, call=None if index else False)
        elif test == 'str':
            test_str(obj, varname=varname, call=None if index else False)

    print()

# generate test data for class Rectangle
def generate_rectangle(valid=1.0):

    x = random.randint(-10, 10)
    y = random.randint(-10, 10)
    w = random.randint(1, 10) if random.random() <= valid else random.randint(-10, 0)
    h = random.randint(1, 10) if random.random() <= valid else random.randint(-10, 0)

    return (x, y, w, h)

cases = [(1, 1, 8, 5), (2, 3, 9, 2)]
while len(cases) < 50:
    cases.append(generate_rectangle(valid=0.95))

# generate unit tests for class Rectangle
sys.stdout = open(os.path.join('..', 'evaluation', '1.in'), 'w', encoding='utf-8')
for index, (x, y, w, h) in enumerate(cases):

    try:

        # instantiation
        varname = f'rectangle_{index + 1:02d}'
        obj = test_instantiation(Rectangle, Point(x, y), w, h, varname=varname)

        # test string conversion (str)
        tests = [
            'repr', 'str', 'surface_area', 'circumference', 'bottom_right',
            'overlapping', 'nonoverlapping'
        ]
        if index:
            random.shuffle(tests)

        for test in tests:

            if test == 'repr':
                test_repr(obj, varname=varname, call=None if index else False)
            elif test == 'str':
                test_str(obj, varname=varname, call=None if index else False)
            elif test.endswith('overlapping'):
                x, y, w, h = generate_rectangle()
                rectangle =  Rectangle(Point(x, y), w, h)
                while bool(obj.overlap(rectangle)) == test.startswith('non'):
                    x, y, w, h = generate_rectangle()
                    rectangle = Rectangle(Point(x, y), w, h)
                test_method(obj, 'overlap', rectangle, representation=obj.overlap(rectangle) is not None, varname=varname)
            else:
                test_method(obj, test, representation=(True if test=='bottom_right' else False), varname=varname)

    except Exception as e:
        print('Traceback (most recent call last):\n{}: {}'.format(e.__class__.__name__, e))

    print()
