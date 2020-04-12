Om exceptions expliciet in je programma af te handelen, gebruik je de
`try … except` constructie. Er zijn verschillende manieren om deze
constructie toe te passen.

### `try` … `except`

De meest basale vorm van de `try … except` constructie heeft de
volgende syntax:

```python
try:
    <acties>
except:
    <exception afhandeling>
```

Als de `<acties>` tussen `try:` en `except:` worden uitgevoerd en er een
exception wordt gegenereert, springt Python onmiddellijk naar de
`<exception afhandeling>` en voert die uit, waarna het programma
vervolgt met de regels code onder de `<exception afhandeling>`. Als er
geen exceptions optreden gedurende de uitvoering van `<acties>`, wordt
de `<exception afhandeling>` overgeslagen.

Gebruik makend van exception afhandeling, kan de code aan het begin van
dit hoofdstuk als volgt geschreven worden om runtime errors te
vermijden:

```python
from pcinput import getInteger

num = getInteger( "Geef een getal: " )
try:
    print( "3 gedeeld door {} is {}".format( num, 3/num ) )
except:
    print( "Je kunt niet delen door nul" )
print( "Tot ziens!" )
```

Meerdere statements mogen binnen een enkele `try … except` gebruikt
worden. Bijvoorbeeld, de volgende code genereert een exception als de
gebruiker een nul ingeeft of als de gebruiker een 3 ingeeft. Beide
uitzonderingen worden via dezelfde `try … except` constructie
afgehandeld.

```python
from pcinput import getInteger

num = getInteger( "Geen een getal: " )
try:
    print( "3 gedeeld door {} is {}".format( num, 3/num ) )
    print( "3 gedeeld door {}-3 is {}".format( num, 3/(num-3) ) )
except:
    print( "Je kunt niet delen door nul" )
print( "Tot ziens!" )
```

Dit is een beetje lelijk, niet alleen omdat deze fouten vermeden hadden
kunnen worden in plaats van ze af te handelen via exceptions, maar ook
omdat wanneer een exception optreedt het onduidelijk is welk van de twee
statements deze veroorzaakt heeft (hoewel je in dit geval kunt zien dat
als je 3 ingeeft, de eerste van de twee statements onder de `try`
correct is uitgevoerd). Maar dit is slechts een demonstratie, en er zijn
zeker situaties te bedenken waarin je zegt: "het maakt mij niet uit waar
er een exception optreedt in deze regels code, maar als er iets gebeurt,
wil ik in ieder geval *dit* doen."

### Afhandeling van specifieke exceptions

Bekijk de code hieronder. Er kunnen minstens twee exceptions optreden
als deze code wordt uitgevoerd. Welke?

```python
print( 3 / int( input( "Geef een getal: " ) ) )
```

De twee exceptions die in deze code kunnen optreden zijn de
`ZeroDivisionError` als je een nul ingeeft, en de `ValueError` als je
iets ingeeft dat geen integer is. Probeer het als je dat niet al gedaan
hebt.

Je kunt beide exceptions afhandelen met een enkele `try … except`
constructie, maar je kunt ze ook van elkaar onderscheiden door meerdere
`except`s te gebruiken. Iedere `except` kan gevolgd worden door één van
de specifieke exceptions, en de code die bij die `except` hoort wordt
alleen uitgevoerd als die specifieke exception wordt gegenereerd.

```python
try:
    print( 3 / int( input( "Geef een getal: " ) ) )
except ZeroDivisionError:
    print( "Je kunt niet delen door nul" )
except ValueError:
    print( "Je gaf geen getal" )
print( "Tot ziens!" )
```

Als je "alle overige exceptions" wilt afhandelen, kun je een `except`
zonder specifieke exception aan het einde toevoegen. Slechts één van de
`except`s zal worden uitgevoerd, namelijk de eerste die wordt
aangetroffen die van toepassing is. Dit werkt dus ongeveer als een
`if … elif … elif … else` constructie.

```python
try:
    print( 3 / int( input( "Geef een getal: " ) ) )
except ZeroDivisionError:
    print( "Je kunt niet delen door nul" )
except ValueError:
    print( "Je gaf geen getal" )
except:
    print( "Iets onverwachts ging fout" )
print( "Tot ziens!" )
```

Hier zijn een aantal specifieke exceptions die vaak optreden:

-   `ZeroDivisionError`: Delen door nul

-   `IndexError`: Het benaderen van een list of tuple met een index die
    niet binnen het legale bereik valt

-   `KeyError`: Het benaderen van een dictionary met een key die
    onbekend is

