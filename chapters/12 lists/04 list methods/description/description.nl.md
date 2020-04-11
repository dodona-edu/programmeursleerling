Python heeft een groot aantal methodes die lists wijzigen of informatie
uit lists halen. Je hoeft geen module te importeren om ze te gebruiken.
Omdat het methodes betreft, gebruik je de syntax
`<``list``>.<methode>()`.

{:class="callout callout-warning"}
> #### Belangrijk
> Lists zijn veranderbaar en deze methodes veranderen vaak
> de list waarop ze werken! Dit is niet wat je gewend bent met string
> methodes, waarbij de methodes een nieuwe string maken en die
> retourneren, zonder de originele string aan te passen. De meeste list
> methodes hebben daarentegen een onomkeerbaar effect op de list waarop ze
> werken. Meestal hebben ze ook geen retourwaarde, en die heb je ook niet
> nodig, omdat het doel van de methodes is de list te wijzigen.

### `append()`

`append()` plakt een nieuw element aan het einde van een list. Je roept
de methode aan met het nieuwe element als argument.

```python
fruitlist = ["appel", "banaan", "kers", "doerian"]
print( fruitlist )
fruitlist.append( "mango" )
print( fruitlist )
```

Zoals hierboven is beschreven, kun je in plaats van de `append()`
methode een element aan een list toevoegen via de $+$ operator, en het
resultaat weer toekennen aan de variabele die de list bevat. De
`append()` methode is echter leesbaarder. `<``list``>.append(<element>)`
is equivalent met `<``list``>[len(<``list``>):] = [<element>]`, of
`<``list``> += [<element>]`.

### `extend()`

`extend()` maakt een list langer door alle elementen van een tweede list
aan het einde te van de eerste list toe te voegen. Je roept de methode
aan met de list met de nieuwe elementen als argument.

```python
fruitlist = ["appel", "banaan", "kers", "doerian"]
print( fruitlist )
fruitlist.extend( ["framboos", "aardbei", "aalbes"] )
print( fruitlist )
```

Net als bij de `append()` methode kun je in plaats van de `extend()`
methode de $+$ operator gebruiken en het resultaat toekennen aan de
originele list. En net als bij de `append()` methode, is het gebruik van
de `extend()` methode te prefereren vanwege de leesbaarheid.
`<``list``>.extend(<addlist>)` is equivalent met
`<``list``>[len(<``list``>):] = <addlist>`.

### `insert()`

`insert()` geeft de mogelijkheid een element aan een list toe te voegen
op een specifieke positie. Je roept de methode aan met twee argumenten,
waarvan de eerste de index is van de positie waar het nieuwe element
moet komen, en de tweede het nieuwe element zelf. Als je een element toe
wilt voegen aan het begin van de list, kun je index 0 gebruiken.

```python
fruitlist = ["appel", "banaan", "kers", "doerian"]
print( fruitlist )
fruitlist.insert( 2, "mango" )
print( fruitlist )
```

`<``list``>.insert(<i>,<element>)` is equivalent met
`<``list``>[<i>:<i>] = [<element>]`.

### `remove()`

`remove()` laat je een element van de list verwijderen. Het element dat
je wilt verwijderen geef je mee als argument. Als dit element meerdere
keren voorkomt in de list, wordt de eerste instantie (die met de laagste
index) verwijderd. Als je een element probeert te verwijderen dat niet
voorkomt op de list, geeft dat een runtime error.

```python
fruitlist = ["appel", "banaan", "kers", "doerian"]
print( fruitlist )
fruitlist.remove( "banaan" )
print( fruitlist )
```

### `pop()`

Net als `remove()`, verwijdert `pop()` een element van de list, maar
doet dat via een index. Er is één numeriek argument, dat optioneel is,
dat de index is van het te verwijderen element. Als geen argument wordt
meegegeven, wordt het laatste element van de list verwijdered. Als een
index wordt meegegeven die buiten de list valt, volgt een runtime error.

Een groot verschil tussen `remove()` en `pop()` is dat `pop()` een
retourwaarde heeft, namelijk het element dat verwijderd is. Dit zorgt
ervoor dat je via `pop()` snel alle elementen van een list kunt
verwerken terwijl je de list leegmaakt.

```python
fruitlist = ["appel", "banaan", "kers", "doerian"]
print( fruitlist )
print( fruitlist.pop() )
print( fruitlist )
print( fruitlist.pop( 0 ) )
print( fruitlist )
```

### `del`

`del` is noch een methode noch een functie, maar omdat het vaak in één
adem genoemd wordt met `remove()` en `pop()`, zet ik het hier neer.
`del` is een gereserveerd woord dat een list element verwijderd, of
zelfs een sub-list, via de index. Het lijkt op wat `pop()` doet, maar
heeft geen retourwaarde. `pop()` kan ook niet gebruikt worden op
sub-lists. `del` gebruik je via de syntax `del <``list``>[<index>]` of
`del <``list``>[<index1>:<index2>]`.

```python
fruitlist = ["appel", "banaan", "kers", "banaan", "doerian"]
del fruitlist[3]
print( fruitlist )
```

### `index()`

`index()` retourneert de index van de eerste instantie in een list van
het element dat als argument aan de methode is meegegeven. Een runtime
error volgt als het element niet voorkomt op de list.

```python
fruitlist = ["appel", "banaan", "kers", "banaan", "doerian"]
print( fruitlist.index( "banaan" ) )
```

### `count()`

`count()` retourneert een integer die aangeeft hoe vaak het element dat
als argument is meegegeven voorkomt in de list.

```python
fruitlist = ["appel", "banaan", "kers", "banaan", "doerian"]
print( fruitlist.count( "banaan" ) )
```

