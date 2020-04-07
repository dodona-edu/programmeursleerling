# drie gehele getallen inlezen
getal1 = int(input())
getal2 = int(input())
getal3 = int(input())

# grootste, kleinste en gemiddelde bepalen
print(f'maximum: {max(getal1, getal2, getal3)}')
print(f'minimum: {min(getal1, getal2, getal3)}')
print(f'gemiddelde: {sum((getal1, getal2, getal3)) / 3:.2f}')
