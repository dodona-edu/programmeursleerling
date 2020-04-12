Een set is een ongeordende collectie van elementen. Je kunt geen
specifieke elementen van een set benaderen via een index of een key. De
enige manier om elementen van een set te benaderen is via een `for`
loop, of door met de `in` operator te testen of een element in de set
bestaat.

Je moet bij sets denken aan wiskundige verzamelingen. In de wiskunde is
een verzameling een collectie van elementen die alle uniek zijn, en
ieder element zit ofwel in de verzameling, ofwel niet in de verzameling.
Er zijn bepaalde operatoren die toestaan verzamelingen te combineren. Ik
gebruik vanaf dit punt het woord "set" in plaats van "verzameling,"
omdat `set` een data type is.

Python gebruikt dictionaries om sets te implementeren; specifiek
implementeert het de elementen van een set als keys van een dictionary.
Dat betekent dat alleen onveranderbare data types in een set kunnen
worden opgeslagen. Sets zelf zijn echter wel veranderbaar.

Omdat Python dictionaries gebruikt om sets te implementeren, denk je
misschien dat je een lege set kunt creëren door `{}` toe te kennen aan
een variabele. Dat creëert echter een lege dictionary, en niet een lege
set. In plaats daarvan creëer je een lege set door de retourwaarde van
de functie `set()` (zonder argumenten) toe te kennen aan een variabele.

Om een set te creëren waarin al een paar elementen zitten, kun je wel
die elementen tussen accolades toekennen aan een variabele. Als
alternatief kun je de `set()` functie aanroepen met een list met de
elementen als argument.

```python
fruitset = { "appel", "banaan", "kers" }
print( fruitset )
```

Als je een set wilt creëren bestaande uit de verschillende letters van
een string, dan kun je `set()` aanroepen met de string als argument
(dubbele letters worden automatisch genegeerd).

```python
helloset = set( "hello world" )
print( helloset )
```

Je kunt een `for` loop gebruiken om een set te doorlopen. De variabele
van de `for` loop krijgt toegang tot alle element van de set. Er is geen
manier om te bepalen in welke volgorde je de elementen te zien krijgt.
Je kunt ze niet sorteren zolang ze in de set zitten. Je kunt echter wel
met een list casting de set omzetten in een list, en die list dan
sorteren.

```python
fruitset = { "appel", "banaan", "kers", "doerian", "mango" }
for element in fruitset:
    print( element )
print()

fruitlist = list( fruitset )
fruitlist.sort()
for element in fruitlist:
    print( element )
```

Met behulp van de `len()` functie kun je het aantal elementen in de set
vaststellen.
