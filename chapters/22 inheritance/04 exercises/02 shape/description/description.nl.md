Een `Rechthoek` en een `Vierkant` zijn
vormen. Er zijn, uiteraard, meerdere vormen die op verschillende
manieren gedefinieerd zijn, maar die met rechthoeken en vierkanten
gemeen hebben dat ze een oppervlakte en een omtrek hebben. Definieer een
interface class `Vorm`, waarvan `Rechthoek` en `Vierkant`
sub(sub)classes zijn. Definieer ook een class `Cirkel` die je afleidt
van `Vorm`.

### Opgave

Hieronder geef ik de interface class `Vorm` uit de vorige opgave,
samen met de classes `Rechthoek` en `Vierkant` die erop voortbouwen (je
oplossing wordt op zichzelf beoordeeld, en kan dus niets importeren uit
een andere opgave). `Vorm` legt het gemeenschappelijke interface vast
dat elke vorm moet ondersteunen: een methode `oppervlakte` en een
methode `omtrek`. `Vorm` zelf weet niet hoe ze die moet berekenen,
dus geven beide gewoon `NotImplemented` terug.

```python
class Vorm:
    def oppervlakte( self ):
        return NotImplemented
    def omtrek( self ):
        return NotImplemented

class Rechthoek(Vorm):
    def __init__( self, x, y, b, h ):
        self.x = x
        self.y = y
        self.b = b
        self.h = h
    def __repr__( self ):
        return "[({},{}),b={},h={}]".format( self.x, self.y, 
            self.b, self.h )
    def oppervlakte( self ):
        return self.b * self.h
    def omtrek( self ):
        return 2*(self.b + self.h)

class Vierkant(Rechthoek):
    def __init__( self, x, y, zijde ):
        Rechthoek.__init__( self, x, y, zijde, zijde )
```

Creëer nu ook een class `Cirkel` die rechtstreeks erft van `Vorm` (niet
van `Rechthoek` of `Vierkant`). Een cirkel wordt aangemaakt met de `x`-
en `y`-coördinaat van haar middelpunt, en een straal `straal`. Als een
cirkel doorgegeven wordt aan de ingebouwde functies `repr` of `str`,
dan moet de string `"[({},{}),straal={}]".format(x, y, straal)`
teruggegeven worden. Haar methode `oppervlakte` moet $$\pi \cdot
straal^2$$ teruggeven en haar methode `omtrek` moet $$2\pi \cdot
straal$$ teruggeven (gebruik `math.pi`).

### Voorbeeld

```console?lang=python&prompt=>>>
>>> vorm = Vorm()
>>> vorm.oppervlakte()
NotImplemented
>>> vorm.omtrek()
NotImplemented

>>> r = Rechthoek(1, 1, 8, 5)
>>> r
[(1,1),b=8,h=5]
>>> r.oppervlakte()
40
>>> r.omtrek()
26
>>> isinstance(r, Vorm)
True

>>> v = Vierkant(2, 3, 4)
>>> v
[(2,3),b=4,h=4]
>>> v.oppervlakte()
16
>>> v.omtrek()
16
>>> isinstance(v, Rechthoek)
True
>>> isinstance(v, Vorm)
True

>>> c = Cirkel(0, 0, 3)
>>> c
[(0,0),straal=3]
>>> c.oppervlakte()
28.274333882308138
>>> c.omtrek()
18.84955592153876
>>> isinstance(c, Vorm)
True
>>> isinstance(c, Rechthoek)
False
```
