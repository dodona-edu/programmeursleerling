import math
import random

# aantal simulaties inlezen
simulaties = int(input())

# gooi darts op willekeurige positie en tel hoeveel er op een afstand kleiner
# dan 1 van de linkeronderhoek liggen
dichter = 0
for _ in range(simulaties):

    # bepaal willekeurige positie van dart
    x = random.random()
    y = random.random()

    # bepaal afstand van dart tot linkeronderhoek
    afstand = math.sqrt(x ** 2 + y ** 2)

    # bepaal of dart op afstand kleiner dan 1 van linkeronderhoek ligt
    if afstand < 1:
        dichter += 1

# benadering van pi uitschrijven
print(4 * dichter / simulaties)
