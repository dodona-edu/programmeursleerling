Je kunt een collectie van elementen tot een list maken door de type
casting functie `list()` te gebruiken. De code hieronder maakt van een
tuple een list.

```python
t1 = ( "appel", "banaan", "kers" )
print( t1 )
print( type( t1 ) )
fruitlist = list( t1 )
print( fruitlist )
print( type( fruitlist ) )
```

Dit is soms nodig, specifiek wanneer je een "iterator" hebt en je wilt
de elementen van de iterator als een list gebruiken. Een iterator is een
functie die een collectie van elementen één voor één creëert (meer over
iteratoren volgt in hoofdstuk
24).
Een voorbeeld van een iterator dat ik al genoemd heb is de `range()`
functie. `range()` genereert een collectie getallen. Als je deze
getallen wilt gebruiken in de vorm van een list, moet je list casting
doen.

```python
numlist = range( 1, 11 )
print( numlist )
numlist = list( range( 1, 11 ) )
print( numlist )
```

Je kunt een string ook casten als list. Dan krijg je een list waarin
ieder teken in de string een element is.
