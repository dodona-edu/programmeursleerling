"""Generate the test suite of the exercise "decompression".

Run this script from within the directory that contains it:

    python3 generator.py

The byte strings that are decompressed by the test suite are produced by the
sample solution of the previous exercise ("compression"), and the expected
results are produced by running the sample solution of this exercise. That way
both exercises are guaranteed to describe the exact same encoding, and no byte
string representation is ever typed by hand.
"""

import contextlib
import importlib.util
import io
import os
import sys

# do not leave a __pycache__ directory behind when loading the sample
# solutions below
sys.dont_write_bytecode = True

# locate the directories of the exercise
evaldir = os.path.join('..', 'evaluation')
solutiondir = os.path.join('..', 'solution')

# the sample solution of the previous exercise, used to produce the byte
# strings that have to be decompressed
compressiondir = os.path.join('..', '..', '02 compression', 'solution')

os.makedirs(evaldir, exist_ok=True)


def load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


solution = load('solution', os.path.join(solutiondir, 'solution.en.py'))
compression = load(
    'compression', os.path.join(compressiondir, 'solution.en.py')
)

# the texts whose compressed form is decompressed by the test suite
TEXTS = [
    # the example from the description of the previous exercise
    'Hello, world!',

    # boundary cases: no characters at all, and a single character
    '',
    'e',
    ' ',
    'Q',

    # only common characters, with and without padding half-byte
    'ee',
    'eeeeeee',
    'etaoinshrdlcum ',
    'the man in the moon',

    # only uncommon characters
    'QWERTY',
    'ABC 123',

    # a mix of common and uncommon characters, including a newline
    'How much wood would a woodchuck chuck\n',
    'If a woodchuck could chuck wood?\n',
    'Ha! 42 & 0.5%\n',

    # non-ASCII characters and control characters, both of which are stored as
    # three half-bytes as well
    'Ca coute 12,50 EUR',
    '\xc7a co\xfbte 12,50 \xa4',
    '\x00\x01\x02',
    ''.join(chr(value) for value in range(16)),
]

TAB = 'decompress'

LANGUAGE = """<LANGUAGE code="nl">
    <function from="decompress" to="decomprimeer" />
</LANGUAGE>"""


def transcript(statements, namespace):

    """Turn a list of statements into a Python interactive session.

    The statements are executed one after the other in a single namespace, and
    what the interactive interpreter would echo for them is used as the
    expected output of the doctest.
    """

    lines = []

    for source, use_stdout in statements:

        lines.append(
            '>>> {}{}'.format(source, ' # doctest: +STDOUT' if use_stdout else '')
        )

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


statements = []
for text in TEXTS:

    data = compression.compress(text)

    # the sample solutions of both exercises must be each other's inverse
    assert solution.decompress(data) == text, f'no round trip for {text!r}'

    statements.append((f'decompress({data!r})', False))

session = transcript(statements, {'decompress': solution.decompress})

with open(os.path.join(evaldir, '0.in'), 'w', encoding='utf-8') as testfile:
    testfile.write(session)

with open(os.path.join(evaldir, '0.out'), 'w', encoding='utf-8') as testfile:
    testfile.write(
        '--------------------------------------------------------\n'
        f'tab name: {TAB}\n'
        f'{LANGUAGE}'
    )
