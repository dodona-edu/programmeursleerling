import os
import random
import subprocess

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

# configuration settings
settings = f'''
tab name: Tests
python input without prompt: true
block count: multi
input block size: 1
output block size: 1
comparison: exact match
'''

# helper function for generating test data
def contains(word, sentence):

    """
    >>> contains('wonder', 'And now for something completely different')
    True
    >>> contains('wonder', 'Always look on the bright side of life.')
    False
    """

    index = -1
    for character in word:
        index = sentence.find(character, index + 1)
        if index == -1:
            return False

    return True

def hide(word, sentence):

    """
    >>> hide('wonder', 'And now for something completely different')
    'And no[w] f[o]r somethi[n]g completely [d]iff[er]ent'
    >>> hide('wonder', 'Always look on the bright side of life.')
    'Al[w]ays l[o]ok o[n] the bright si[de] of life.'
    """

    index = 0
    hidden = ''
    open = False
    word = word.lower()
    for character in sentence:
        if index < len(word) and character.lower() == word[index]:
            if not open:
                hidden += '['
            open = True
            index += 1
        elif open:
            hidden += ']'
            open = False
        hidden += character

    if open:
        hidden += ']'

    return hidden

# generate test data
cases = [
    'And no[w] for s[o]methi[n]g completely [d]iff[er]ent.',
]
with open('quotes.txt') as quotes:
    for quote in quotes:
        quote = quote.strip()
        quote_lower = quote.lower()
        best_word = ''
        with open('words.txt') as words:
            for word in words:
                word = word.strip()
                if (
                    len(word) > len(best_word) and
                    word.islower() and
                    contains(word, quote_lower)
                ):
                    best_word = word
        cases.append(hide(best_word, quote))

# configure test files
infile = open(os.path.join(evaldir, '0.in'), 'w', encoding='utf-8')
outfile = open(os.path.join(evaldir, '0.out'), 'w', encoding='utf-8')

# generate unit tests
for stdin in cases:

    # add input to input file
    print(stdin, file=infile)

    # generate output to output file
    script = os.path.join(solutiondir, 'solution.en.py')
    process= subprocess.run(
        ['python', script],
        input=stdin,
        encoding='utf-8',
        capture_output=True, shell=True, check=True
    )
    stdout = process.stdout

    # add stdout to output file
    print(stdout, file=outfile, end='')

# add settings to output file
print('-' * 60 + settings, file=outfile)
