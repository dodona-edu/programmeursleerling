Voordat ik toekom aan expressies, is er nog een onderwerp dat aan bod
moet komen, en dat is data types. Er zijn drie verschillende data types
die je op dit moment moet kennen, en dat zijn strings, integers, en
floats.

### Strings

Een string is een tekst, die bestaat uit nul of meer tekens, omsloten
door aanhalingstekens. Je mag dubbele of enkele aanhalingstekens
gebruiken. Wat je kiest maakt niet uit, bijvoorbeeld: `"appel"` is
equivalent met `'appel'`. Echter, als je tekst een enkel aanhalingsteken
bevat, moet je hem om problemen te voorkomen omsluiten met dubbele
aanhalingstekens; dus `"mango's"` is een correcte string, terwijl
`'mango's'` niet correct is. Hetzelfde geldt natuurlijk voor een dubbel
aanhalingsteken in een string, die dan omsloten moet worden door enkele
aanhalingstekens.

Maar wat moet je doen als een string zowel dubbele als enkele
aanhalingstekens bevat? Je kunt dat oplossen door in de string een
"backslash" (`\`) op te nemen voor ieder dubbel of enkel aanhalingsteken
dat in de string staat. Dit vertelt Python dat dat aanhalingsteken
behandeld moet worden als een teken in de string, en niet als een
afsluiting van de string. Dus `'mango\'s'` is een correcte string, wat
je kunt zien als je hem probeert te printen:

```python
print( 'mango\'s' )
```

Maar wat moet je dan doen als je een echte backslash wilt opnemen in de
string, en die backslash moet dan ook nog eens staan voor een dubbel of
enkel aanhalingsteken? Dat kun je oplossen door voor de backslash een
extra backslash op te nemen, wat er een teken in de string van maakt in
plaats van een aanduiding dat wat erachter komt letterlijk genomen moet
worden. Bijvoorbeeld, controleer wat de volgende code doet als je hem
uitvoert (je kunt hem intypen in de Python shell):

```python
print( 'mango\\\'s' )
```

Als je dit verwarrend vindt kun je het voorlopig vergeten; ik ga het
hierover in een later hoofdstuk nog uitgebreid hebben. Voor dit moment
is het voldoende om te weten dat een string een tekst is die omsloten is
door dubbele of enkele aanhalingstekens. Een string kan iedere lengte
hebben, inclusief nul tekens lang.

Let erop dat je alleen "rechte" aanhalingstekens gebruikt in Python
programma's, en niet "ronde." Tekstverwerkers hebben de neiging om
rechte aanhalingstekens automatisch te vervangen door ronde, maar Python
herkent zulke ronde aanhalingstekens niet. Tekst editors doen dat niet,
maar als je om wat voor reden dan ook Python code kopieert naar een
tekstverwerker, dan zou het best kunt gebeuren dat je aanhalingstekens
gewijzigd worden. Kijk daarvoor uit.

### Integers

Integers zijn gehele getallen, die positief of negatief (of nul) kunnen
zijn. Er is een zekere grens aan hoe groot integers kunnen worden, die
afhankelijk is van je computer en besturingssysteem. Voor de meeste
toepassingen maakt dit niet uit, en kom je nooit aan die grenzen toe.
Python is niet als rekenmachines met een 10-cijfer display.

Er zijn meerdere manieren mogelijk om een specifieke integer-waarde te
schrijven. `1` is hetzelfde als `+1` (er zijn nog meer manieren om `1`
te schrijven, maar die volgen in een later hoofdstuk). Dus zowel
`print( 1 )` als `print( +1 )` geven hetzelfde resultaat. Voor strings
is dat natuurlijk anders: de string `"1"` is niet hetzelfde als de
string `"+1"`.

Als je integers in Python gebruikt, mag je ze niet schrijven met
scheiders tussen de veelvouden van 1000 om ze leesbaarder te maken. Je
moet het getal 1 miljard dus schrijven als `1000000000` en niet als
`1,000,000,000` (de Engelse conventie) of `1.000.000.000`.

Bestudeer de volgende code en bedenk wat er gebeurt als je hem uitvoert.
Kopieer hem daarna naar de Python shell en voer hem uit.

```python
print( 1,000,000,000 )
```

Als je voorspelling van wat de code doet niet correct is, probeer dan te
bedenken waarom de code deze uitkomst geeft.

### Floats

Floats, wat kort is voor "floating-point getallen" ("gebroken
getallen"), zijn getallen met decimalen. Bijvoorbeeld, `3.14159265` is
een float. Merk op dat je een punt in plaats van een komma moet
gebruiken als decimaal-scheider. Veel landen (inclusief Nederland)
gebruiken een komma als decimaal-scheider, maar Python houdt zich aan de
conventie van Engelstalige landen en gebruikt daarom de punt.

Als je een integer hebt die je wilt gebruiken als float, kun je dat doen
door er `.0` achter te zetten. Bijvoorbeeld, `13` is een integer, maar
`13.0` is een float. Ze geven nog steeds dezelfde waarde weer, en als je
ze in code met elkaar vergelijkt (dat bespreek ik in hoofdstuk
7),
dan zal Python stellen dat ze hetzelfde zijn.

Er zijn bepaalde begrenzingen aan de grootte van de floats, en aan de
precisie. Het is onwaarschijnlijk dat je ooit de maximale groottes
bereikt, aangezien Python wetenschappelijke notatie voor grote getallen
gebruikt. Maar als je Python gebruikt voor zeer exacte berekeningen, kun
je wel in de problemen komen met precisie. Voor de meeste toepassingen
gebeurt dat niet, maar als je een natuurkundige bent wiens berekeningen
grote getallen omvatten op quantumniveau, moet je je wel bewust zijn van
deze beperkingen.

Door de manier waarop Python floats opslaat, kunnen bepaalde getallen
niet precies vastgelegd worden. Bijvoorbeeld, het statement
`print( (431 / 100) * 100 )` geeft als antwoord 430.99999999999994, en
niet 431 zoals je zou verwachten. Als je weet dat de uitkomst van een
berekening waarin floats zitten een integer moet zijn, dan doe je er
goed aan om de uitkomst af te ronden naar het dichtstbijzijnde gehele
getal. Dat kun je doen met behulp van de `round()` functie, die ik
bespreek in hoofdstuk
6.
