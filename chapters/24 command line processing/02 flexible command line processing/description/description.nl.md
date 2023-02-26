Als ik Python programma's schrijf, geef ik de voorkeur aan werken met
een editor. Er zijn een paar editors die het meegeven van command-line
argumenten ondersteunen tijdens testen, maar de meeste doen dat niet.
Dus ik wil mijn programma's zodanig bouwen dat ze command-line
argumenten kunnen verwerken, maar ik ze toch kan testen vanuit een
editor, en het testen van het programma in de echte command shell
slechts éénmalig hoef te doen. Dat doe ik als volgt:

Voor iedere parameter die een waarde moet krijgen via de command line,
creëer ik een globale variabele. Ik vul die globale variabelen met
default waardes. In de rest van het programma gebruik ik die variabelen
alsof het constanten zijn. Slechts bij de start van het hoofdprogramma
controleer ik of er command-line argumenten zijn meegegeven, en als dat
zo is, overschrijf ik de variabelen met de waardes die op de command
line staan.

Het voordeel van deze aanpak is dat ik mijn programma kan ontwikkelen
zonder command-line parameters te gebruiken. Als ik verschillende
waardes voor de command-line argumenten wil testen, stop ik gewoon
andere waardes in de variabelen die ik gebruik om de command-line
argumenten op te slaan. Ik kan het programma zelfs zo opzetten dat ik de
variabele ofwel vul met een command-line parameter als die is
meegegeven, ofwel de gebruiker vraag om een waarde voor de command-line
parameter als die niet is meegegeven.

Zulk soort code ziet er typisch als volgt uit:

```python
import sys

# 3 variabelen die de command line parameters bevatten
invoer = "input.txt"
uitvoer = "output.txt"
shift = 3

# Verwerken van command line parameters
# (werkt met 0, 1, 2, of 3 parameters)
if len( sys.argv ) > 1:
    invoer = sys.argv[1]
if len( sys.argv ) > 2:
    uitvoer = sys.argv[2]
if len( sys.argv ) > 3:
    try:
        shift = int( sys.argv[3] )
    except TypeError:
        print( sys.argv[3], "is geen getal." )
        sys.exit(1)
```

Deze code ondersteunt drie command line argumenten: de eerste twee zijn
strings, en de derde is een integer. De derde wordt onmiddellijk
geconverteerd van een string naar een integer (aangezien een command
line argument altijd een string is), en het programma wordt afgebroken
als deze conversie mislukt. Ik zou meer controles hebben kunnen inbouwen
in deze demonstratie, maar ik neem aan dat dat op dit punt in je
programmeercarrière geen probleem voor je is.

Merk op dat alledrie de argumenten een default waarde hebben: de eerste
string heeft als default waarde `"input.txt"`, de tweede string heeft
als default waarde `"output.txt"`, en de integer heeft als default
waarde 3. Je hoeft niet alle argumenten op de command line mee te geven:
als je er geen mee geeft, worden alle drie de default waardes gebruikt;
als je er één meegeeft, wordt de eerste string overschreven met het
command-line argument, en houden de andere twee hun default waarde;
etcetera.

### `sys.exit()`

In de code hierboven wordt het programma afgebroken via `sys.exit()` als
een argument niet voldoet aan de gestelde eisen. `sys.exit()` heb ik
geïntroduceerd in hoofdstuk
7.
Ik vertelde er toen niet bij dat `sys.exit()` een numeriek argument kan
krijgen, zoals je hierboven ziet. Dit argument wordt geretourneerd naar
het batchbestand waarin het programma is aangeroepen, en het
batchbestand kan er mogelijk op reageren. Meestal is dit argument een
foutcode. Typisch wordt nul als argument gegeven als alles in principe
correct verwerkt is (een programma dat "normaal" eindigt retourneert ook
een nul), en anders wordt een ander getal gebruikt. Omdat sommige
systemen deze getallen beperken tot de waardes 0 tot en met 255, is het
de gewoonte om die restrictie ook te gebruiken voor de waardes die
`sys.exit()` als argument mee kan krijgen.

### `argparse`

Er bestaat een module die command-line verwerking ondersteunt, namelijk
de standaard module `argparse`. Om eerlijk te zijn zie ik zelf het nut
van zo'n module niet in, omdat command-line verwerking te simpel is om
er veel tijd aan te spenderen. Maar sommige Python programma's, met name
programma's die bedoeld zijn om het besturingssysteem uit te breiden,
kennen een grote variëteit aan command-line argumenten, en kunnen
profiteren van een dergelijke module. Als je erin geïnteresseerd bent,
kun je er de documentatie op nalezen.
