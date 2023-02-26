In hoofstuk
21
gaf ik een voorbeeld van een class `Appel` en een class `Peer`, die
beide "afgeleid" waren van een class `Fruit`. Ik gaf ook een voorbeeld
van een class `Student` en een class `Docent` die beide zijn afgeleid
van een class `Persoon`. Je implementeert een dergelijk "hiërarchie" van
classes via "overerving."

Overerving is erg eenvoudig. Bij de definitie van een nieuwe class, zet
je tussen haakjes de naam van een andere class. De nieuwe class erft dan
alle attributen en methodes van de andere class, wat wil zeggen dat ze
automatisch zijn opgenomen in de nieuwe class.

```python
class Persoon:
    def __init__( self, voornaam, achternaam, leeftijd ):
        self.voornaam = voornaam
        self.achternaam = achternaam
        self.leeftijd = leeftijd
    def __repr__( self ):
        return "{} {}".format( self.voornaam, self.achternaam )
    def minderjarig( self ):
        return self.leeftijd < 18

class Student( Persoon ):
    pass

albert = Student( "Albert", "Applebaum", 19 )
print( albert )
print( albert.minderjarig() )
```

Zoals je kunt zien, heeft de class `Student` alle attributen en methodes
van de class `Persoon` geërfd. De nieuwe class (in dit geval `Student`)
wordt de "subclass" genoemd, en de class waarvan de subclass wordt
afgeleid (in dit geval `Persoon`) heet de "superclass" (soms
"ouder-class" genoemd).

### Uitbreiden en overschrijven

![overerving](media/Inheritance.png "overerving"){:width="50%"}

Als je een subclass wilt uitbreiden met nieuwe methodes, dan kun je
gewoon die nieuwe methodes definiëren in de subclass. Als je op deze
manier methodes definieert die al bestaan in de superclass, dan
"overschrijven" ze de methodes van de superclass, wat wil zeggen dat bij
een aanroep van de betreffende methode voor de subclass, de methode van
de subclass gebruikt wordt, en niet die van de superclass.

Vaak gebeurt het dat als je een methode overschrijft, je nog steeds de
methode van de superclass wilt kunnen gebruiken. Bijvoorbeeld, als de
class `Student` een list bevat van de cursussen waarvoor de student is
ingeschreven, dan wordt die list geïnitialiseerd in de `__init__()`
methode. Dus moet ik de `__init__()` methode van `Persoon`
overschrijven, waardoor de naam en leeftijd van de student niet langer
geïnitialiseerd worden, tenzij ik ervoor zorg dat dat wel gebeurt. Ik
zou bijvoorbeeld een kopie kunnen maken van de `__init__()` methode van
`Persoon` en die kopie aanpassen voor `Student`, maar het is beter om de
`__init__()` methode van `Persoon` aan te roepen vanuit de `__init__()`
methode van `Student`. Op die manier zorg ik ervoor dat, mocht de
`__init__()` methode van `Persoon` gewijzigd worden, ik de `__init__()`
methode van `Student` niet hoef aan te passen.

Er zijn twee manieren om de methode van een andere class aan te roepen:
middels een "class call" of middels de `super()` methode.

Een "class call" houdt in dat een methode wordt aangeroepen via de
syntax `<classnaam>.<methode>()`. Dus om de methode `__init__()` van
`Persoon` aan te roepen, kan ik schrijven `Persoon.__init__()`. Ik ben
daarbij niet beperkt tot het aanroepen van alleen superclass methodes;
ik kan op deze manier methodes van iedere willekeurige class aanroepen.
Omdat dit geen reguliere aanroep van een methode is, moet `self` als
argument meegegeven worden. Dus, voor de code hierboven, als ik de
`__init__()` methode van `Persoon` wil aanroepen vanuit de `__init__()`
methode van `Student`, dan schrijf ik
`Persoon.__init__( self, firstname, lastname, age )` (ik mag hier `self`
gebruiken omdat iedere instantie van `Student` ook een instantie van
`Persoon` is, aangezien `Student` een subclass is van `Persoon`).

Via de standaardfunctie `super()` kan ik direct aan de superclass
refereren vanuit een subclass, zonder dat ik de naam van de superclass
ken. Ik kan dus de `__init__()` methode van de superclass van `Student`
aanroepen via `super().__init__()`. Ik hoef dan niet `self` als eerste
argument mee te geven. Dus, voor de code hierboven, als ik de
`__init__()` methode van `Persoon` wil aanroepen vanuit de `__init__()`
methode van `Student`, dan schrijf ik
`super().__init__( firstname, lastname, age )`.

Ik prefereer de tweede benadering, gebruik makend van `super()`, maar
alleen op deze specifieke manier: het aanroepen van de directe
superclass via overerving vanuit een enkele class. `super()` kan op
diverse andere manieren gebruikt worden en heeft wat eigenaardigheden,
die ik later in dit hoofdstuk zal bespreken.

