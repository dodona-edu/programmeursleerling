Een "list comprehension" (helaas is er geen geschikte Nederlandse
vertaling voor deze term) is een techniek waarbij je op een compacte
manier lists creëert. Ze zijn typisch voor Python, en je vindt ze zelden
in andere programmeertalen. Je hebt ze niet echt nodig, omdat je via
functies exact hetzelfde effect kunt bereiken. Ze worden echter vaak
gebruikt in voorbeelden (vooral door mensen die willen laten zien hoe
goed ze Python beheersen door met een kort statement een uitgebreid
effect te ressorteren), dus het leek me verstandig om ze toch aan de
orde te stellen. Als je ze nooit gaat gebruiken in je eigen code, is dat
prima want list comprehensions zijn volledig optioneel. Maar je moet ze
kunnen herkennen in andermans code.

Een list comprehension bestaat uit een expressie tussen vierkante haken,
bestaande uit een `for` statement, gevolgd door nul of meer `for` en/of
`if` statements. Het resultaat is een list die de elementen bevat die
het resultaat zijn van de evaluatie van de combinatie van de `for` en
`if` statements. Dit klinkt ingewikkeld (en dat is het eigenlijk ook
wel), maar een voorbeeld zal veel duidelijk maken:

Stel je voor dat ik een list wil creëren die de kwadraten van de
getallen 1 tot en met 25 bevat. Ik kan dat met een functie als volgt
doen:

```python
def kwadraatlist():
    k = []
    for i in range( 1, 26 ):
        k.append( i*i )
    return k

sl = kwadraatlist()
print( sl )
```

In Python kan ik hetzelfde effect bereiken met één regel code, namelijk
als volgt:

```python
sl = [ x*x for x in range( 1, 26 ) ]
print( sl )
```

Ik neem aan dat deze code min of meer voor zichzelf spreekt. Stel je nu
voor dat je deze list wilt creëren, maar dat je om een of andere reden
geen kwadraten wilt opnemen van getallen die op een 5 eindigen. Als ik
dat in bovenstaande functie wil doen, heb ik minstens twee regels code
meer nodig, maar met een list comprehension kan het nog steeds in één en
hetzelfde statement:

```python
sl = [ x*x for x in range( 1, 26 ) if x%10 != 5]
print( sl )
```

De resultaten kunnen behoorlijk complex zijn. Bijvoorbeeld, de volgende
list comprehension creëert een list van tuples van drie integers tussen
1 en 4, waarbij de drie integers alledrie verschillend zijn:

```python
triolist = [ (x,y,z) for x in range( 1, 5 ) 
    for y in range( 1, 5 ) for z in range( 1, 5 ) 
    if x != y if x != z if y != z]
print( triolist )
```

Als je list comprehensions maar lastig vindt, onthoudt dan dat er
absoluut geen reden is om ze te gebruiken behalve om je code compact te
houden, en dat het belangrijker is je code leesbaar en begrijpbaar te
houden.
