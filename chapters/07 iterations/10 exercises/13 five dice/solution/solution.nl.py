import random

# aantal dobbelstenen inlezen
aantal_dobbelstenen = int(input())

# worpen met dobbelsteen simuleren
positief = 0
aantal_simulaties = 1000000
for _ in range(aantal_simulaties):

    # werp het gegeven aantal dobbelstenen
    worpen = 0
    stijgend = True
    vorige_waarde = 0
    while worpen < aantal_dobbelstenen and stijgend:

        # gooi volgende dobbelsteen
        waarde = random.randint(1, 6)
        worpen += 1

        # controleer dat waarde niet lager is dan die van vorige dobbelsteen
        if waarde < vorige_waarde:
            stijgend = False

        # vorige waarde onthouden
        vorige_waarde = waarde

    # stijgende reeks waarden wordt als positieve uitkomst aanzien
    if stijgend:
        positief += 1

kans = positief / aantal_simulaties
print(f'P(niet-dalende reeks van {aantal_dobbelstenen} dobbelstenen) = {kans}')
