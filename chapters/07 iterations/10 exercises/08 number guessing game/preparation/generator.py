import os
import random
import subprocess
import sys

# locate evaldir
evaldir = os.path.join('..', 'evaluation')
if not os.path.exists(evaldir):
    os.makedirs(evaldir)

# locate solutiondir
solutiondir = os.path.join('..', 'solution')
if not os.path.exists(solutiondir):
    os.makedirs(solutiondir)

# The submitted program picks the number to guess itself, using the random
# module. The judge executes submitted code without seeding that module, so the
# number to guess differs from run to run and the generated output can not be
# compared to a fixed expected output. Each test therefore consists of
#
#   1. a fixed sequence of guesses that contains every number of the interval
#      [1, 1000], so that the program terminates whatever number it picked;
#
#   2. a custom evaluation function that checks that the generated output is a
#      consistent reaction to those guesses, worded exactly as the sample
#      solution words it (the expected output of a sample run is used as the
#      reference for that wording, and is translated by the LANGUAGE block
#      before the comparison, just as with a regular comparison).
#
# Every test needs its own guess sequence, and the custom evaluation function
# only sees the output of a single run, so every test goes in its own pair of
# test files (which Dodona shows as separate tabs).

# guess sequences, as source code fragments that are shared between this
# generator and the custom evaluation functions it writes
INCREASING = 'guesses = list(range(1, 1001))'
DECREASING = 'guesses = list(range(1000, 0, -1))'
ALTERNATING = '''guesses = [
    number
    for offset in range(500)
    for number in (1 + offset, 1000 - offset)
]'''
SCATTERED_1 = 'guesses = [(333 * index) % 1000 + 1 for index in range(1000)]'
SCATTERED_2 = 'guesses = [(111 * index) % 1000 + 1 for index in range(1000)]'

# the tests: tab name, guess sequence and the number the sample run should pick
# (picked such that the sample run is short and, where the sequence allows it,
# says both lower and higher at least once)
tests = [
    ('Increasing', INCREASING, 37),
    ('Decreasing', DECREASING, 968),
    ('Alternating', ALTERNATING, 993),
    ('Scattered 1', SCATTERED_1, 997),
    ('Scattered 2', SCATTERED_2, 555),
]

# configuration settings
settings = '''
tab name: {tab}
python input without prompt: true
block count: one
<LANGUAGE code="nl">
    <fixed from="You guessed it!" to="Je hebt het geraden!" />
    <fixed from="Number of attempts" to="Aantal pogingen" />
    <fixed from="Lower" to="Lager" />
    <fixed from="Higher" to="Hoger" />
</LANGUAGE>
<DEFINITION>
{checker}
</DEFINITION>
'''

# custom evaluation function, with the guess sequence of the test filled in
checker = '''def customEvaluate(expected_output, generated_output):

    """
    Checks that the generated output is a consistent reaction to the guesses
    that were fed to the program, and that it uses the same wording as the
    sample solution. The number to guess is picked at random by the program
    itself, so the expected output and the generated output are reactions to
    the same guesses, but almost always to a different number to guess.
    """

    # the guesses that were fed to the program, in the order they are read
{guesses}

    def analyse(output):

        # the program writes one line for each guess it reads, and ends with a
        # line that reports the number of attempts
        lines = [line.rstrip('\\n') for line in output]
        if len(lines) < 2 or len(lines) > len(guesses) + 1:
            return None
        responses, report = lines[:-1], lines[-1]

        # the last response announces the correct guess, so the number to
        # guess must have been the last guess that was read
        number = guesses[len(responses) - 1]

        # all earlier responses must consistently say lower or higher
        words = dict(lower=None, higher=None)
        for guess, response in zip(guesses, responses[:-1]):
            key = 'lower' if number < guess else 'higher'
            if words[key] is None:
                words[key] = response
            elif words[key] != response:
                return None
        words['correct'] = responses[-1]
        if words['correct'] in (words['lower'], words['higher']):
            return None

        # the last line must report the number of guesses that were read
        attempts = str(len(responses))
        head, found, tail = report.rpartition(attempts)
        if not found:
            return None
        words['report'] = (head, tail)

        return words

    expected = analyse(expected_output)
    generated = analyse(generated_output)
    if expected is None or generated is None:
        return False

    # the number of attempts must be reported as the sample solution reports it
    if generated['report'] != expected['report']:
        return False

    # the responses must be worded as the sample solution words them; a
    # response the sample run did not produce must at least differ from all
    # responses it did produce
    for key in ('lower', 'higher', 'correct'):
        response = generated[key]
        if response is None:
            continue
        if expected[key] is not None:
            if response != expected[key]:
                return False
        elif response in (
            expected['lower'], expected['higher'], expected['correct']
        ):
            return False

    return True'''

# source code that seeds the random module before running the sample solution,
# so that the sample run in the expected output is reproducible
runner = '''
import random
import sys
random.seed(int(sys.argv[1]))
with open(sys.argv[2], encoding='utf-8') as handle:
    source = handle.read()
exec(compile(source, sys.argv[2], 'exec'), {'__name__': '__main__'})
'''


def find_seed(number):

    """
    Find a seed for which the first call of randint(1, 1000) returns the given
    number, so that the sample solution can be made to pick that number.
    """

    for seed in range(1000000):
        if random.Random(seed).randint(1, 1000) == number:
            return seed
    raise ValueError(f'no seed found for {number}')


script = os.path.join(solutiondir, 'solution.en.py')

for index, (tab, fragment, number) in enumerate(tests):

    # evaluate the guess sequence that is also written into the test file
    namespace = {}
    exec(fragment, namespace)
    guesses = namespace['guesses']
    assert sorted(guesses) == list(range(1, 1001)), 'guesses must be a permutation'

    # write the guesses to the input file
    with open(os.path.join(evaldir, f'{index}.in'), 'w', encoding='utf-8') as infile:
        for guess in guesses:
            print(guess, file=infile)

    # run the sample solution on those guesses, with the random module seeded
    # so that it picks the number of this test
    process = subprocess.run(
        [sys.executable, '-c', runner, str(find_seed(number)), script],
        input='\n'.join(str(guess) for guess in guesses) + '\n',
        encoding='utf-8',
        capture_output=True, check=True
    )

    # write the output of the sample run, followed by the settings
    with open(os.path.join(evaldir, f'{index}.out'), 'w', encoding='utf-8') as outfile:
        print(process.stdout, file=outfile, end='')
        print('-' * 60, file=outfile, end='')
        print(settings.format(
            tab=tab,
            checker=checker.replace(
                '{guesses}',
                '\n'.join('    ' + line for line in fragment.splitlines())
            )
        ), file=outfile, end='')
