"""Generate the test suite of the exercise "compression".

Run this script from within the directory that contains it:

    python3 generator.py

Every expected byte string in the generated doctests is produced by actually
running the sample solution, so no byte string representation is ever typed by
hand.
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

os.makedirs(evaldir, exist_ok=True)

# load functionality defined in sample solution
spec = importlib.util.spec_from_file_location(
    'solution', os.path.join(solutiondir, 'solution.en.py')
)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

# the texts that are compressed by the test suite; the byte strings they must
# be compressed into are computed by running the sample solution
TEXTS = [
    # the example from the description
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

    # non-ASCII characters and control characters, both of which need three
    # half-bytes as well
    'Ca coute 12,50 EUR',
    '\xc7a co\xfbte 12,50 \xa4',
    '\x00\x01\x02',
    ''.join(chr(value) for value in range(16)),
]

TAB = 'compress'

LANGUAGE = """<LANGUAGE code="nl">
    <function from="compress" to="comprimeer" />
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


statements = [(f'compress({text!r})', False) for text in TEXTS]
session = transcript(statements, {'compress': module.compress})

with open(os.path.join(evaldir, '0.in'), 'w', encoding='utf-8') as testfile:
    testfile.write(session)

with open(os.path.join(evaldir, '0.out'), 'w', encoding='utf-8') as testfile:
    testfile.write(
        '--------------------------------------------------------\n'
        f'tab name: {TAB}\n'
        f'{LANGUAGE}'
    )
