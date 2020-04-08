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
<LANGUAGE code="nl">
    <fixed from="is not a prime" to="is geen priemgetal" />
    <fixed from="is a prime" to="is een priemgetal" />
</LANGUAGE>
'''

# generate test data
maximum = 10000
primes = [p for p in range(1, maximum + 1) if all(p % d for d in range(2, p))]
noprimes = [p for p in range(1, maximum + 1) if any(not p % d for d in range(2, p))]
cases = random.sample(primes, 25) + random.sample(noprimes, 25)
random.shuffle(cases)

# configure test files
infile = open(os.path.join(evaldir, '0.in'), 'w', encoding='utf-8')
outfile = open(os.path.join(evaldir, '0.out'), 'w', encoding='utf-8')

# generate unit tests
for stdin in cases:

    # add input to input file
    stdin = str(stdin)
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
