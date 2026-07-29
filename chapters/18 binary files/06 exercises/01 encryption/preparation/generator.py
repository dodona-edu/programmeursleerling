"""Generate the test suite of the exercise "encryption".

Run this script from within the directory that contains it:

    python3 generator.py

Every expected value in the generated doctests is produced by actually running
the sample solution, so no byte string representation is ever typed by hand.
"""

import contextlib
import importlib.util
import io
import os
import shutil
import sys
import tempfile

# do not leave a __pycache__ directory behind when loading the sample
# solutions below
sys.dont_write_bytecode = True

# locate the directories of the exercise
evaldir = os.path.join('..', 'evaluation')
solutiondir = os.path.join('..', 'solution')
workdir = os.path.join('..', 'workdir')
mediadir = os.path.join('..', 'description', 'media')
datadir = os.path.join(mediadir, 'data')
mediaworkdir = os.path.join(mediadir, 'workdir')

for directory in (evaldir, solutiondir, workdir, datadir, mediaworkdir):
    os.makedirs(directory, exist_ok=True)

# load functionality defined in sample solution
spec = importlib.util.spec_from_file_location(
    'solution', os.path.join(solutiondir, 'solution.en.py')
)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

# the data files that are made available to the submission; the judge copies
# the content of the workdir directory into the working directory of the
# submission before running it
POEM = (
    b'How much wood would a woodchuck chuck\n'
    b'If a woodchuck could chuck wood?\n'
)

GIVEN_FILES = {
    'poem.txt': POEM,
    'borders.bin': bytes([0, 127, 128, 255]),
    'empty.bin': b'',
    'single.bin': bytes([0]),
    'bytes.bin': bytes(range(256)),
}

# the data file used by the example in the description
EXAMPLE_FILE = ('data.txt', b'Hello, world!\n')

# the statements of the test suite, in the order in which they are executed;
# every statement is a (source, show stdout instead of return value, data
# files to link to from the feedback) triple
STATEMENTS = [
    # a plain text file turns into a mess and is restored by a second call
    ("print(open('poem.txt', 'r').read(), end='')", True, ['poem.txt']),
    ("encrypt('poem.txt')", False, []),
    ("open('poem.txt', 'rb').read()", False, []),
    ("encrypt('poem.txt')", False, []),
    ("print(open('poem.txt', 'r').read(), end='')", True, []),

    # the four boundary values 0, 127, 128 and 255
    ("open('borders.bin', 'rb').read()", False, ['borders.bin']),
    ("encrypt('borders.bin')", False, []),
    ("open('borders.bin', 'rb').read()", False, []),
    ("encrypt('borders.bin')", False, []),
    ("open('borders.bin', 'rb').read()", False, []),

    # an empty file stays empty
    ("encrypt('empty.bin')", False, ['empty.bin']),
    ("open('empty.bin', 'rb').read()", False, []),

    # a file that holds a single byte
    ("encrypt('single.bin')", False, ['single.bin']),
    ("open('single.bin', 'rb').read()", False, []),
    ("encrypt('single.bin')", False, []),
    ("open('single.bin', 'rb').read()", False, []),

    # every possible byte value, encrypted and decrypted again
    ("open('bytes.bin', 'rb').read() == bytes(range(256))", False, ['bytes.bin']),
    ("encrypt('bytes.bin')", False, []),
    ("open('bytes.bin', 'rb').read() == bytes(range(128, 256)) + bytes(range(128))", False, []),
    ("encrypt('bytes.bin')", False, []),
    ("open('bytes.bin', 'rb').read() == bytes(range(256))", False, []),
]

TAB = 'encrypt'

LANGUAGE = """<LANGUAGE code="nl">
    <function from="encrypt" to="encrypteer" />
</LANGUAGE>"""


def transcript(statements, namespace):

    """Turn a list of statements into a Python interactive session.

    The statements are executed one after the other in a single namespace, and
    what the interactive interpreter would echo for them is used as the
    expected output of the doctest.
    """

    lines = []

    for source, use_stdout, files in statements:

        lines.append(
            '>>> {}{}'.format(source, ' # doctest: +STDOUT' if use_stdout else '')
        )

        # link the data files that are given to the submission, so that their
        # content can be inspected from the feedback
        for name in files:
            lines.append(f'<FILE name="{name}" href="media/workdir/{name}" />')

        try:
            code = compile(source, '<test>', 'eval')
            expression = True
        except SyntaxError:
            code = compile(source, '<test>', 'exec')
            expression = False

        buffer = io.StringIO()
        try:
            with contextlib.redirect_stdout(buffer):
                if expression:
                    value = eval(code, namespace)
                else:
                    exec(code, namespace)
                    value = None
        except Exception as error:
            lines.append('Traceback (most recent call last):')
            lines.append(f'{error.__class__.__name__}: {error}')
            lines.append('')
            continue

        if use_stdout:
            printed = buffer.getvalue()
            if printed:
                lines.append(printed.rstrip('\n'))
        elif value is not None:
            lines.append(repr(value))

        lines.append('')

    return '\n'.join(lines)


# write the data files that are given to the submission, and copy them to the
# description so that they can be inspected from the feedback
for name, content in GIVEN_FILES.items():
    with open(os.path.join(workdir, name), 'wb') as datafile:
        datafile.write(content)
    shutil.copyfile(
        os.path.join(workdir, name), os.path.join(mediaworkdir, name)
    )

# write the data file used by the example in the description
name, content = EXAMPLE_FILE
for directory in (solutiondir, datadir):
    with open(os.path.join(directory, name), 'wb') as datafile:
        datafile.write(content)

# run the test suite against the sample solution in a scratch directory, since
# the function modifies the files it is given
origin = os.getcwd()
with tempfile.TemporaryDirectory() as scratch:
    shutil.copytree(workdir, scratch, dirs_exist_ok=True)
    os.chdir(scratch)
    try:
        session = transcript(STATEMENTS, {'encrypt': module.encrypt})
    finally:
        os.chdir(origin)

with open(os.path.join(evaldir, '0.in'), 'w', encoding='utf-8') as testfile:
    testfile.write(session)

with open(os.path.join(evaldir, '0.out'), 'w', encoding='utf-8') as testfile:
    testfile.write(
        '--------------------------------------------------------\n'
        f'tab name: {TAB}\n'
        f'{LANGUAGE}'
    )
