import math
import random

# read number of simulations
simulations = int(input())

# throw dart at random position in unit square and determine how many are within
# distance of 1 to left bottom corner of unit square
closer = 0
for _ in range(simulations):

    # determine random position of dart
    x = random.random()
    y = random.random()

    # determine distance to left bottom corner
    distance = math.sqrt(x ** 2 + y ** 2)

    # determine if dart is within distance of 1 to left bottom corner
    if distance < 1:
        closer += 1

# print approximation of pi
print(4 * closer / simulations)
