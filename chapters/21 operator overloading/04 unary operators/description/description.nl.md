Eénwaardige operatoren zijn operatoren die op een enkel object werken,
dus niet in combinatie met een ander object. Een typisch voorbeeld is
het min-teken (`-`) dat je voor een getal kunt zetten om het negatief te
maken. Je kunt sommige eenwaardige operatoren overloaden, evenals een
aantal basale functies die op een enkel object werken.

-   `__neg__()` implementeert de negatie (`-`) van een object

-   `__pos__()` implementeert een plus-teken (`+`) voor een object (dit
    doet meestal niks)

-   `__invert__()` implementeert de bitsgewijze `not` (`\~`)

-   `__abs__()` implementeert de absolute waarde van een object via de
    `abs()` functie

-   `__int__()` implementeert de (naar beneden afgeronde) integer waarde
    van een object middels de `int()` functie; deze moet een integer
    retourneren

-   `__float__()` implementeert de conversie naar een float van een
    object middels de `float()` functie; deze moet een float retourneren

-   `__round__()` implementeert afronding middels de `round()` functie.
    Een optioneel tweede argument kan gegeven worden dat het aantal
    decimalen specificeert; er moet een integer of een float
    geretourneerd worden

-   `__bytes__()` implementeert de representatie van het object als een
    byte string. Hierin is de methode gelijkwaardig met de `__str__()`
    methode die in hoofdstuk
    <a href="#ch:objectorientation" data-reference-type="ref" data-reference="ch:objectorientation">21</a>
    beschreven werd

```python
class Quaternion:
    def __init__( self, a, b, c, d ):
        self.a, self.b, self.c, self.d = a, b, c, d
    def __repr__( self ):
        return "({},{}i,{}j,{}k)".format( self.a, self.b, 
            self.c, self.d )
    def __neg__( self ):
        return Quaternion( -self.a, -self.b, -self.c, -self.d )
    def __abs__( self ):
        return Quaternion( abs( self.a ), abs( self.b ), 
            abs( self.c ), abs( self.d ) )
    def __bytes__( self ):
        return self.__str__().encode( "utf-8" )

c1 = Quaternion( 3, -4, 5, -6 )
print( c1 )
print( -c1 )
print( abs( c1 ) )
print( bytes( c1 ) )
```

{:class="callout callout-info"}
> #### Opmerking
> Het lijkt op het eerste gezicht handig om in de code hierboven ook de
> `__int__(),` `__float__()`, en `__round__()` methodes te implementeren,
> om respectievelijk de functies `int()`, `float()`, en `round()` toe te
> passen op `self.a`, `self.b`, `self.c`, en `self.d`. Helaas werkt dat
> niet, omdat de betreffende functies integers of floats moeten
> retourneren, en niet `Quaternion`en. Ik zie geen zinvolle interpretatie
> van `int()`, `float()`, en `round()` voor de class `Quaternion`, anders
> dan ik suggereerde, dus deze methodes moeten niet geïmplementeerd
> worden.
