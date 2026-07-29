import os
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

# Nothing about this exercise is random: the computer bisects the interval of
# numbers that are still possible, and the answers of the user are what this
# generator makes up. The answers of a truthful user are simulated here, and
# then fed to the sample solution to capture the output it really writes.
#
# The program plays a single game before it stops, so every game goes in its own
# pair of test files (which Dodona shows as separate tabs).


def answers(number):

    """
    Simulate the answers of a user that truthfully answers the guesses of the
    sample solution about the given number.
    """

    smallest, largest = 1, 1000
    given = []
    while True:
        guess = (smallest + largest) // 2
        if guess == number:
            given.append('C')
            return given
        elif guess > number:
            given.append('L')
            largest = guess - 1
        else:
            given.append('H')
            smallest = guess + 1


# the games: tab name and the answers the user gives
tests = [
    # the number is guessed straight away
    ('Game 1', answers(500)),
    # the extremes of the interval of possible numbers
    ('Game 2', answers(1)),
    ('Game 3', answers(1000)),
    # numbers scattered over the interval
    ('Game 4', answers(42)),
    ('Game 5', answers(137)),
    ('Game 6', answers(862)),
    # a user that keeps saying that the number is lower, until nothing is left
    ('Impossible 1', list('LLLLLLLLL')),
    # a user that narrows down to 137 and then contradicts that
    ('Impossible 2', list('LLHLLLHHLL')),
]

# configuration settings
settings = '''
tab name: {tab}
python input without prompt: true
block count: one
comparison: exact match
<LANGUAGE code="nl">
    <fixed from="Number of attempts" to="Aantal pogingen" />
    <fixed from="That is impossible!" to="Dat is onmogelijk!" />
    <fixed from="Is it" to="Is het" />
</LANGUAGE>
'''

script = os.path.join(solutiondir, 'solution.en.py')

for index, (tab, given) in enumerate(tests):

    # sanity check: no game may take more than ten guesses
    assert len(given) <= 11, f'{tab} takes too many guesses'

    # write the answers of the user to the input file
    stdin = ''.join(answer + '\n' for answer in given)
    with open(os.path.join(evaldir, f'{index}.in'), 'w', encoding='utf-8') as infile:
        print(stdin, file=infile, end='')

    # run the sample solution on those answers
    process = subprocess.run(
        [sys.executable, script],
        input=stdin,
        encoding='utf-8',
        capture_output=True, check=True
    )

    # write the output of the sample solution, followed by the settings
    with open(os.path.join(evaldir, f'{index}.out'), 'w', encoding='utf-8') as outfile:
        print(process.stdout, file=outfile, end='')
        print('-' * 60, file=outfile, end='')
        print(settings.format(tab=tab), file=outfile, end='')
