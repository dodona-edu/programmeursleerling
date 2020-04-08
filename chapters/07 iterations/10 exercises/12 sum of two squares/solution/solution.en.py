import math

# read upper and lower limits
lower_limit = int(input())
upper_limit = int(input())

# vierkantswortels van grenzen bepalen
lower = math.ceil(math.sqrt(lower_limit))
upper = math.floor(math.sqrt(upper_limit)) + 1

# print sum of squares
for x in range(0, upper):
    for y in range(x, upper):
        z = x ** 2 + y ** 2
        if lower_limit <= z <= upper_limit:
            print(f'{x} ** 2 + {y} ** 2 = {z}')
