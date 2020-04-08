# parameters van kwadratische vergelijking inlezen
a = float(input())
b = float(input())
c = float(input())

if a == 0:

    if b == 0:
        print('Ongeldige vergelijking')
    else:
        x1 = -c / b
        print(f'Er is 1 reële oplossing: {x1}')

else:

    # discriminant berekenen
    Δ = b ** 2 - 4 * a * c

    # aantal reële oplossingen bepalen
    if abs(Δ) < 1e-6:
        x1 = -b / (2 * a)
        print(f'Er is 1 reële oplossing: {x1}')
    elif Δ > 0:
        x1 = (-b - Δ ** 0.5) / (2 * a)
        x2 = (-b + Δ ** 0.5) / (2 * a)
        print(f'Er zijn 2 reële oplossingen: {x1} en {x2}')
    else:
        print('Er zijn geen reële oplossingen')