-   `IOError`: Iedere fout die kan optreden als je een bestand benadert
    (deze exception is een alias voor `OSError`)

-   `FileNotFoundError`: Het proberen te openen van een niet-bestaand
    bestand om eruit te lezen

-   `ValueError`: Het optreden van een fout bij het "casten" van een
    waarde naar een andere waarde

-   `TypeError`: Het gebruiken bij een operatie van een waarde met een
    data type dat niet ondersteund wordt door de operatie

De code hieronder kan verschillende exceptions genereren. Deze worden nu
afgehandeld door een enkele `try … except` constructie. Breid deze
code uit met de expliciete afhandeling van alle exceptions die van
toepassing zijn (er zijn er minimaal drie). Ik wil hierbij benadrukken
dat ik liever zie dat je exceptions vermijdt dan dat je ze afhandelt,
maar in dit geval wil ik je laten oefenen met het afhandelen van
exceptions.

```python
fruitlist = ["appel", "banaan", "kers"]
try:
    num = input( "Geef een getal: " )
    if "." in num:
        num = float( num )
    else:
        num = int( num )
    print( fruitlist[num] )
except:
    print( "Er ging iets fout" )    
```

### Toevoegen van een `else`

Aan het einde van een `try … except` constructie kun je een `else`
toevoegen. De acties die bij de `else` staan worden alleen uitgevoerd
als er geen exception optreedt. Bijvoorbeeld, in de code hieronder wordt
de berekende waarde voor `num` alleen getoond als er geen exception
wordt gegenereerd.

```python
try:
    num = 3 / int( input( "Geef een getal: " ) ) 
except ZeroDivisionError:
    print( "Je kunt niet delen door nul" )
except ValueError:
    print( "Je gaf geen getal" )
except:
    print( "Iets onverwachts ging fout" )
else:
    print( num )
print( "Tot ziens!" )
```

Zelf geef ik er de voorkeur aan geen `else` te gebruiken bij een
exception, omdat het voor mij aanvoelt alsof de code onder de `except`s
code is die alleen moet worden uitgevoerd in uitzonderlijke
omstandigheden. Maar het staat je vrij deze constructie te gebruiken als
je er het nut van inziet.

### Toevoegen van een `finally`

Je kunt nog een extra tak toevoegen aan een `try` constructie, namelijk
`finally`. Bij `finally` kun je een serie statements opnemen die worden
uitgevoerd ongeacht de wijze waarop de `try` constructie wordt verlaten.
Als alles normaal verloopt, worden de statements bij de `finally`
uitgevoerd, maar ook als je een runtime error krijgt, worden ze
uitgevoerd. Je kunt bijvoorbeeld `finally` gebruiken om er zeker van te
zijn dat een bestand dat je geopend hebt, wordt gesloten.

```python
try:
    fp = open( "pc_rose.txt" )
    print( "Bestand geopend" )
    print( fp.read() )
finally:
    fp.close()
    print( "Bestand gesloten" )
```

### Informatie over een exception

Je kunt extra informatie krijgen over een exception door een `as` toe te
voegen aan een `except`, middels de syntax
`except <exception> as <variabele>`. De variabele bevat dan een
exception "object," dat meer informatie bevat over de exception. Helaas
is er geen standaard manier waarop je de informatie eruit kunt krijgen:
het is afhankelijk van de specifieke exception wat de variabele bevat.

De variabele bevat altijd een tuple met argumenten, die tijdens het
genereren van de exception bepaald zijn. Je kunt deze argumenten
inspecteren middels `<variabele>.args`. Een `ValueError` krijgt een
tuple met slechts één waarde, namelijk een string.

```python
try:
    print( int( "GeenInteger" ) )
except ValueError as ex:
    print( ex.args )
```

Als je de code hieronder uitvoert, zie je dat een `IOError` een tuple
met twee waardes heeft: een integer en een string. De integer is kan erg
informatief zijn, aangezien hij aangeeft wat er fout ging (als je de
codes snapt).

```python
try:
    fp = open( "GeenBestand" )
    fp.close()
except IOError as ex:
    print( ex.args )
```

### Advies voor het gebruik van exception afhandeling

Als je een exception opvangt in je code, handel hem dan ook netjes af,
en negeer hem niet. Gebruik zeker geen generieke `try … except`
constructie waarna je niks doet met een exception. Als je denkt dat je
een bepaalde exception veilig kunt negeren, vang dan alleen die
specifieke exception af, en zet commentaar in je programma dat aangeeft
waarom je meent dat je de exception kunt negeren. In principe moeten
alle exceptions in je programma ofwel afgehandeld worden, ofwel het
programma laten crashen.
