In hoofdstuk
21
beschreef ik dat objecten een alias van elkaar kunnen zijn, maar dat je
ook echte kopieën van objecten kunt maken. Wat gebeurt er als ik probeer
objecten met elkaar te vergelijken?

```python
class Punt:
    def __init__( self, x=0.0, y=0.0 ):
        self.x = x
        self.y = y
    def __repr__( self ):
        return "({}, {})".format( self.x, self.y )

p1 = Punt( 3, 4 )
p2 = Punt( 3, 4 )
p3 = p1
print( p1 is p2 )
print( p1 is p3 )
print( p1 == p2 )
print( p1 == p3 )
```

Het gereserveerde woord `is` wordt gebruikt om identiteiten met elkaar
te vergelijken. Omdat `p3` een alias is van `p1`, retourneert `p1 is p3`
`True`, terwijl `p1 is p2` `False` retourneert.

Het `==`-teken zou een waarde-vergelijking moeten doen. Omdat `p1` en
`p2` refereren aan hetzelfde punt in de 2-dimensionale ruimte, zou het
fijn zijn als `p1 == p2` `True` zou retourneren (want dat is wat je zou
verwachten van een waarde-vergelijking). Maar dat gebeurt niet. Vreemd
is dat niet, aangezien Python niet kan weten hoe je de waarde van
`Punt`en moet vergelijken (althans niet zonder verdere specificatie).
Daarom doet `==` de enige vergelijking die Python standaard kent,
namelijk de vergelijking van identiteiten, dus dezelfde vergelijking als
`is` doet. Je kunt Python echter vertellen hoe de waarde van twee punten
vergeleken kan worden via de speciale methode `__eq__()`:

```python
class Punt:
    def __init__( self, x=0.0, y=0.0 ):
        self.x = x
        self.y = y
    def __repr__( self ):
        return "({}, {})".format( self.x, self.y )
    def __eq__( self, p ):
        return self.x == p.x and self.y == p.y

p1 = Punt( 3, 4 )
p2 = Punt( 3, 4 )
p3 = p1
print( p1 is p2 )
print( p1 is p3 )
print( p1 == p2 )
print( p1 == p3 )
```

De `__eq__()` methode vertelt Python in dit geval wat gedaan moet worden
als twee objecten van het type `Punt` met elkaar vergeleken worden
middels `==`. Het retourneert `True` als de `x` en `y` coördinaten
gelijk zijn, en anders `False`. In dit voorbeeld heeft er "operator
overloading" plaatsgevonden voor de vergelijkingsoperator `==` door de
`__eq__()` methode in te vullen.

Je kunt ook de andere vergelijkingsoperatoren "overloaden," dus de
`\`=!, `>`, `>=`, `<`, en `<=`:

-   `__eq__()` voor gelijkheid (`==`)

-   `__ne__()` voor ongelijkheid (`\`=!)

-   `__gt__()` voor groter dan (`>`)

-   `__ge__()` voor groter dan of gelijk aan (`>=`)

-   `__lt__()` voor kleiner dan (`<`)

-   `__le__()` voor kleiner dan of gelijk aan (`<=`).

Als je `__eq__()` invult maar `__ne__()` niet, dan retourneert
`__ne__()` automatisch het omgekeerde van wat `__eq__()` retourneert.
Geen van de andere methodes heeft een dergelijke automatische
interpretatie.

Je bent niet beperkt tot het vergelijken van objecten van dezelfde
class. Bijvoorbeeld, ik kan een class `Quaternion` maken die een
quaternion implementeert, die ik zou willen vergelijken met een integer
of een float. Dat kan:

```python
class Quaternion:
    def __init__( self, a, b, c, d ):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
    def __repr__( self ):
        return "({},{}i,{}j,{}k)".format( self.a, self.b,
            self.c, self.d )
    def __eq__( self, n ):
        if isinstance( n, int ) or isinstance( n, float ):
            if self.a == n and self.b == 0 and \
                self.c == 0 and self.d == 0:
                return True
            else:
                return False
        elif isinstance( n, Quaternion ):
            if self.a == n.a and self.b == n.b and \
                self.c == n.c and self.d == n.d:
                return True
            else:
                return False
        return NotImplemented

c1 = Quaternion( 1, 2, 3, 4 )
c2 = Quaternion( 1, 2, 3, 4 )
c3 = Quaternion( 3, 0, 0, 0 )
if c1 == c2:
    print( c1, "==", c2 )
