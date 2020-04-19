import os
import sys
import shutil
import importlib
from test_utils import *

# set fixed seed for generating test cases
random.seed(123456789)

# exercise directories
evaldir = create_dir('..', 'evaluation')                        # evaluation
solutiondir = create_dir('..', 'solution')                      # solution
workdir = create_dir('..', 'workdir')                           # work
datadir = create_dir('..', 'description', 'media', 'workdir')   # shared work

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

# generate unit tests for function copy_csv
sys.stdout = open(os.path.join('..', 'evaluation', '0.in'), 'w', encoding='utf-8')
for filename in os.listdir(workdir):

    # generate copied file name
    copy_filename = filename.split('.')
    copy_filename.insert(1, 'copy')
    copy_filename = '.'.join(copy_filename)

    # generate test expression
    print(f'>>> copy_csv({filename!r}, {copy_filename!r})')
    print(f'<FILE name="{filename}" src="" href="media/workdir/{filename}" />')

    # generate return value
    try:

        # copy file
        result = copy_csv(os.path.join(workdir, filename), copy_filename)

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

        if result is not None:
            print(f'{result!r}')

    except Exception as e:
        print('Traceback (most recent call last):\n{}: {}'.format(e.__class__.__name__, e))

    print()
