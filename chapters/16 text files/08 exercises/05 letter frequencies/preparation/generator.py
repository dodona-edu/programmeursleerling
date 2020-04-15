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
prefixes = []
for filename in os.listdir(workdir):
    shutil.copyfile(os.path.join(workdir, filename), os.path.join(datadir, filename))
    if filename.endswith('a.txt'):
        prefixes.append(filename[:-5])

# generate unit tests for functions common_words
sys.stdout = open(os.path.join('..', 'evaluation', '0.in'), 'w', encoding='utf-8')
for prefix in prefixes:

    filename1 = f'{prefix}a.txt'
    filename2 = f'{prefix}b.txt'
    filename3 = f'{prefix}c.txt'
    filename4 = f'{prefix}.csv'

    # generate test expression
    print(f'>>> letter_frequencies({filename1!r}, {filename2!r}, {filename3!r}, {filename4!r})')
    print(f'<FILE name="{filename1}" src="" href="media/workdir/{filename1}" />')
    print(f'<FILE name="{filename2}" src="" href="media/workdir/{filename2}" />')
    print(f'<FILE name="{filename3}" src="" href="media/workdir/{filename3}" />')
    print(f'<FILE name="{filename4}" src="memory">')

    # generate return value
    try:
        filename1 = os.path.join(workdir, filename1)
        filename2 = os.path.join(workdir, filename2)
        filename3 = os.path.join(workdir, filename3)

        # copy file
        letter_frequencies(filename1, filename2, filename3, filename4)

        # produce output as reference for comparison
        with open(filename4) as csv:
            print(csv.read(), end='')
        os.remove(filename4)
        print('</FILE>')

        # add output processor for file
        print('<OUTPUTPROCESSOR>')
        print('OutputProcessor()')
        print('</OUTPUTPROCESSOR>')
        print('<OUTPUTPROCESSOR>')
        print(f'FileContentChecker({filename4!r})')
        print('</OUTPUTPROCESSOR>')

    except Exception as e:
        print('Traceback (most recent call last):\n{}: {}'.format(e.__class__.__name__, e))

    print()