### `sort()`

`sort()` sorteert de elementen van de list, van laag naar hoog. Als de
elementen strings zijn, betreft het een alfabetische sortering. Als de
elementen getallen zijn, betreft het een numerieke sortering. Als de
elementen gemixt zijn, volgt een runtime error, tenzij bepaalde extra
argumenten zijn meegegeven.

```python
fruitlist = ["appel", "aardbei", "banaan", "framboos", 
    "kers", "banaan", "doerian", "mango"]
fruitlist.sort()
print( fruitlist )

numlist = [314, 315, 642, 246, 129, 999]
numlist.sort()
print( numlist )
```

Om van hoog naar laag te sorteren, kun je een argument
`reverse=<boolean>` meegeven.

```python
fruitlist = ["appel", "aardbei", "banaan", "framboos", "kers", "banaan", "doerian", "aalbes"]
fruitlist.sort( reverse=True )
print( fruitlist )
```

Een ander argument dat je `sort()` kunt meegeven is een "key" (Engels
voor sleutel). Je geeft dit argument mee volgens de syntax
`<``list``>.sort( key=<key> )`, waarbij `<key>` een functie is die één
element meekrijgt (namelijk het element dat gesorteerd moet worden) en
die een waarde retourneert die als sorteringssleutel gebruikt moet
worden. Een typische toepassing van het key argument is als je een list
van strings wilt sorteren, waarbij je de strings "case-insensitive" (dat
wil zeggen zonder verschil te maken tussen hoofd- en kleine letters)
wilt sorteren. Dus als key wil je de waarde van het element volledig als
kleine letters gebruiken. Dat kun je doen door als key functie
`str.lower()` mee te geven. Je roept dan de `sort()` methode aan als in
het volgende voorbeeld:

```python
fruitlist = ["appel", "Aardbei", "banaan", "framboos", "KERS", "banaana", "doerian", "mango"]
fruitlist.sort() 
print( fruitlist )
fruitlist.sort( key=str.lower ) # case-insensitive sort
print( fruitlist )
```

Merk op dat je bij het key argument geen haakjes achter de functie naam
zet. Dit is namelijk geen functie-aanroep, het is een argument dat
Python vertelt welke functie gebruikt moet worden om de
sorteringssleutel te genereren. Je kunt ook je eigen functies gebruiken
als key. Bijvoorbeeld, in de volgende code wordt `numlist` gesorteerd
met de cijfers van de drie-cijferige getallen in omgekeerde volgorde:

```python
def keercijfersom( item ):
    return (item%10)*100 + (int(item/10)%10)*10 + int(item/100)

numlist = [314, 315, 642, 246, 129, 999]
numlist.sort( key=keercijfersom )
print( numlist )
```

Hier is een ander voorbeeld, waarbij een list van strings gesorteerd
wordt op string lengte als eerste (korte strings vóór lange strings), en
alleen bij gelijke lengte op alfabetische volgorde:

```python
def len_alfabetisch( element ):
    return len( element ), element 

fruitlist = ["appel", "aardbei", "banaan", "framboos", 
    "kers", "banaan", "doerian", "mango"]
fruitlist.sort( key=len_alfabetisch )
print( fruitlist )
```

Merk op dat de `len\_alfabetisch()` functie een tuple retourneert. Zoals
in hoofdstuk
<a href="#ch:tuples" data-reference-type="ref" data-reference="ch:tuples">12</a>
werd uitgelegd, als je twee tuples vergelijkt worden eerst de eerste
elementen van de tuples vergeleken, en alleen als die gelijk zijn worden
de tweede elementen vergeleken.

Op dit punt kan ik een typisch voorbeeld geven van het gebruik van een
"anonieme functie," die ik introduceerde in hoofdstuk
<a href="#ch:functions" data-reference-type="ref" data-reference="ch:functions">9</a>
(als je die niet hebt overgeslagen). Als je een anonieme functie
gebruikt om de key voor een `sort()` methode te specificeren, in plaats
van als een separate functie elders in het programma, houd je de code
compact en leesbaar.

```python
fruitlist = ["appel", "aardbei", "banaan", "framboos", "kers", "banaan", "doerian", "mango"]
fruitlist.sort( key=lambda x: (len(x),x) )
print( fruitlist )
```

### `reverse()`

`reverse()` zet de elementen van de list in omgekeerde volgorde.

```python
fruitlist = ["appel", "aardbei", "banaan", "framboos", "kers", "banaan", "doerian", "aalbes"]
fruitlist.reverse()
print( fruitlist )
```

### Oefening

Schrijf een programma dat de gebruiker vraagt wat data in te geven,
bijvoorbeeld de namen van zijn of haar vrienden. De gebruiker geeft aan
te stoppen met data ingeven als alleen `Enter` wordt ingedrukt. Het
programma toont dan alle ingegeven data items, alfabetisch gesorteerd.
Print ieder item apart, op een eigen regel.

Sorteer een list van nummers op absolute waarde. Hint: Gebruik de
`abs()` functie als key.

Tel hoe vaak iedere letter (case-insensitive) voorkomt in een string. Je
mag alle tekens negeren die geen letter zijn. Je zou dit natuurlijk
kunnen doen met 26 variabelen, maar het is veel beter om een list te
gebruiken. Zet alle 26 elementen van de list bij de start op 0. Wanneer
de letters geteld zijn, druk je alle resulterende tellingen af. Als
index voor de list kun je `ord(letter) - ord("a")` gebruiken, waarbij
"letter" een kleine letter is (de functie `ord()` is uitgelegd in
hoofdstuk
<a href="#ch:strings" data-reference-type="ref" data-reference="ch:strings">11</a>).
