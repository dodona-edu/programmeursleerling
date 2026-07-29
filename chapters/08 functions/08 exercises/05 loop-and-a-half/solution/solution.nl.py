def getInteger(prompt):

    """
    Vraag een geheel getal met de gegeven prompt, en blijf vragen zolang de
    gebruiker geen geldig geheel getal invoert. (Dit is pcinput.getInteger().)
    """

    while True:
        try:
            getal = int(input(prompt))
        except ValueError:
            print("Dat is geen geheel getal -- probeer opnieuw")
            continue
        return getal


def vraag_geldig_getal(prompt):

    """
    Vraag een geheel getal met de gegeven prompt, en blijf vragen tot de
    gebruiker een waarde tussen 0 en 1000 (inclusief) invoert.
    """

    while True:
        getal = getInteger(prompt)
        if 0 <= getal <= 1000:
            return getal
        print("De nummers moeten tussen 0 en 1000 liggen")


def main():

    while True:
        x = vraag_geldig_getal("Geef nummer 1: ")
        if x == 0:
            break
        y = vraag_geldig_getal("Geef nummer 2: ")
        if y == 0:
            break
        if x % y == 0 or y % x == 0:
            print("Fout: de nummers mogen geen delers zijn")
            return
        print("Vermenigvuldiging van", x, "met", y, "geeft", x * y)

    print("Tot ziens!")


if __name__ == '__main__':
    main()
