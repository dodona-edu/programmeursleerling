Nu ik de basis filosofie van object oriëntatie heb uitgelegd, kan ik
beschrijven hoe object oriëntatie werkt in Python. Het begint met het
creëren van nieuwe klassen middels het gereserveerde woord `class`.

### `class`

Een "class" (ik zal vanaf dit punt meestal het woord "class" gebruiken
in plaats van "klasse," omdat het refereert aan het gereserveerde woord
dat Python gebruikt) kun je beschouwen als een nieuw data type. Wanneer
een class gecreëerd is, kun je instanties van de class toekennen aan
variabelen. Om eenvoudig te beginnen, zal ik een class creëren die een
punt in een 2-dimensionale ruimte beschrijft. Ik noem dit de class
`Punt` (class benaming kent dezelfde eisen als de benaming van
variabelen, en het is de conventie dat de naam van een class begint met
een hoofdletter). Het creëren van de class `Punt` in Python is
ongelofelijk eenvoudig:

```python
class Punt:
    pass
```

Het gereserveerde woord `pass` in de class definitie betekent "doe
niks." Dit gereserveerde woord kun je overal gebruiken waar je een
commando moet plaatsen, maar waar je nog niks hebt om er neer te zetten.
Je mag het niet leeg laten, of alleen een commentaar regel schrijven.
Maar zodra je statements toevoegt, kun je het woord `pass` verwijderen.

Om een object te creëren dat een instantie van de class is, ken ik aan
een variabele de naam van de class toe, met haakjes erachter, alsof het
de aanroep van een functie is (je kunt argumenten tussen de haakjes
zetten, maar dat bediscussieer ik later in dit hoofdstuk).

```python
class Punt:
    pass

p = Punt()
print( type( p ) )
```

Natuurlijk is een punt meer dan alleen een object. Een punt heeft een x
en een y coördinaat. Omdat Python "soft types" gebruikt, kun je waardes
aan attributen toekennen om ze te creëren. Dit doe je in een speciale
initialisatie methode in de class.

![OO](media/OO.png "OO"){:width="70%"}

### `__init__()`

De initialisatie methode van een class heeft de naam `__init__` (twee
"underscores," gevolgd door het woord `init`, gevolgd door nog twee
"underscores"). Zelfs als je de methode `__init__()` niet expliciet voor
een class definieert, bestaat hij toch. Je kunt de `__init__()` methode
gebruiken om alles te initialiseren waarvan je wilt dat het bestaat bij
het instantiëren van de class.

In het geval van `Punt`, moet de `__init__()` methode ervoor zorgen dat
iedere instantie van `Punt` een `x` en een `y` coördinaat heeft. Dit
implementeer je als volgt:

```python
class Punt:
    def __init__( self ):
        self.x = 0.0
        self.y = 0.0

p = Punt()
print( "({}, {})".format( p.x, p.y ) )
```

Bestudeer bovenstaande code goed. Je ziet dat de `__init__()` methode
net zo gedefinieerd is als je een functie zou definiëren, maar binnen de
class definitie.

`__init__()` krijgt één parameter, die `self` genoemd is. Iedere methode
die je definieert krijgt altijd minstens één parameter, die gevuld wordt
met een referentie aan het object waarvoor je de methode aanroept. Het
is de gewoonte dat deze eerste parameter altijd `self` genoemd wordt.
Dat is niet verplicht, maar iedereen doet het zo (zelfs in het
Nederlands). Als je vergeet parameters op te nemen, krijg je een runtime
error. Als je vergeet `self` op te nemen als eerste parameter, maar je
hebt wel andere parameters gespecificeerd, dan zal Python de eerste van
je parameters vullen met een referentie naar het object, en krijg je
daarna waarschijnlijk alsnog een runtime error (omdat je niet had
verwacht dat dat zou gebeuren).

In de `__init__()` methode voor `Punt`, krijgt de instantie van `Punt`
twee attributen, die je kunt beschouwen als variabelen die een deel van
het object zijn. Deze worden `x` en `y` genoemd, en omdat ze een deel
zijn van het object, refereer je aan ze als `self.x` en `self.y`. Ze
krijgen beide de waarde 0.0, wat betekent dat ze floats zijn.

Om aan deze attributen te refereren als het object eenmaal bestaat,
gebruik je de syntax `<object>.<attribuut>`, zoals je kunt zien in de
laatste regel van bovenstaande code, waar het zojuist gecreëerde object
getoond wordt middels een `print()` statement.

Je vraagt je misschien af of je alleen attributen kun creëren in de
`__init__()` methode. Het antwoord is: nee, je kunt attributen ook
creëren in andere methodes, en zelfs buiten de definitie van de class.

```python
class Punt:
    def __init__( self ):
        self.x = 0.0
        self.y = 0.0

p = Punt()
p.z = 0.0
print( "({}, {}, {})".format( p.x, p.y, p.z ) )
```

De meeste Python programmeurs (mijzelf incluis) vinden wat er gebeurt in
de code hierboven bijzonder lelijk. Het is een goed gebruik om alle
attributen die je aan een object wilt toekennen uitsluitend te creëren
in de `__init__()` methode (hoewel je hun waardes elders kunt wijzigen),
zodat je weet dat iedere instantie van de class deze attributen heeft,
en geen instantie méér dan deze heeft.

