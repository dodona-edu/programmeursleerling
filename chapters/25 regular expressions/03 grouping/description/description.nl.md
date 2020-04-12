Zoals ik hierboven heb uitgelegd, kun je groepen maken binnen een
reguliere expressie middels haakjes. De reguliere expressie
`(\d{1,2})-(\d{1,2})-(\d{4})` kan bijvoorbeeld een datum beschrijven:
één of twee cijfers, gevolgd door een streepje, gevolgd door één of twee
cijfers, gevolgd door een streepje, gevolgd door vier cijfers (als je
deze reguliere expressie niet begrijpt, bestudeer dan de eerdere delen
van dit hoofdstuk totdat je hem wel begrijpt). Deze expressie bevat drie
groepen: de eerste bestaand uit één of twee cijfers, de tweede bestaand
uit één of twee cijfers, en de derde bestaand uit vier cijfers. De code
hieronder zoekt naar dit patroon in een string.

```python
import re

pDatum = re.compile( r"(\d{1,2})-(\d{1,2})-(\d{4})" )
m = pDatum.search( "In antwoord op uw schrijven van 25-3-2015, \
heb ik besloten een huurmoordenaar op u af te sturen." )
if m:
    print( "Datum: {}; dag: {}; maand: {}; jaar: {}".format( 
            m.group(0), m.group(1), m.group(2), m.group(3) ) )
```

Als je deze code uitvoert, zie je dat niet alleen het resultaat als
geheel wordt gevonden (via de methode `group()` of `group(0)`), maar ook
dat je ieder van de groepen afzonderlijk kunt benaderen, via methodes
`group(1)` voor de dag, `group(2)` voor de maand, en `group(3)` voor het
jaar. Je kunt ook de methode `groups()` gebruiken om een tuple te
krijgen waarin alle groepen zitten.

### `findall()` en groepen

De `findall()` methode retourneert een list van patroon objecten. In de
voorbeelden die ik tot nu toe heb gegeven, was dat een list van strings.
En inderdaad is een patroon object een string als er ten hoogste één
groep in de reguliere expressie zit. Als er meerdere groepen zijn, is
een patroon object een tuple waarin alle groepen zitten.

```python
import re

pDatum = re.compile( r"(\d{1,2})-(\d{1,2})-(\d{4})" )
datumlist = pDatum.findall( "In antwoord op uw schrijven van \
25-3-2015, heb ik op 27-3-2015 besloten u verder te negeren." )
for datum in datumlist:
    print( datum )
```

### Benoemde groepen

Het is mogelijk om iedere groep een naam te geven, via de constructie
`?P<naam>` (waarbij je voor "naam" de naam invult die je aan de groep
wilt geven – in dit geval laat je de `<` en `>` dus in de uitdrukking
staan) onmiddellijk achter het openingshaakje. Je kunt daarna aan de
groepen refereren met hun naam, in plaats van een index.

```python
import re

pDatum = re.compile( 
    r"(?P<dag>\d{1,2})-(?P<maand>\d{1,2})-(?P<jaar>\d{4})" )
m = pDatum.search( "In antwoord op uw schrijven van 25-3-2015, \
heb ik besloten een zingend telegram op u af te sturen." )
if m:
    print( "dag is {}".format( m.group('dag') ) )
    print( "maand is {}".format( m.group('maand') ) )
    print( "jaar is {}".format( m.group('jaar') ) )
```

### Refereren binnen een reguliere expressie

Stel dat je een reguliere expressie moet schrijven die een string
representeert waarin een willekeurig teken (dat geen spatie is) twee
keer voorkomt. Bijvoorbeeld, de string "gasoven" zou geen match geven,
maar de string "magnetron" wel (aangezien de `"n"` twee keer voorkomt).
Dit kun je niet doen met de mogelijkheden van reguliere expressies die
ik tot nu toe bediscussieerd heb. Je kunt het echter oplossen met
groepen, en speciale referenties binnen reguliere expressies, als volgt:
je gebruikt het speciale teken `\\x`, waarbij `x` een cijfer is, waarmee
je dan refereert aan de groep met index `x` in het patroon. Dus de
gevraagde reguliere expressie is `(\\S).*\\1`.

Omdat op dit punt deze reguliere expressie misschien wat moeilijk te
begrijpen is, zal ik hem in detail doornemen. De `\\S` is een speciaal
teken dat een non-spatie voorstelt. Door er haakjes omheen te zetten,
wordt het een groep, en omdat de eerste (en enige) groep is, is de index
1. De `.*` stelt een serie van nul of meer tekens voor die alles kunnen
zijn (de punt is een meta-teken dat ieder teken kan voorstellen).
Tenslotte is de `\\1` een referentie aan de eerste groep, en stelt dat
je hier exact moet hebben wat de eerste groep is. Als je je afvraagt of
je niet ook moet beschrijven wat er vóór de `\\S` of na de `\\1` komt,
dan is het antwoord dat dat niet nodig is, aangezien deze reguliere
expressie niet de string als geheel representeert. Dus zolang dit maar
ergens voorkomt in de string, wordt het patroon gevonden.

Test deze reguliere expressie in de code hieronder, waarbij je de string
`"Monty Python's Flying Circus"` vervangt door andere strings, en het
resultaat van de uitvoering bekijkt.

```python
import re

m = re.search( r"(\S).*\1", "Monty Python's Flying Circus" )
if m:
    print( "{} komt twee keer voor in de string".format( 
        m.group(1) ) )
else:
    print( "Geen match gevonden." )
```

Kun je de reguliere expressie in de code hierboven zo wijzigen dat het
een patroon beschrijft waarbij een willekeurig teken minimaal drie keer
voorkomt?

Kun je de reguliere expressie wijzigen zodat het een patroon beschrijft
waarbij twee tekens twee keer voorkomen? Dit is behoorlijk moeilijk en
daarom optioneel, maar als je het probeert, zorg er dan voor dat je het
test met op zijn minst de strings `"aaaa"`, `"aabb"`, `"abab"` and
`"abba"`. Deze moeten allemaal een match geven, tenzij je ook nog eist
dat de twee tekens verschillend moeten zijn, in welk geval `"aaaa"` geen
match mag geven (maar dat maakt de reguliere expressie nog eens een stuk
moeilijker).
