Een list is een verzameling (of "collectie") elementen.

De elementen van een list zijn *geordend*. Omdat ze geordend zijn, kun
je ieder element van een list benaderen via een index, net zoals je de
tekens in een string kunt benaderen. De indices beginnen bij nul, net
als bij strings.

![list](media/List.png "list"){:width="70%"}

In Python kun je lists herkennen aan het feit dat de elementen van een
list tussen vierkante haken (`[]`) staan. Je kunt het aantal elementen
in een list achterhalen door middel van de `len()` functie. Via een
`for` loop kun je de elementen van de list doorlopen. Je mag data types
in een list mixen. Je kunt de functies `max()`, `min()` en `sum()`
gebruiken op een list. Je kunt testen of een element voorkomt in een
list via de `in` operator (of het niet voorkomen van een element via de
`not in` operator).

```python
fruitlist = ["appel", "banaan", "kers", 27, 3.14]
print( len( fruitlist ) )
for element in fruitlist:
    print( element )
print( fruitlist[2] )

numlist = [314, 315, 642, 246, 129, 999]
print( max( numlist ) )
print( min( numlist ) )
print( sum( numlist ) )
print( 100 in numlist )
print( 999 in numlist )
```

Schrijf een `while` loop die elementen van een list afdrukt.

Afgezien van de vierkante haken, lijken lists veel op tuples. Maar er is
een groot verschil...