Als je een versie van een class wilt hebben met extra attributen, kun je
"inheritance" gebruiken om een nieuwe class te creëren op basis van de
bestaande class, die deze extra attributen heeft. Ik beschrijf dat in
een toekomstig hoofdstuk. Vooralsnog moet je ervoor zorg dragen dat
iedere class alle benodigde attributen gedefinieerd krijgt in de
`__init__()` methode.

Net als andere methodes kan de `__init__()` methode argumenten krijgen.
Je kunt die argumenten gebruiken om (sommige van) de attributen een
waarde te geven. Bijvoorbeeld, als ik een instantie van `Punt`
onmiddellijk waardes wil geven voor de `x` en `y` coördinaten, kan ik de
volgende class definitie gebruiken:

```python
class Punt:
    def __init__( self, x, y ):
        self.x = x
        self.y = y

p = Punt( 3.5, 5.0 )
print( "({}, {})".format( p.x, p.y ) )
```

`__init__()` heeft nu drie parameters. De eerste is nog steeds `self`,
aangezien dat altijd de eerste parameter moet zijn. De tweede en derde
heten respectievelijk `x` en `y`. Ik had ze ook anders mogen noemen
(binnen de beperkingen die gelden voor variabele namen), maar ik koos
`x` en `y` als de meest voor-de-hand-liggende benamingen. Ik ken `x` toe
aan `self.x`, en `y` aan `self.y`.

Ik roep nu de instantie van een punt aan met waardes voor de `x` en `y`
coördinaten als argumenten. Het eerste argument komt bij de methode
binnen als de tweede parameter, en het tweede argument als de derde
parameter, aangezien de eerste parameter altijd gebruikt wordt om de
referentie naar het object zelf door te geven.

Als je het meegeven van zulke argumenten optioneel wilt maken, kun je de
parameters default waardes geven middels een assignment in de parameter
specificatie. Dat doe je als volgt:

```python
class Punt:
    def __init__( self, x=0.0, y=0.0 ):
        self.x = x
        self.y = y

p1 = Punt()
print( "({}, {})".format( p1.x, p1.y ) )

p2 = Punt( 3.5, 5.0 )
print( "({}, {})".format( p2.x, p2.y ) )
```

Creëer een list van alle punten met integer coördinaten, waarbij zowel
de `x` als de `y` coördinaat waardes tussen 0 en 3 kunnen aannemen.

### `__repr__()` en `__str__()`

In de code hierboven toon ik de attributen van punten. Maar wat gebeurt
er als ik het punt zelf probeer te printen?

```python
class Punt:
    def __init__( self, x=0.0, y=0.0 ):
        self.x = x
        self.y = y

p = Punt( 3.5, 5.0 )
print( p )
```

Ik neem aan dat je het dan met me eens bent dat het getoonde resultaat
(in feite de plaats in het computergeheugen waar het object zich
bevindt) weinig informatief is. Als ik een punt print, wil ik de
coördinaten zien. Python biedt een voorgedefinieerde methode waarmee ik
dat kan regelen, namelijk de methode `__repr__()`. `__repr__()` moet een
string retourneren, en die string wordt getoond als geprobeerd wordt het
object te tonen.

```python
class Punt:
    def __init__( self, x=0.0, y=0.0 ):
        self.x = x
        self.y = y
    def __repr__( self ):
        return "({}, {})".format( self.x, self.y )

p = Punt( 3.5, 5.0 )
print( p )
```

Dat ziet er een stuk beter uit.

Python kent nog een tweede methode om een string versie van een object
te creëren, namelijk `__str__()`. `__str__()` is hetzelfde als
`__repr__()`, maar wordt alleen gebruikt als het object geprint wordt,
of als argument gebruikt wordt in de `format()` methode. Als `__str__()`
niet gedefinieerd is, wordt `__repr__()` in plaats ervan gebruikt (maar
niet vice versa). Als `__str__()` wel gedefinieerd is, dan kun je ervoor
zorgen dat iets anders gebeurt wanneer het object getoond wordt middels
de `print()` methode, en wanneer het getoond wordt op andere manieren.

Je denkt nu misschien: "welke andere manieren?" De belangrijkste "andere
manier" om objecten te tonen is in de command shell, als je alleen de
naam van de variabele ingeeft die het object bevat.

Het is de gewoonte dat de `__repr__()` methode een string retourneert
die ieder detail van een object bevat, zodat je (indien nodig) aan de
hand van deze string het object opnieuw zou kunnen instantiëren, terwijl
`__str__()` een string retourneert die een netjes geformatteerde, goed
leesbare versie van de meest belangrijke informatie van een object
bevat. In veel gevallen kunnen deze strings hetzelfde zijn.

Veel programmeurs negeren `__repr__()` en definiëren alleen `__str__()`.
Ik denk dat dat verkeerd om is: je zou altijd `__repr__()` moeten
definiëren, terwijl `__str__()` optioneel is. Als je `__repr__()`
gebruikt, zorg er dan voor dat je alle details van een object
retourneert. Als je besluit om sommige details weg te laten, kun je
beter `__str__()` gebruiken.

Breid de class `Punt` uit met een `kleur` attribuut, waarbij `kleur` een
getal is tussen 0 en $2^{24}-1$. Zorg ervoor dat de kleur in de
`__init__()` methode een waarde krijgt, en in de `__repr__()` methode
geretourneerd wordt.
