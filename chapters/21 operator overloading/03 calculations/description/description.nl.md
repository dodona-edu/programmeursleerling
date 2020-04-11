Er zijn methodes beschikbaar die definiëren wat er gebeurt als je een
instantie van een class combineert met een waarde via een reguliere
berekeningsoperator. De meest belangrijke zijn:

-   `__add__()` voor optellen (`+`)

-   `__sub__()` voor aftrekken (`-`)

-   `__mul__()` voor vermenigvuldigen (`*`)

-   `__truediv__()` voor delen (`/`)

-   `__floordiv__()` voor integer delen (`//`)

-   `__mod__()` voor modulo (`\%`)

-   `__pow__()` voor machtsverheffen (`**`)

-   `__lshift__()` voor shift-links (`<<`)

-   `__rshift__()` voor shift-rechts (`>>`)

-   `__and__()` voor bitsgewijze `and` (`\&`)

-   `__or__()` voor bitsgewijze `or` (`|`)

-   `__xor__()` voor bitsgewijze `xor` (`\^`)

Bijvoorbeeld, voor quaternionen is de optelling gedefinieerd als:
$(A + Bi + Cj + Dk) + (E + Fi + Gj + Hk) = (A+E) + (B+F)i + (C+G)j + (D+H)k$.
Je kunt natuurlijk ook integers en floats optellen bij quaternionen. Dit
kan als volgt geïmplementeerd worden:

```python
class Quaternion:
    def __init__( self, a, b, c, d ):
        self.a, self.b, self.c, self.d = a, b, c, d
    def __repr__( self ):
        return "({},{}i,{}j,{}k)".format( self.a, self.b, 
            self.c, self.d )
    def __add__( self, n ):
        if isinstance( n, int ) or isinstance( n, float ):
            return Quaternion( n+self.a, self.b, self.c, self.d )
        elif isinstance( n, Quaternion ):
            return Quaternion( n.a + self.a, n.b + self.b, \
                n.c + self.c, n.d + self.d )
        return NotImplemented

c1 = Quaternion( 3, 4, 5, 6 )
c2 = Quaternion( 1, 2, 3, 4 )
print( c1 + c2 )
print( c1 + 10 )
```

Als een berekeningsoperator gebruikt wordt met je nieuwe class als de
rechteroperand, en de linkeroperand ondersteunt deze operator niet (dat
wil zeggen: de linkeroperand retourneert `NotImplemented`), dan
controleert Python of je nieuwe class de operatie ondersteunt als
rechteroperand. Je moet dat mogelijk maken via extra methodes, die
dezelfde namen hebben als de bovengenoemde operatoren, maar met een `r`
voor de naam, bijvoorbeeld, `__radd__()` is de optelling met het object
als rechteroperand (alle andere methodes kun je op dezelfde manier
creëren).

De code hierboven zal een runtime error geven als je probeert `10 + c1`
uit te rekenen (probeer het maar). Je moet de `__radd__()` methode
implementeren om dat op te lossen.

```python
class Quaternion:
    def __init__( self, a, b, c, d ):
        self.a, self.b, self.c, self.d = a, b, c, d
    def __repr__( self ):
        return "({},{}i,{}j,{}k)".format( self.a, self.b, 
            self.c, self.d )
    def __add__( self, n ):
        if isinstance( n, int ) or isinstance( n, float ):
            return Quaternion( n+self.a, self.b, self.c, self.d )
        elif isinstance( n, Quaternion ):
            return Quaternion( n.a + self.a, n.b + self.b, \
                 n.c + self.c, n.d + self.d )
        return NotImplemented
    def __radd__( self, n ):
        return self.__add__( n )

c1 = Quaternion( 3, 4, 5, 6 )
print( 10 + c1 )
```

Je ziet dat ik het probleem heb opgelost door `__radd__()` te
implementeren als een directe aanroep van `__add__()`. Je vraagt je
misschien af waarom Python dat niet automatisch doet. De reden is van
wiskundige aard: het komt inderdaad vaak voor dat `+` "commutatief" is,
wat wil zeggen dat je de operanden mag omwisselen zonder dat dat het
eindresultaat beïnvloedt, maar dat is zeker niet altijd het geval. Maar
als voor je nieuwe class de optelling commutatief is, dan kun je
`__radd__()` implementeren door eenvoudigweg `__add__()` aan te roepen.

Voor de verkorte operatoren `+=`, `-=`, `*=`, etcetera, kun je ook
aparte methodes definiëren. Deze hebben dezelfde namen als de methodes
hierboven, maar met een `i` voor de naam, bijvoorbeeld, `__iadd__()`
implementeert de `+=` operator (wederom kun je op dezelfde manier de
namen voor de andere methodes creëren). Deze methodes moeten `self`
wijzigen, en ook het resultaat (meestal `self`) retourneren. Als ze niet
geïmplementeerd zijn, valt Python terug op de reguliere interpretatie,
dat wil zeggen, als een statement `x += y` wordt gegeven, probeert
Python `x.__iadd__(y)` uit te voeren, en als dat `NotImplemented` geeft,
zal het `x = x.__add__(y)` uitvoeren. Daarom hoef je meestal niet de
methodes voor de verkorte operatoren te implementeren.

Breid de `Quaternion` class uit met aftrekking. Aftrekken werkt
equivalent met optellen, maar alle plussen worden vervangen door minnen.
Merk op dat aftrekken niet commutatief is, dus je kunt `__rsub__()` niet
als een simpele aanroep van `__sub__()` implementeren. Het is echter
niet bepaald moeilijk om `__rsub__()` te implementeren, dus doe dat ook.
