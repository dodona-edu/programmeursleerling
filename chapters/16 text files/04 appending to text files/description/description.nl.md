"Toevoegen"(Engels: "appending") houdt in dat er geschreven wordt aan
het einde van een bestaand bestand. Als je een bestand opent om toe te
voegen, wordt de inhoud niet verwijderd, maar wordt de pointer geplaatst
aan het einde van het bestand, waar je dan nieuwe data mag wegschrijven.
Om een bestand in deze modus te openen, gebruik je `"a"` als het tweede
argument bij het openen van het bestand.

De code hieronder toont eerst de inhoud van "pc_writetest.tmp" (die nu
zou moeten bestaan). Daarna wordt de gebruiker gevraagd om regels in te
geven die aan het bestand worden toegevoegd. Tenslotte wordt de nieuwe
inhoud van het bestand getoond. Ik heb dit programma iets beter
gestructureerd dan ik hiervoor steeds deed, door gebruik van een
constante voor de bestandsnaam en middels een functie voor het tonen van
de bestandsinhoud.

```python
NAAM = "pc_writetest.tmp"

def tooninhoud( bestandsnaam ):
    fp = open( bestandsnaam )
    print( fp.read() )
    fp.close()

tooninhoud( NAAM )

fp = open( NAAM, "a" )
while True:
    tekst = input( "Geef een regel tekst: " )
    if tekst == "":
        break
    fp.write( tekst+"\n" )
fp.close()

tooninhoud( NAAM )
```