In de code hieronder krijgt de class `Student` twee nieuwe attributen:
een studieprogramma en een list van cursussen. De methode `__init__()`
wordt overschreven om die nieuwe attributen toe te voegen, waarbij ook
de `__init__()` methode van `Persoon` wordt aangeroepen. `Student`
krijgt daarnaast een nieuwe methode, `inschrijven()`, om cursussen toe
te voegen aan de cursus-list. Tenslotte heb ik als demonstratie de
methode `minderjarig()` overschreven om studenten minderjarig te maken
als ze nog geen 21 zijn (mijn excuses daarvoor).

```python
class Persoon:
    def __init__( self, voornaam, achternaam, leeftijd ):
        self.voornaam = voornaam
        self.achternaam = achternaam
        self.leeftijd = leeftijd
    def __repr__( self ):
        return "{} {}".format( self.voornaam, self.achternaam )
    def minderjarig( self ):
        return self.leeftijd < 18

class Student( Persoon ):
    def __init__( self, voornaam, achternaam,
        leeftijd, programma ):
        super().__init__( voornaam, achternaam, leeftijd )
        self.cursussen = []
        self.programma = programma
    def minderjarig( self ):
        return self.leeftijd < 21
    def inschrijven( self, cursus ):
        self.cursussen.append( cursus )

albert = Student( "Albert", "Applebaum", 19, "CSAI" )
print( albert )
print( albert.minderjarig() )
print( albert.programma )
albert.inschrijven( "Toepassingen van rationaliteit" )
albert.inschrijven( "Verweer tegen de zwarte kunsten" )
print( albert.cursussen )
```

### Meervoudige overerving

Je kunt een class creëren die erft van meerdere andere classes. Dit
wordt "meervoudige overerving" genoemd. Je specificeert dan alle
superclasses, met komma's ertussen, tussen de haakjes van de class
definitie. Die nieuwe class vormt dan een combinatie van alle
superclasses.

Als een methode van een instantie van de nieuwe class wordt aangeroepen,
moet Python beslissen welke methode gebruikt wordt als deze voorkomt in
meerdere van de samenstellende classes. Python controleert daarvoor
eerst de subclass zelf. Als de methode daar niet gevonden wordt, worden
alle superclasses gecontroleerd, van links naar rechts. Zodra een
specificatie van de methode gevonden wordt, wordt die uitgevoerd.

Als je de methode van een superclass wilt uitvoeren, moet je aan Python
aangeven welke superclass je daarvoor wilt gebruiken. Dat gaat het beste
via een "class call." Maar je kunt hier ook `super()` voor gebruiken.
Dat is wel een beetje ingewikkeld. Je moet als argumenten de classes
verstrekken die je wilt laten controleren, in de volgorde dat je wilt
dat ze gecontroleerd worden. Het eerste argument van `super()` wordt
daarbij echter overgeslagen (ik neem aan dat dat `self` zou moeten
zijn).

Dit werkt dus ongeveer als volgt: Je hebt drie classes, A, B, en C. Je
creëert een nieuwe class D die erft van de andere drie, via de definitie
`class D( A, B, C )`. Als je in de `__init__()` methode van D de
`__init__()` methodes van de drie superclasses wilt aanroepen, doe je
dat via class calls `A.__init__()`, `B.__init__()`, en `C.__init__()`.
Echter, als je de `__init__()` methode van slechts één ervan wilt
aanroepen, en je niet precies weet van welke, maar je weet wel in welke
volgorde je ze zou willen controleren (bijvoorbeeld B, C, A), dan kun je
een aanroep doen via `super()` met `self` als eerste argument en de drie
andere classes in de volgorde van controle (bijvoorbeeld
`super( self, B, C, A ).__init__()`).

Zoals ik al zei, het is wat ingewikkeld. Meervoudige overerving is
zowiezo ingewikkeld. Over het algemeen raad ik je aan om meervoudige
overerving niet te gebruiken, tenzij er geen enkele andere manier is om
een probleem op te lossen. Veel object georiënteerde talen ondersteunen
meervoudige overerving niet eens, en de talen die dat wel doen zetten er
vaak waarschuwingen bij.

Ik ga daarom geen een praktijkvoorbeeld geven van meervoudige
overerving, noch zul je hieronder opgaves aantreffen die het gebruiken.
Je moet het gewoon vermijden, totdat je flink veel ervaring hebt
opgebouwd met Python en object georiënteerd programmeren. En als je dat
eenmaal bereikt hebt, kom je waarschijnlijk gemakkelijk tot manieren om
programma's te construeren die meervoudige overerving niet nodig hebben.
