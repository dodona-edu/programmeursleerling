"""Generate the test suite of the exercise "file compression".

Run this script from within the directory that contains it:

    python3 generator.py

The compressed data files that are given to the submission are produced by the
sample solution of the exercise "compression", and every expected value in the
generated doctests is produced by running the sample solution of this
exercise. That way the three exercises are guaranteed to describe the exact
same encoding, and no byte string representation is ever typed by hand.
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

# the sample solution of the exercise "compression", used to produce the
# compressed data files that are given to the submission
compressiondir = os.path.join('..', '..', '02 compression', 'solution')

for directory in (evaldir, solutiondir, workdir, datadir, mediaworkdir):
    os.makedirs(directory, exist_ok=True)


def load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


solution = load('solution', os.path.join(solutiondir, 'solution.en.py'))
compression = load(
    'compression', os.path.join(compressiondir, 'solution.en.py')
)

# the uncompressed data files that are made available to the submission
PLAIN_FILES = {
    'poem.txt': (
        b'How much wood would a woodchuck chuck\n'
        b'If a woodchuck could chuck wood?\n'
    ),
    'bytes.bin': bytes(range(256)),
    'empty.bin': b'',
}

# the data file used by the example in the description
EXAMPLE_FILE = ('data.txt', b'Hello, world!')

# the compressed counterparts of the uncompressed data files, produced by the
# sample solution of the exercise "compression"
COMPRESSED_FILES = {
    name.rsplit('.', 1)[0] + '.cmp': compression.compress(
        content.decode('latin-1')
    )
    for name, content in PLAIN_FILES.items()
}

# the statements of the test suite, one list per tab; every statement is a
# (source, show stdout instead of return value, data files to link to from
# the feedback) triple
TABS = [
    ('compress_file', [
        # a plain text file
        ("compress_file('poem.txt', 'poem.new')", False, ['poem.txt']),
        ("open('poem.new', 'rb').read() == open('poem.cmp', 'rb').read()", False, ['poem.cmp']),

        # a binary file that holds every possible byte value
        ("compress_file('bytes.bin', 'bytes.new')", False, ['bytes.bin']),
        ("open('bytes.new', 'rb').read() == open('bytes.cmp', 'rb').read()", False, ['bytes.cmp']),

        # an empty file
        ("compress_file('empty.bin', 'empty.new')", False, ['empty.bin']),
        ("open('empty.new', 'rb').read()", False, []),

        # the input file must exist and the output file must not exist
        ("compress_file('missing.bin', 'missing.new')", False, []),
        ("compress_file('poem.txt', 'poem.cmp')", False, []),
    ]),
    ('decompress_file', [
        # the compressed counterpart of the plain text file
        ("decompress_file('poem.cmp', 'poem.raw')", False, ['poem.cmp']),
        ("open('poem.raw', 'rb').read() == open('poem.txt', 'rb').read()", False, ['poem.txt']),

        # the compressed counterpart of the binary file
        ("decompress_file('bytes.cmp', 'bytes.raw')", False, ['bytes.cmp']),
        ("open('bytes.raw', 'rb').read() == bytes(range(256))", False, []),

        # an empty file
        ("decompress_file('empty.cmp', 'empty.raw')", False, ['empty.cmp']),
        ("open('empty.raw', 'rb').read()", False, []),

        # the input file must exist and the output file must not exist
        ("decompress_file('missing.cmp', 'missing.raw')", False, []),
        ("decompress_file('poem.cmp', 'poem.txt')", False, []),
    ]),
]

LANGUAGE = """<LANGUAGE code="nl">
    <function from="compress_file" to="comprimeer_bestand" />
    <function from="decompress_file" to="decomprimeer_bestand" />
    <fixed from="input file does not exist" to="invoerbestand bestaat niet" detect="false" />
    <fixed from="output file already exists" to="uitvoerbestand bestaat al" detect="false" />
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
for name, content in {**PLAIN_FILES, **COMPRESSED_FILES}.items():
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

# the sample solutions of this exercise and of the previous two exercises must
# describe the exact same encoding
for name, content in PLAIN_FILES.items():
    text = content.decode('latin-1')
    assert solution.compress(text) == compression.compress(text)
    assert solution.decompress(solution.compress(text)) == text

namespace = {
    'compress_file': solution.compress_file,
    'decompress_file': solution.decompress_file,
}

origin = os.getcwd()
for index, (tab, statements) in enumerate(TABS):

    # run the statements against the sample solution in a scratch directory,
    # since they create files in the working directory
    with tempfile.TemporaryDirectory() as scratch:
        shutil.copytree(workdir, scratch, dirs_exist_ok=True)
        os.chdir(scratch)
        try:
            session = transcript(statements, namespace)
        finally:
            os.chdir(origin)

    with open(
        os.path.join(evaldir, f'{index}.in'), 'w', encoding='utf-8'
    ) as testfile:
        testfile.write(session)

    with open(
        os.path.join(evaldir, f'{index}.out'), 'w', encoding='utf-8'
    ) as testfile:
        testfile.write(
            '--------------------------------------------------------\n'
            f'tab name: {tab}\n'
            f'{LANGUAGE}'
        )
