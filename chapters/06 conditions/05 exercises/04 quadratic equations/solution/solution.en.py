# read parameters of quadratic equation
a = float(input())
b = float(input())
c = float(input())

if a == 0:

    if b == 0:
        print('Invalid equation')
    else:
        x1 = -c / b
        print(f'There is 1 real-valued solution: {x1}')

else:

    # compute discriminant
    discriminant = b ** 2 - 4 * a * c

    # determine real-valued solutions
    if abs(discriminant) < 1e-6:
        x1 = -b / (2 * a)
        print(f'There is 1 real-valued solution: {x1}')
    elif discriminant > 0:
        x1 = (-b - discriminant ** 0.5) / (2 * a)
        x2 = (-b + discriminant ** 0.5) / (2 * a)
        print(f'There are 2 real-valued solutions: {x1} and {x2}')
    else:
        print('There are no real-valued solutions')
