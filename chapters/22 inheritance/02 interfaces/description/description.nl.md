Een interface is een class die specifieke attributen en methodes
vastlegt zonder een implementatie te geven van die methodes. Het idee is
dat je gedwongen bent een subclass af te leiden die de methodes
implementeert. Je kunt dan, zelfs als je nog niet weet welke subclasses
allemaal gemaakt gaan worden, toch al functies bouwen die methodes
aanroepen van de interface class, met als aanname dat deze functies
worden aangeroepen met instanties van subclasses waarvoor de methodes
ingevuld zijn. Om dit goed te begrijpen, kan ik beter een voorbeeld
geven.

Stel dat ik een applicatie wil bouwen die werkt met voertuigen.
Misschien is dit een reisplanner die berekent hoe ik van punt A naar
punt B kan komen. De reisplanner heeft een kaart met daarop alle
mogelijke punten en alle mogelijke verbindingen tussen naburige punten.
Het heeft ook een lijst van voertuigen, waarbij sommige voertuigen
gelimiteerd zijn tot bepaalde punten, en slechts beperkte andere punten
verbinden (bijvoorbeeld, boten reizen alleen tussen havens). De
reisplanner krijgt een start- en een eindpunt, en geeft dan een uitvoer
die iets zegt als: neem de auto en reis van het startpunt naar punt X,
neem dan het vliegtuig om van punt X naar punt Y te reizen, neem dan de
bus om van punt Y naar punt Z te reizen, en loop tenslotte van punt Z
naar het eindpunt.

Deze applicatie heeft een definitie van voertuigen nodig. Om een
optimaal reisplan te maken, moet de applicatie weten welke voertuigen
waar aanwezig zijn, waarheen ze kunnen reizen, en de reissnelheid (zodat
je niet een plan krijgt dat zegt "loop van Amsterdam naar Moskou"). Het
kan ook zinvol zijn om een werkwoord op te nemen dat beschrijft hoe je
reist met een voertuig (bijvoorbeeld "rijd," "vaar," of "vlieg"). Je
moet er goed over nadenken hoe je dergelijke voertuigen wilt
implementeren. Een mogelijke aanpak is ieder voertuig een methode te
geven die een beginpunt als argument krijgt en die retourneert of het
voertuig op dat beginpunt aanwezig is, een methode die een eindpunt
krijgt en die retourneert of dat eindpunt met dat voertuig bereikt kan
worden, een methode die twee punten krijgt en die aangeeft hoeveel tijd
het voertuig nodig heeft om tussen die twee punten te reizen, en een
methode die het corresponderende werkwoord retourneert (ik zeg niet dat
deze implementatie een goed idee is, maar het is er een die gebruikt zou
kunnen worden). Dus je kunt de class `Voertuig` als volgt implementeren:

```python
class Voertuig:
    def __init__( self ):
        self.startpunt = []
        self.eindpunten = []
        self.werkwoord = ""
        self.naam = ""
    def __str__( self ):
        return self.naam
    def isStartpunt( self, p ):
        return NotImplemented
    def isEindpunt( self, p ):
        return NotImplemented
    def snelheid( self, p1, p2 ):
        return NotImplemented
    def reisWerkwoord( self ):
        return NotImplemented
```

Een dergelijke class heet een "interface" of "abstracte class" (in
computertheorie zijn er subtiele verschillen tussen interfaces en
abstracte classes, maar voor Python zijn die niet van belang). Je
gebruikt deze class niet om er instanties van te creëren, wat de reden
is dat alle methodes `NotImplemented` retourneren. In plaats daarvan
gebruik je de class als een superclass waarvan je subclasses afleidt,
waarbij de subclasses min of meer gedwongen zijn om een implementatie
voor iedere van de voorgedefinieerde methodes te geven. Dit betekent
dat, ongeacht het voertuig dat je als subclass creëert, de methodes van
`Voertuig` altijd voor het voertuig zullen bestaan. Functies die iets
doen met voertuigen mogen er dus vanuit gaan dat de betreffende methodes
beschikbaar zijn.
