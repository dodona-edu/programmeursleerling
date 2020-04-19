import os
import sys
import random
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
languages = ['en', 'nl']
for language in languages:

    module_name = f'solution_{language}'
    file_path = os.path.join(solutiondir, f'solution.{language}.py')
    spec = importlib.util.spec_from_file_location(module_name, file_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)

    for name in dir(module):
        if not (name.startswith('__') and name.endswith('__')):
            globals()[name] = eval(f'module.{name}')

# copy files from workdir to datadir
for filename in os.listdir(workdir):
    shutil.copyfile(os.path.join(workdir, filename), os.path.join(datadir, filename))

# generate unit tests for functions find_the_the
sys.stdout = open(os.path.join('..', 'evaluation', '0.in'), 'w', encoding='utf-8')
functions = {
    'en': find_the_the,
    'nl': zoek_de_de,
}
for filename in os.listdir(workdir):

    # parse filename parts
    parts = filename.split('.')
    if not (
        len(parts) == 3 and
        parts[0].startswith('data') and
        len(parts[1]) == 2 and
        parts[2] == 'txt'
    ):
        continue
    language = parts[1]

    # generate test expression
    print(f'>>> find_the_the({filename!r})')
    print(f'<LANGUAGE code="{"en notdetected" if language == "en" else language}" />')
    print(f'<FILE name="{filename}" src="" href="media/workdir/{filename}" />')

    # generate return value
    try:
        print(f'{functions[language](os.path.join(workdir, filename))!r}')
    except Exception as e:
        print('Traceback (most recent call last):\n{}: {}'.format(e.__class__.__name__, e))

    print()
