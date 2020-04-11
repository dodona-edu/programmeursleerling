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
input block size: 2
output block size: 1
comparison: exact match
<LANGUAGE code="nl">
    <fixed from="Number of times" to="Aantal keren dat het woord" />
    <fixed from="occurs in the text" to="voorkomt" />
</LANGUAGE>
'''

# generate test data
cases = [
    ('wood', 'How much wood would a woodchuck chuck if a woodchuck could chuck wood? He would chuck, he would, as much as he could, and chuck as much as a woodchuck would If a woodchuck could chuck wood.'),
    ('chuck', 'How much wood would a woodchuck chuck if a woodchuck could chuck wood? He would chuck, he would, as much as he could, and chuck as much as a woodchuck would If a woodchuck could chuck wood.'),
]

# configure test files
infile = open(os.path.join(evaldir, '0.in'), 'w', encoding='utf-8')
outfile = open(os.path.join(evaldir, '0.out'), 'w', encoding='utf-8')

# generate unit tests
for stdin in cases:

    # add input to input file
    stdin = '\n'.join(stdin)
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
