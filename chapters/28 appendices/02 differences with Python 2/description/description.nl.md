Deze appendix bevat een overzicht van verschillen tussen Python 2 en
Python 3, voor zover gerelateerd aan de inhoud van dit boek en voor
zover ik ervan weet. Je kunt deze appendix negeren als je alleen Python
3 gaat gebruiken.

### Operatoren

De delingsoperator (/) werkt in Python 2 anders dan in Python 3. In
Python 3 wordt automatisch aangenomen dat als je een deling maakt, je
floats moet gebruiken, en de deling neemt aan dat de getallen die
gebruikt worden floats zijn, en levert altijd een float op als uitkomst.
In Python 2 wordt aangenomen dat de uitkomst van de deling van het type
is dat het "meest gedetailleerd" is van de getallen die erbij betrokken
zijn, dat wil zeggen, als je twee getallen deelt en één ervan is een
float, dan is de uitkomst van een deling ook een float. Maar als je twee
integers deelt, is de uitkomst een integer (decimalen die mathematisch
gezien er zouden moeten zijn worden weggelaten). Python 2 werkt op dit
gebied zoals de meeste programmeertalen doen, maar zoals Python 3 werkt
is meer intuïtief en leidt tot minder fouten.

### Gereserveerde woorden

In Python 3 zijn `print` en `exec` niet langer gereserveerde woorden;
het zijn nu functies. `True`, `False`, `None` en `nonlocal` zijn nu
echter wel gereserveerde woorden.

### Basale functies

Een klein verschil tussen Python 2 en Python 3 is dat als je de `type()`
functie gebruikt, Python 3 het woord `class` toont, waar Python 2 het
woord `type` toont. De reden is dat in Python 3 alle types
geïmplementeerd zijn als classes.

De `format()` functie was in latere versies van Python 2
geïmplementeerd, maar bestond niet in de eerdere versies. In plaats
daarvan werd een formatteerstijl ondersteund die "percentage-codes"
gebruikt, zoals ook gebruikt wordt in talen zoals C++. Dit werd direct
ondersteund door de `print()` functie, en bleef onderdeel van de
`print()` functie zelfs nadat `format()` toegevoegd was (om redenen van
compatibiliteit). Het gevolg is dat in de meeste Python 2 programma's,
zelfs de programma's die in een recente versie van Python 2 zijn
geschreven, deze oudere manier van formatteren gebruikt wordt. De oudere
aanpak wordt niet langer door Python 3 ondersteund. Overigens is het
gebruik van haakjes bij de `print()` functie niet nodig voor Python 2,
maar verplicht voor Python 3.

In Python 3 is de `range()` functie een iterator (zie hoofdstuk
<a href="#ch:iteratorsandgenerators" data-reference-type="ref" data-reference="ch:iteratorsandgenerators">24</a>).
Dit betekent dat het erg weinig geheugen gebruikt: het onthoudt alleen
het laatst gegenereerde getal, de stapgrootte, en de limiet die bereikt
moet worden. In Python 2 is `range()` anders geïmplementeerd: het
produceert alle getallen in één keer in het geheugen. Dit betekent dat
een statement als `range(1000000000)` in Python 2 zoveel geheugen nodig
heeft dat je programma zou kunnen vastlopen. Dat gebeurt niet bij Python
3. In Python 2 is het daarom aan te raden om `range()` niet te gebruiken
voor meer dan tienduizend getallen of zo, terwijl in Python 3 er geen
restricties zijn.

In Python 2 zijn string manipulaties methodes die opgenomen zijn in de
`string` module, en die je gewoonlijk aanroept door de module te
importen en de methodes te gebruiken via de `string.<methode>()` syntax.
Zulke aanroepen zijn niet langer nodig in Python 3.

### Data structuren

In Python 2 geeft het sorteren van een list met een mengelmoes van data
types een runtime error. De `sort()` functie ondersteunt ook een
argument `cmp=<functie>`, dat je toestaat een functie op te geven die
twee elementen met elkaar vergelijkt. Deze functie bestaat niet langer
in Python 3, maar je kunt de key parameter voor hetzelfde doel
gebruiken. In de Python module `functools` is een functie
`cmp\_to\_key()` opgenomen die een oude-stijl `cmp` specificatie in een
nieuwe-stijl `key` specificatie wijzigt.

In Python 2 retourneren de dictionary methodes `keys()`, `values()`, en
`items()` een list in plaats van een iterator. Python 2 ondersteunt ook
een methode `has\_key()` die je kunt gebruiken om te controleren of een
key in de dictionary zit, maar deze methode is verwijderd uit Python 3.

Python 2 ondersteunt sets niet als een basis-data structuur. Je moet de
`sets` module importeren om ze te gebruiken. Je creëert bovendien een
set met de `Set()` methode, en niet de `set()` functie. Om een set met
elementen te creëren, is in Python 2 de enige manier om de elementen als
een list mee te geven aan de `Set()` methode.

De structuur van exceptions is gewijzigd tussen Python 2 en Python 3.
Specifiek is de exception `IOError` tot een alias gemaakt van de
`OSError` exception, omdat het nogal lastig was om te onderscheiden
welke specifieke problemen ieder van deze onderschept.

### Unicode

Python 2 ondersteunt Unicode niet, maar Python 3 is erop gebaseerd.
Python 3 strings zijn Unicode strings. Je merkt geen verschil zolang al
je strings alleen ASCII tekens bevatten, maar Python 2 strings kunnen
problemen krijgen als Unicode tekens in de strings gebracht worden.
Python 3 ondersteunt ook Unicode in namen voor variabelen, functies,
classes, en methodes, wat Python 2 niet toestaat. Ik raad je echter
sterk af om in de namen van deze entiteiten tekens op te nemen die geen
ASCII zijn.

Python 2 heeft geen byte strings. Die heeft Python 2 niet nodig,
aangezien Unicode niet ondersteund wordt. Als je in Python 2 een teken
wilt schrijven waarvan de numerieke waarde 0 is, gebruik je gewoon
`chr(0)`. De `read()` en `write()` methodes voor binaire bestanden
gebruiken reguliere strings in Python 2. Dit kan niet met Python 3.

In Python 2 werkt de `pickle` module op tekstbestanden. Dat kan niet
langer in Python 3, omdat Python 3 Unicode ondersteunt. Pickle bestanden
die met Python 2 gecreëerd zijn, kun je niet inladen in Python 3 en vice
versa.

### Iteratoren

Python 3 is veel meer gebaseerd op iteratoren en generatoren dan Python
2, wat een hoop voordelen heeft, vooral waar het snelheid en
geheugengebruik betreft. Het gevolg is dat er een groot aantal
verschillen bestaat tussen Python 2 en Python 3 op dit gebied. Ik heb ze
niet allemaal onderzocht, maar hier zijn er een paar:

Iteratoren in Python 2 hebben een `next()` methode. Die hebben ze niet
langer in Python 3, waar deze methode `__next__()` heet.

In Python 2 produceert `zip()` een list in plaats van een iterabele.

De `itertools` module kent ook een paar verschillen. Bijvoorbeeld, in
Python 2 kent het een functie `izip()` die een iterabele produceert,
maar omdat in Python 3 `zip()` dat zelf al doet, is `izip()` uit
`itertools` verwijderd.

### Modules

Naast `pickle` en `itertools` is ook `urllib` flink gewijzigd tussen
Python 2 en Python 3.

De `statistics` module bestaat niet in Python 2.
