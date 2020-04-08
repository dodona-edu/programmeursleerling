import math

# onder- en bovengrens inlezen
ondergrens = int(input())
bovengrens = int(input())

# vierkantswortels van grenzen bepalen
onder = math.ceil(math.sqrt(ondergrens))
boven = math.floor(math.sqrt(bovengrens)) + 1

# som van kwadraten uitschreven
for x in range(0, boven):
    for y in range(x, boven):
        z = x ** 2 + y ** 2
        if ondergrens <= z <= bovengrens:
            print(f'{x} ** 2 + {y} ** 2 = {z}')
