# read three integers
number1 = int(input())
number2 = int(input())
number3 = int(input())

# grootste, kleinste en gemiddelde bepalen
print(f'maximum: {max(number1, number2, number3)}')
print(f'minimum: {min(number1, number2, number3)}')
print(f'average: {sum((number1, number2, number3)) / 3:.2f}')