else:
    print( c1, "!=", c2 )
if c1 == c3:
    print( c1, "==", c3 )
else:
    print( c1, "!=", c3 )
if c3 == 1:
    print( c3, "==", 1 )
else:
    print( c3, "!=", 1 )
if c3 == 3:
    print( c3, "==", 3 )
else:
    print( c3, "!=", 3 )
if c3 == 3.0:
    print( c3, "==", 3.0 )
else:
    print( c3, "!=", 3.0 )
if c3 == "3":
    print( c3, "== \"3\"" )
else:
    print( c3, "!= \"3\"" )
if 3 == c3:
    print( 3, "==", c3 )
else:
    print( 3, "!=", c3 )
```

De implementatie van de `__eq__()` methode in de code hierboven test
eerst of een vergelijking gemaakt wordt met een `Quaternion`, een
integer, of een float. Als het één van deze data types is, dan wordt de
vergelijking uitgevoerd, en het resultaat geretourneerd als `True` of
`False`. Als het geen van de data types is, wordt `NotImplemented`
geretourneerd. `NotImplemented` is een speciale waarde die aangeeft dat
de vergelijking geen zinvolle uitkomst geeft. Hoewel de `__ne__()`
methode het resultaat van de `__eq__()` methode inverteert, kan hij niet
`NotImplemented` inverteren.

In de code hierboven zou je iets moeten opvallen aan de laatste
vergelijking. De vergelijking `3 == c3` wordt uitgevoerd. Gewoonlijk
wordt de vergelijkingsoperator uitgevoerd voor de linker-operand, wat in
dit geval wil zeggen dat de vergelijking die gedefinieerd is voor de
integer 3 wordt uitgevoerd, met `c3` als argument. Maar voor integers
houdt de `__eq__()` methode geen rekening met `Quaternion`en (de makers
van Python, die verantwoordelijk zijn voor de integer class, kunnen
immers niet weten dat ik een `Quaternion` class zal bouwen), en dus zal
de vergelijking `NotImplemented` retourneren. Als dat echter gebeurt,
inverteert Python de operanden, zodat in dit geval de vergelijking
`c3 == 3` wordt uitgevoerd. Dit leidt dan wel tot een resultaat,
aangezien voor een `Quaternion` de vergelijking met een integer
gedefinieerd is. Hetzelfde zal gebeuren voor de `\`=! operator. En iets
vergelijkbaars gebeurt voor de andere vergelijkingsoperatoren, maar als
daar de operanden worden verwisseld, wordt ook een `<` omgewisseld met
een `>`, en een `<=` met een `>=`, zoals je zou verwachten.

In hoofdstuk
21
werd een class `Rechthoek` gedefinieerd. Voeg aan deze class operatoren
toe die de gelijkheid van rechthoeken testen (twee rechthoeken zijn
gelijk als ze exact dezelfde vorm hebben, zelfs als ze niet dezelfde
plek in de ruimte innemen), en voeg ook operatoren toe die testen of een
rechthoek kleiner of groter dan een andere rechthoek is (op basis van de
oppervlaktes). Test de nieuwe operatoren. Ik wil hierbij opmerken dat ik
een beetje twijfel of dit wel acceptabele definities zijn voor
vergelijkingen van rechthoeken, maar als oefening kan het ermee door.

Er is nog een speciaal soort vergelijking die ik wil bespreken, en dat
is het testen of een object `True` of `False` is. Veel objecten worden
als `False` beschouwd in speciale omstandigheden; bijvoorbeeld, een lege
list wordt als `False` geëvalueerd. Ik heb dit kort besproken in
hoofdstuk
7.

```python
buffer = []
if buffer:
    print( buffer )
else:
    print( "buffer is empty" )
```

Je kunt je eigen evaluatie van een object definiëren die gebruikt wordt
als het object optreedt als conditie. Dit gaat via de `__bool__()`
methode.

`__bool__()` wordt aangeroepen als een object als conditie behandeld
wordt. Hij retourneert `True` of `False`. Als `__bool__()` niet
geïmplementeerd is, wordt in plaats ervan `__len__()` aangeroepen (die
bespreek ik hieronder), en zal er `False` geretourneerd worden als
`__len__()` nul retourneert. Als noch `__bool__()` noch `__len__()`
geïmplementeerd is, zal het object altijd als `True` beschouwd worden in
een conditie.
