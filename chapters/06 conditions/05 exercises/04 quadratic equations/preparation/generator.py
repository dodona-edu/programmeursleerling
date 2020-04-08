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
tab name: Solutions
python input without prompt: true
block count: multi
input block size: 3
output block size: 1
ignore fp rounding: -6
<LANGUAGE code="nl">
    <fixed from="Invalid equation" to="Ongeldige vergelijking" />
    <fixed from="There is 1 real-valued solution" to="Er is 1 reële oplossing" />
    <fixed from="There are 2 real-valued solutions" to="Er zijn 2 reële oplossingen" />
    <fixed from="There are no real-valued solutions" to="Er zijn geen reële oplossingen" />
    <fixed from=" and " to=" en " detect="false" />
    <fixed from="Solutions" to="Oplossingen" detect="false" />
</LANGUAGE>
'''

# generate test data
cases = [
    (1, 4, -5),
    (1, -12, 36),
    (4, 2, 7),
    (0, 0, 3),
]
while len(cases) < 50:
    if random.random() < 0.2:
        a = 0
        if random.random() < 0.5:
            b = 0
        else:
            b = random.randint(-10, 10)
    else:
        a = random.randint(-10, 10)
        if random.random() < 0.2:
            b = 0
        else:
            b = random.randint(-10, 10)
    c = random.randint(-10, 10)
    parameters = (a, b, c)
    if parameters not in cases:
        cases.append(parameters)

# configure test files
infile = open(os.path.join(evaldir, '0.in'), 'w', encoding='utf-8')
outfile = open(os.path.join(evaldir, '0.out'), 'w', encoding='utf-8')

# generate unit tests
for stdin in cases:

    # add input to input file
    stdin = '\n'.join(str(line) for line in stdin)
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
