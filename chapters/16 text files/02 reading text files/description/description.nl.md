Om een tekstbestand te lezen, moet je het bestand eerst openen, dan de
inhoud lezen, en tenslotte het bestand sluiten.

### Openen van een bestand met `open()`

Om een bestand te openen, gebruik je de `open()` functie.

De `open()` functie krijgt twee argumenten, waarvan de tweede optioneel
is. Het eerste argument is de naam van het bestand. Als het bestand niet
in de huidige directory staat, moet je het complete pad naar het bestand
opgeven zodat Python het kan vinden. Het tweede argument is de "modus."
Deze geeft aan hoe Python het bestand moet behandelen. De default modus
(die gebruikt wordt als er geen argument wordt opgegeven) is dat het
bestand wordt geopend als tekstbestand, en er alleen uit het bestand
gelezen mag worden. Ik zal later bediscussiëren hoe je andere modi
opgeeft.

De `open()` functie retourneert een handle, die je gebruikt voor alle
andere functionaliteiten.

In plaats van `<handle> = open( <bestandsnaam> )`, schrijven Python
programmeurs vaak `open( <bestandsnaam> ) as <handle>`. De tweede manier
is equivalent met de eerste. Ikzelf prefereer de eerste manier, omdat
deze het dichtst ligt bij de manieren waarop andere programmeertalen het
openen van bestanden afhandelen. De tweede methode heeft echter een
klein voordeel, dat ik zal bespreken wanneer ik het heb over het sluiten
van bestanden.

### Lezen uit een bestand met `read()`

De eenvoudigste manier om de inhoud van een bestand te lezen is via de
`read()` methode, zonder argumenten, via de handle. Dit levert een
string die de complete inhoud van het bestand bevat. `read()` kan een
argument krijgen, dat ik zal bespreken in hoofdstuk
<a href="#ch:binaryfiles" data-reference-type="ref" data-reference="ch:binaryfiles">19</a>,
dat gaat over binaire bestanden.

Lezen uit een bestand verplaatst de pointer naar het teken dat volgt
meteen na het laatste teken dat is gelezen. Dat betekent dat als je de
`read()` methode aanroept zonder argumenten, de pointer verplaatst wordt
naar het einde van het bestand (meteen achter het laatste teken in het
bestand). Als je dan `read()` een tweede keer aanroept, valt er niks
meer te lezen, omdat er niks staat na de pointer. `read()` retourneert
dan een lege string.

### Sluiten van een bestand met `close()`

Om een bestand te sluiten gebruik je de `close()` methode met de handle.
Daarna is de handle niet meer gerelateerd aan het bestand. Ieder bestand
dat je opent, moet je op enig moment weer sluiten in je programma.

Een compleet programma dat een bestand opent, de inhoud leest, de inhoud
toont, en het bestand weer sluit, is dus het volgende:

```python
fp = open( "pc_rose.txt" )
print( fp.read() )
fp.close()
```

Als alles wat je met het bestand wilt doen, gedaan kan worden in een
enkel blok code, dan kun je dat blok als volgt schrijven:

```python
with open( <bestandsnaam> ) as <handle>:
    <acties>
```

Deze syntactische constructie heeft als voordeel dat het bestand
automatisch gesloten wordt als het blok `<acties>` eindigt, dus je hoeft
niet expliciet de `close()` methode aan te roepen. Deze constructie is
typisch Python; je ziet hem niet in veel andere programmeertalen.

### Tonen van de inhoud van een bestand

Nu ik de eerste paar functies en methodes voor bestandsmanipulatie heb
geïntroduceerd, kan ik code schrijven die de inhoud van een bestand
leest.

```python
with open( "pc_rose.txt" ) as fp:
    buffer = fp.read()
print( buffer )
```

Deze code verkeert in de veronderstelling dat een bestand met de naam
"pc\_rose.txt" beschikbaar is in dezelfde directory als waar het
programma staat. Appendix
<a href="#ch:testtextfiles" data-reference-type="ref" data-reference="ch:testtextfiles">33</a>
legt uit hoe je dit bestand kunt krijgen (als je het nog niet hebt). Als
het bestand niet bestaat, krijg je een runtime error. Hoe je met zulke
fouten om moet gaan wordt in het volgende hoofdstuk uitgelegd.

