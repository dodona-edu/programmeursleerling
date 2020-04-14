import random

# read number of dice
dice = int(input())

# simulate throwing dice
positives = 0
simulations = 100000
for _ in range(simulations):

    # throw given number of dice
    thrown = 0
    increasing = True
    previous_die = 0
    while thrown < dice and increasing:

        # throw the next die
        die = random.randint(1, 6)
        thrown += 1

        # check if value is not lower than previous value
        if die < previous_die:
            increasing = False

        # remember previous value
        previous_die = die

    # increasing sequence is considered positive outcome
    if increasing:
        positives += 1

probability = positives / simulations
print(f'P(non-decreasing sequence of {dice} dice) = {probability}')
