Een speciale class is de sequentie. Ik heb al een aantal sequentie
classes geïntroduceerd, namelijk tuples, lists, dictionaries, en sets.
Zulke classes bevatten een serie elementen, die je kunt benaderen
middels een index of een key. Je kunt zelf ook een sequentie class
creëren, door een aantal methodes die informatie over elementen van de
class geven te overloaden.

-   `__len__()` implementeert de `len()` functie, die een integer
    retourneert die aangeeft hoeveel elementen het object bevat.

-   `__getitem__()` implementeert het retourneren van een element met de
    key (of index) die als argument is meegegeven. Deze methode wordt
    aangeroepen als het object benaderd wordt met een waarde tussen
    vierkante haken, bijvoorbeeld `x[key]` met `x` het object en `key`
    de key of index van het gezochte element. Als `key` een index is en
    de index valt buiten het correcte bereik, dan moet de methode een
    `IndexError` genereren (zie hoofdstuk
    <a href="#ch:exceptions" data-reference-type="ref" data-reference="ch:exceptions">18</a>).
    Als `key` iets anders is (bijvoorbeeld een sleutel voor een
    dictionary) en deze refereert niet aan een bestaand element, dan
    moet de methode een `KeyError` genereren. Als `key` een index is,
    dan moeten voor een complete implementatie ook zogenaamde "slice
    objects" ondersteund worden).

-   `__setitem__()` implementeert het toekennen van een waarde aan een
    element van het object dat de key of index heeft die als argument is
    meegegeven, met de toe te kennen waarde als tweede argument. Deze
    methode wordt aangeroepen als een waarde wordt toegekend middels een
    assignment aan het object met een waarde tussen vierkante haken,
    bijvoorbeeld `x[key] = value`.

-   `__delitem__()` implementeert het verwijderen van een element uit
    het object met als key of index het gegeven arument, wanneer het
    gereserveerde woord `del` wordt gebruikt, bijvoorbeeld `del x[key]`.

-   `__missing__()` wordt aangeroepen door `__getitem__()`, met de key
    of index als argument, als deze key of index niet verwijst naar een
    element dat in het object bestaat. Deze methode is vooral bedoeld
    voor subclasses van de Python dictionary.

-   `__contains__()` krijgt een element mee (en dus niet een key of
    index) als argument, en retourneert `True` als het element in het
    object bestaat, en anders `False`. Deze methode wordt aangeroepen
    als het gereserveerde woord `in` gebruikt wordt om te testen of het
    element in het object aanwezig is.

Om te demonstreren hoe deze methodes werken, heb ik een sequentie
geïmplementeerd die een Filippine puzzel beschrijft. Deze puzzel bestaat
uit een serie vragen, die ieder beantwoordt kunnen worden met één woord.
Van ieder antwoord is één letter "speciaal." Als je de speciale letters
achter elkaar zet, krijg je de oplossing van de puzzel.

Ik heb ieder van de puzzelwoorden gedefinieerd als een instantie van de
class `FilippineWoord`, die als attributen heeft het antwoord, de index
van de speciale letter in het antwoord, en de vraag. De class
`Filippine` is de complete puzzel, dat wil zeggen, een sequentie van
`FilippineWoord`en. Ik heb de methodes `__len__()`, `__getitem__()`,
`__setitem__()`, en `__delitem__()` geïmplementeerd (de laatste twee
worden in de code hieronder niet gebruikt).

```python
class FilippineWoord:
    def __init__( self, woord, index, vraag ):
        self.woord = woord
        self.index = index
        self.vraag = vraag

class Filippine:
    def __init__( self, naam, woorden ):
        self.naam, self.woorden = naam, woorden
    def __len__( self ):
        return len( self.woorden )
    def __getitem__( self, n ):
        return self.woorden[n]
    def __setitem__( self, n, waarde ):
        self.woorden[n] = waarde
    def __delitem__( self, n ):
        del self.woorden[n]
    def toon( self ):
        print( self.naam )
        for i in range( len( self ) ):
            print( "{}. {}".format( i+1, self[i].vraag ), 
                end = "  " )
            for j in range( len( self[i].woord ) ):
                if j == self[i].index:
                    print( "* ", end="" )
                else:
                    print( "_ ", end="" )
            print()
    def oplossing( self ):
        s = ""
        for i in range( len( self ) ):
            s += self[i].woord[self[i].index]
        return s
    
puzzel = Filippine( 
    "De Monty Python en de Heilige Graal Filippine",
    [ FilippineWoord( "ANTHRAX", 5, 
          "Sir Galahad bestormde kasteel" ),
      FilippineWoord( "BORS", 2, "Een konijn doodde Sir" ),
      FilippineWoord( "TIM", 0, "De wijze tovenaar heet" ),
      FilippineWoord( "HERBERT", 0, 
          "De erfgenaam van het Moeras Kasteel is prins" ),
      FilippineWoord( "ZWALUW", 4, 
          "Een kokosnoot is te zwaar voor een Europese" ),
      FilippineWoord( "MINSTREELS", 5, 
          "De ridders aten Robins" ) ] )
          
puzzel.toon()
```

Ik heb nog twee methodes geïmplementeerd, die demonstreren hoe de
hierboven genoemde methodes werken. `toon()` toont de puzzel, en
gebruikt als zodanig de `len()` functie en indices om de woorden te
benaderen. `oplossing()` toont de oplossing van de puzzel, en gebruikt
ook `len()` en indices.

Het zou overigens mooier geweest zijn als ik de sterretjes, die de
speciale letters aangeven, onder elkaar had afgedrukt. Het is echter
afhankelijk van de editor die je gebruikt of er een vaste letterbreedte
is, en dus is het lastig om dat voor elkaar te krijgen. Je kunt hier
zelf een oplossing voor implementeren als je wilt (voor dit hoofdstuk is
dat niet van belang).

Er is nog een belangrijke methode die je voor een sequentie class kunt
implementeren, namelijk `__iter__()`. Ik stel een discussie van deze
methode echter uit tot hoofdstuk
<a href="#ch:iteratorsandgenerators" data-reference-type="ref" data-reference="ch:iteratorsandgenerators">24</a>.

Als je een sequentie class bouwt, kun je overwegen om ook de methode
`__add__()` te implementeren, en wellicht ook een goede interpretatie
van de methode `__mul__()`.

Een `Zin` is een list van woorden. Een basale `Zin` class is hieronder
gegeven. Implementeer de `__len__()`, `__getitem__()`, `__setitem__()`,
en `__contains__()` methodes voor deze class.

```python
class Zin:
    def __init__( self, words ):
        self.words = words
    def __repr__( self ):
        return " ".join( self.words )

s = Zin( [ "Er", "is", "slechts", "een", "ding", "ter", 
"wereld", "erger" "dan", "beroddeld", "worden", "en", 
"dat", "is", "niet", "beroddeld", "worden" ] )
print( s )
print( len( s ) )
print( s[7] )
s[7] = "prettiger"
print( "beroddeld" in s )
```
