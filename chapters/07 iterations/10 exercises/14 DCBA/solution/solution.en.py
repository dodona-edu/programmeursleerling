for A in range(1, 10):
    for B in range(0, 10):
        for C in range(0, 10):
            for D in range(1, 10):
                if (
                    len({A, B, C, D}) == 4 and
                    1000 * D + 100 * C + 10 * B + A == 4 * (1000 * A + 100 * B + 10 * C + D)
                ):
                    print(f'{D}{C}{B}{A} = 4 * {A}{B}{C}{D}')
