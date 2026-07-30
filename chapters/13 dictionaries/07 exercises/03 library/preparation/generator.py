import os
import sys
import importlib.util

# locate evaldir
evaldir = os.path.join('..', 'evaluation')
if not os.path.exists(evaldir):
    os.makedirs(evaldir)

# locate solutiondir
solutiondir = os.path.join('..', 'solution')
if not os.path.exists(solutiondir):
    os.makedirs(solutiondir)

# load functionality defined in sample solution
module_name = 'solution'
file_path = os.path.join(solutiondir, 'solution.en.py')
spec = importlib.util.spec_from_file_location(module_name, file_path)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

for name in dir(module):
    if not (name.startswith('__') and name.endswith('__')):
        globals()[name] = eval(f'module.{name}')

# generate test data for functions list2dict, location and titles
cases = [
    [
        ('Adams', 'Douglas', "The Hitchhiker's Guide to the Galaxy", 42),
        ('Adams', 'Douglas', 'The Restaurant at the End of the Universe', 43),
        ('Adams', 'Douglas', 'Life, the Universe and Everything', 44),
        ('Rowling', 'Joanne', "Harry Potter and the Philosopher's Stone", 271),
        ('Rowling', 'Joanne', 'Harry Potter and the Chamber of Secrets', 272),
        ('Tolkien', 'John', 'The Hobbit', 137),
        ('Spronck', 'Pieter', "The Coder's Apprentice", 512),
    ],
]

# books that are in the library, and one that is not
lookups = [
    ('Adams', 'Douglas', "The Hitchhiker's Guide to the Galaxy"),
    ('Spronck', 'Pieter', "The Coder's Apprentice"),
]
missing = ('Adams', 'Douglas', 'The Long Dark Tea-Time of the Soul')

# writers of whom the library has books, and one of whom it has none
writers = [
    ('Adams', 'Douglas'),
    ('Tolkien', 'John'),
    ('Pratchett', 'Terry'),
]

# generate unit tests for function list2dict
sys.stdout = open(os.path.join('..', 'evaluation', '0.in'), 'w', encoding='utf-8')
for books in cases:

    # generate test expression
    print(f'>>> list2dict({books!r})')

    # generate return value
    try:
        print(f'{list2dict(books)!r}')
    except Exception as e:
        print('Traceback (most recent call last):\n{}: {}'.format(e.__class__.__name__, e))

    print()

# generate unit tests for function location
sys.stdout = open(os.path.join('..', 'evaluation', '1.in'), 'w', encoding='utf-8')
for index, books in enumerate(cases):

    # one-based indexing
    index += 1

    # generate context shared by all test expressions of this case
    library = list2dict(books)
    print(f'>>> library_{index:02d} = list2dict({books!r}) # doctest: +NOEXEC +NEWCONTEXT')
    print(f'>>> library_{index:02d} = {library!r} # doctest: +NOSHOW')

    for last_name, first_name, title in lookups:

        # generate test expression
        print(f'>>> location(library_{index:02d}, {last_name!r}, {first_name!r}, {title!r})')

        # generate return value
        try:
            print(f'{location(library, last_name, first_name, title)!r}')
        except Exception as e:
            print('Traceback (most recent call last):\n{}: {}'.format(e.__class__.__name__, e))

    # a book that is not in the library returns None, which a doctest cannot
    # distinguish from no output at all
    last_name, first_name, title = missing

    # generate test expression
    print(f'>>> location(library_{index:02d}, {last_name!r}, {first_name!r}, {title!r}) is None')

    # generate return value
    try:
        print(f'{location(library, last_name, first_name, title) is None!r}')
    except Exception as e:
        print('Traceback (most recent call last):\n{}: {}'.format(e.__class__.__name__, e))

    print()

# generate unit tests for function titles
sys.stdout = open(os.path.join('..', 'evaluation', '2.in'), 'w', encoding='utf-8')
for index, books in enumerate(cases):

    # one-based indexing
    index += 1

    # generate context shared by all test expressions of this case
    library = list2dict(books)
    print(f'>>> library_{index:02d} = list2dict({books!r}) # doctest: +NOEXEC +NEWCONTEXT')
    print(f'>>> library_{index:02d} = {library!r} # doctest: +NOSHOW')

    for last_name, first_name in writers:

        # generate test expression
        print(f'>>> titles(library_{index:02d}, {last_name!r}, {first_name!r})')

        # generate return value
        try:
            print(f'{titles(library, last_name, first_name)!r}')
        except Exception as e:
            print('Traceback (most recent call last):\n{}: {}'.format(e.__class__.__name__, e))

    print()
