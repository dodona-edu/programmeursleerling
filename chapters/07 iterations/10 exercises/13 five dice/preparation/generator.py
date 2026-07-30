import os
from math import comb

# locate evaldir
evaldir = os.path.join('..', 'evaluation')
if not os.path.exists(evaldir):
    os.makedirs(evaldir)

# configuration settings
settings = r'''
tab name: Tests
python input without prompt: true
block count: multi
input block size: 1
output block size: 1
ignore fp rounding: -2
time limit: 42
<LANGUAGE code="nl">
    <regex from="non-decreasing sequence of ([0-9]+) dice" to="niet-dalende reeks van \1 dobbelstenen" />
    <fixed from="decreasing" to="dalende" />
    <fixed from="sequence" to="reeks" />
    <fixed from="dice" to="dobbelstenen" />
</LANGUAGE>
'''

# generate test data
cases = list(range(1, 11))

# configure test files
infile = open(os.path.join(evaldir, '0.in'), 'w', encoding='utf-8')
outfile = open(os.path.join(evaldir, '0.out'), 'w', encoding='utf-8')

# generate unit tests
for stdin in cases:

    # add input to input file
    n = stdin
    print(n, file=infile)

    # compute the exact probability: C(n+5, n) / 6**n
    probability = comb(n + 5, n) / 6 ** n

    # add expected output to output file
    print(f'P(non-decreasing sequence of {n} dice) = {round(probability, 6)}', file=outfile)

# add settings to output file
print('-' * 60 + settings, file=outfile, end='')
