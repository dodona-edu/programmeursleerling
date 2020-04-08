# read number
number = int(input())

# print first row
width = len(str(number))
row = f'{"":{width}s} |'
for m in range(1, number + 1):
    width = len(str(m * number))
    row += f' {m:{width}d}'
print(row)

# print row of hyphens
print('=' * len(row))

# print other rows
for n in range(1, number + 1):
    width = len(str(number))
    row = f'{n:{width}d} |'
    for m in range(1, number + 1):
        width = len(str(m * number))
        row += f' {m * n:{width}d}'
    print(row)
