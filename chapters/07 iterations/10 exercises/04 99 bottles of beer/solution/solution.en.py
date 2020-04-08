# read initial number of bottles on the wall
bottles = int(input())

while bottles:

    s = '' if bottles == 1 else 's'
    print(f'{bottles} bottle{s} of beer on the wall, {bottles} bottle{s} of beer.')

    bottles -= 1
    s = '' if bottles == 1 else 's'
    print(f'Take one down, pass it around, {bottles} bottle{s} of beer on the wall.')
