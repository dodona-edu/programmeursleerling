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

# generate unit tests for functions vowel_removal
sys.stdout = open(os.path.join('..', 'evaluation', '0.in'), 'w', encoding='utf-8')
for filename in os.listdir(workdir):

    # generate copied file name
    copy_filename = filename.split('.')
    copy_filename.insert(1, 'copy')
    copy_filename = '.'.join(copy_filename)

    # generate test expression
    print(f'>>> vowel_removal({filename!r}, {copy_filename!r})')
    print(f'<FILE name="{filename}" src="" href="media/workdir/{filename}" />')

    # generate return value
    try:

        # copy file
        result = vowel_removal(os.path.join(workdir, filename), copy_filename)

        # produce output as reference for comparison
        print(f'<FILE name="{copy_filename}" src="memory">')
        with open(copy_filename) as copy:
            print(copy.read(), end='')
        os.remove(copy_filename)
        print('</FILE>')

        # add output processor for file
        print('<OUTPUTPROCESSOR>')
        print('OutputProcessor()')
        print('</OUTPUTPROCESSOR>')
        print('<OUTPUTPROCESSOR>')
        print(f'FileContentChecker({copy_filename!r})')
        print('</OUTPUTPROCESSOR>')

        print(f'{result!r}')

    except Exception as e:
        print('Traceback (most recent call last):\n{}: {}'.format(e.__class__.__name__, e))

    print()