Wijzig in de code hierboven de bestandsnaam "pc\_rose.txt" in een naam
die niet bestaat. Bestudeer de fout die je krijgt als je het programma
uitvoert.

Als je het bestand "pc\_woodchuck.txt" hebt, wijzig dan de bestandsnaam
in de code hierboven in die naam. Voer het programma uit en bestudeer de
uitvoer.

### Regels lezen met `readline()`

Om een tekstbestand regel voor regel te lezen, kun je de `readline()`
methode gebruiken. Deze methode leest tekens uit het bestand, beginnend
bij de pointer, tot aan en inclusief het volgende "newline" teken. Deze
tekens worden als een string geretourneerd. Als je aan het einde van het
bestand bent en je probeert een nieuwe regel te lezen, krijg je een lege
string terug.

```python
fp = open( "pc_rose.txt" )
while True:
    buffer = fp.readline()
    if buffer == "":
        break
    print( buffer )
fp.close()
```

Als je de code hierboven uitvoert, zul je zien dat er een lege regel
wordt getoond tussen ieder van de regels die uit het bestand gelezen is.
Waar komen die extra regels vandaan? Denk hierover na.

De extra regels zijn er omdat de `readline()` methode een string
retourneert met de tekens die gelezen zijn, inclusief het newline teken.
Dus als de buffer wordt afgedrukt, wordt ook het newline teken
afgedrukt. En omdat de `print()` functie zelf ook naar een nieuwe regel
gaat nadat hij is uitgevoerd, krijg je een lege regel te zien na iedere
tekstregel die wordt afgedrukt.

Schrijf een programma dat regels leest uit "pc\_rose.txt," en alleen die
regels toont die het woord `"naam"` bevatten.

### Regels lezen met `readlines()`

Vergelijkbaar met de `readline()` methode is de `readlines()` methode.
`readlines()` leest alle regels in een tekstbestand, en retourneert ze
als een list van strings. De strings bevatten de newline tekens.

```python
fp = open( "pc_rose.txt" )
buffer = fp.readlines()
for line in buffer:
    print( line, end="" )
fp.close()
```

Als je de code hierboven uitvoert, zie je niet de lege regels tussen de
tekstregels. Dat komt omdat ik aan de aanroep van de `print()` functie
het `end=""` argument heb toegevoegd, zodat `print()` niet zelf naar een
nieuwe regel gaat na het afdrukken.

### Wanneer gebruik je welke lees-methode?

De `read()` en de `readlines()` methodes lezen beide een bestand als
geheel in. Dat is geen probleem voor relatief kleine bestanden, maar
voor grote bestanden kan het gebeuren dat je onvoldoende geheugen
beschikbaar hebt om de inhoud van de bestanden op een efficiënte manier
vast te houden. In dit soort omstandigheden (of als je niet weet hoe
groot een te lezen bestand is) moet je het tekstbestand regel voor regel
lezen middels de `readline()` methode.

Het is vaak een goed idee om, gedurende het ontwikkelen van code, alleen
de eerste paar regels van een tekstbestand te verwerken. Je beperkt dan
de tijd die je programma nodig heeft om het bestand te verwerken, en je
beperkt de hoeveelheid uitvoer die je moet bestuderen, wat debuggen
vergemakkelijkt. Bijvoorbeeld, de code hieronder verwerkt slechts de
eerste 5 regels van een bestand.

```python
fp = open( "pc_jabberwocky.txt" )
teller = 0
while teller < 5:
    buffer = fp.readline()
    if buffer == "":
        break
    print( buffer, end="" )
    teller += 1
fp.close()
```

Als het programma klaar en foutvrij gemaakt is, kan ik de regeltellingen
verwijderen en de loop wijzigen in `while True`, zodat het hele bestand
verwerkt wordt.

Pas de code hierboven aan zodat je telt hoe vaak het woord "wauwelwok"
(ongeacht gebruik van hoofd- of kleine letters) voorkomt in de eerste 5
regels. Druk alleen de telling af. Als het werkt, verwijder dan de
regeltelling zodat je het programma uitvoert voor de tekst als geheel.
