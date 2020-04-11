# zin inlezen
zin = input()

# Test of het echt wel een zin is
if len(zin) <= 0:
    exit()

# Eerste letter hoofdletter
nieuwezin = zin[0].upper() + zin[1:]

woordlijst = nieuwezin.split()
laatstewoord = ""
nieuwezin = ""

for w in woordlijst:

    # Dubbele hoofdletters correctie
    if len(w) > 2 and w[0] >= "A" and w[0] <= "Z" and \
            w[1] >= "A" and w[1] <= "Z" and w[2] >= "a" and \
            w[2] <= "z":
        w = w[0] + w[1].lower() + w[2:]

    # Dagen met een hoofdletter
    dag = w.lower()
    if dag == "zondag" or dag == "maandag" or dag == "dinsdag" \
            or dag == "woensdag" or dag == "donderdag" or \
            dag == "vrijdag" or dag == "zaterdag":
        w = dag[0].upper() + dag[1:]

    # CAPS LOCK correctie
    if w[0] >= "a" and w[0] <= "z":
        hoofdletters = True
        for c in w[1:]:
            if not (c >= "A" and c <= "Z"):
                hoofdletters = False
                break
        if hoofdletters:
            w = w[0].upper() + w[1:].lower()

    # Duplicaten verwijderen
    if w == laatstewoord:
        continue

    nieuwezin += w + " "
    laatstewoord = w

nieuwezin = nieuwezin.strip()
print(nieuwezin)