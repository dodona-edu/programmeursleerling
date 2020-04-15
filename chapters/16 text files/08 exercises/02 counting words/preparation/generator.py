import os
import sys
import random
import shutil
import importlib

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

# locate workdir
workdir = os.path.join('..', 'workdir')
if not os.path.exists(workdir):
    os.makedirs(workdir)

# locate datadir
datadir = os.path.join('..', 'description', 'media', 'workdir')
if not os.path.exists(datadir):
    os.makedirs(datadir)

# load functionality defined in sample solution
module_name = 'solution'
file_path = os.path.join(solutiondir, 'solution.en.py')
spec = importlib.util.spec_from_file_location(module_name, file_path)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

for name in dir(module):
    if not (name.startswith('__') and name.endswith('__')):
        globals()[name] = eval(f'module.{name}')

# copy files from workdir to datadir
for filename in os.listdir(workdir):
    shutil.copyfile(os.path.join(workdir, filename), os.path.join(datadir, filename))

# generate unit tests for functions word_count
functions = [word_split, word_count]
for index, func in enumerate(functions):
    sys.stdout = open(os.path.join('..', 'evaluation', f'{index}.in'), 'w', encoding='utf-8')
    for filename in os.listdir(workdir):

        # generate test expression
        print(f'>>> {func.__name__}({filename!r})')
        print(f'<FILE name="{filename}" src="" href="media/workdir/{filename}" />')

        # generate return value
        try:
            print(f'{func(os.path.join(workdir, filename))!r}')
        except Exception as e:
            print('Traceback (most recent call last):\n{}: {}'.format(e.__class__.__name__, e))

        print()
