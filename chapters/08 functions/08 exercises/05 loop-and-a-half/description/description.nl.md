In hoofdstuk
8
legde ik de loop-en-een-half uit. De uiteindelijke code voor het
voorbeeld dat ik gebruikte had nog steeds iets lelijks, namelijk dat als
`x` kleiner dan 0 of groter dan 1000 was, dat de code nog steeds vroeg
om `y` terwijl het al bekend was dat het een andere waarde voor `x` zou
moeten krijgen. Ik gaf ook aan dat he dat het gemakkelijkste kon
oplossen via functies. Creëer een functie die je aan onderstaande code
toevoegt en in onderstaande code aanroept, zodat het probleem wordt
opgelost. Verwijder ook de `exit()` door introductie van een `main()`
functie. Hint: Maak een variant van `getInteger()` die garandeert dat de
integer tussen 0 en 1000 ligt.

```python
from pcinput import getInteger
from sys import exit

while True:
    x = getInteger( "Geef nummer 1: " )
    if x == 0:
        break
    y = getInteger( "Geef nummer 2: " )
    if y == 0:
        break
    if (x < 0 or x > 1000) or (y < 0 or y > 1000):
        print( "De nummers moeten tussen 0 en 1000 liggen" )
        continue
    if x%y == 0 or y%x == 0:
        print( "Fout: de nummers mogen geen delers zijn" )
        exit()
    print( "Vermenigvuldiging van", x, "met", y, "geeft", x * y )

print( "Tot ziens!" )
```

### Opgave

Schrijf een functie `vraag_geldig_getal` waaraan een prompt (`str`) moet
doorgegeven worden. De functie moet via `getInteger` blijven vragen om een
geheel getal met de gegeven prompt, tot de gebruiker een waarde tussen 0 en
1000 (inclusief) invoert; voor elke waarde buiten dat bereik print je
`De nummers moeten tussen 0 en 1000 liggen` voor je opnieuw vraagt. De functie
moet het gevalideerde getal (`int`) teruggeven.

Herschrijf bovenstaande code naar een functie `main` die geen argumenten
neemt, en gebruik daarbij `vraag_geldig_getal` om het probleem hierboven op
te lossen. Verwijder ook de `exit()` door in de plaats `return` te gebruiken.

### Voorbeeld

```console?lang=python&prompt=>>>
>>> vraag_geldig_getal("Geef nummer 1: ")
Geef nummer 1: -42
De nummers moeten tussen 0 en 1000 liggen
Geef nummer 1: 314
314

>>> main()
Geef nummer 1: -5
De nummers moeten tussen 0 en 1000 liggen
Geef nummer 1: 250
Geef nummer 2: 999
Vermenigvuldiging van 250 met 999 geeft 249750
Geef nummer 1: 0
Tot ziens!
```
