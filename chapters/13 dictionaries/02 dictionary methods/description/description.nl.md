Hieronder staan de dictionary methodes die het meest gebruikt worden.

### `copy()`

Net als met lists, kun je een variabele die een dictionary bevat via de
assignment operator aan een andere variabele koppelen, en daarmee maak
je dan een alias voor de dictionary (als je je dat niet herinnert, moet
je er hoofdstuk
13
nog eens op naslaan). Het is niet mogelijk dezelfde "truuk" die bij
lists bestaat te gebruiken om een kopie te maken. In plaats daarvan
hebben dictionaries een methode `copy()` die een kopie van de dictionary
maakt en retourneert.

```python
fruitmand = { "appel":3, "banaan":5, "kers":50 }
fruitmandalias = fruitmand
fruitmandcopy = fruitmand.copy()

print( id( fruitmand ) )
print( id( fruitmandalias ) )
print( id( fruitmandcopy ) )
```

Merk op dat een dergelijke kopie een ondiepe kopie is (zie hoofdstuk
13
als je je het verschil tussen ondiepe en diepe kopieën niet herinnert).
Als je een diepe kopie wilt maken, moet je de `deepcopy()` functie van
de `copy` module gebruiken.

### `keys()`, `values()`, and `items()`

De methode `keys()` levert een iterator die alle keys van de dictionary
genereert. De methode `values()` levert een iterator die alle waardes
van een dictionary genereert. De methode `items()` levert een iterator
die 2-tuples genereert die alle keys en waardes van de dictionary
bevatten.

Ik zeg specifiek dat deze methodes iterators retourneren en niet lists.
Als je wat ze retourneren in lists wil veranderen, moet je list casting
gebruiken (zie hoofdstuk
13).

```python
fruitmand = { "appel":3, "banaan":5, "kers":50 }
print( list( fruitmand.keys() ) )
print( list( fruitmand.values() ) )
print( list( fruitmand.items() ) )
```

Op dit punt vraag je je wellicht af wanneer je een iterator kunt
gebruiken. Je gebruikt iterators met name in `for` loops (maar je kunt
ze ook gebruiken als argumenten voor de functies `max()`, `min()` en
`sum()`).

```python
fruitmand = {"appel":3,"banaan":5,"kers":50,"druif":0,"mango":2}
for key in fruitmand.keys():
    print( "{}:{}".format( key, fruitmand[key] ) )
print( sum( fruitmand.values() ) )
```

Omdat deze code een onvoorspelbare volgorde voor de keys doorloopt, wil
je ze meestal sorteren voordat je ze in de loop verwerkt. Omdat `keys()`
geen list maar een iterator levert, kun je ze niet direct sorteren, maar
moet je het resultaat van `keys()` eerst met een list casting in een
list omzetten. Daarna kun je de list sorteren.

```python
fruitmand = {"appel":3,"banaan":5,"kers":50,"druif":0,"mango":2}
keylist = list( fruitmand.keys() )
keylist.sort()
for key in keylist:
    print( "{}:{}".format( key, fruitmand[key] ) )
```

Je kunt niet direct de `sort()` methode toepassen op de list casting,
met andere woorden, `keylist =` `list( fruitmand.key() ).sort()` werkt
niet. Je moet eerst de list creëren, en dan pas sorteren. Je kunt ook
niet schrijven `for key in keylist.sort()`, omdat de `sort()` methode
geen retourwaarde heeft.

Als je je afvraagt waarom Python iterators boven lists prefereert: het
antwoord daarop is dat iterators meer generiek bruikbaar zijn en minder
geheugen gebruiken. Het zijn "luie" methodes, omdat ze alleen een item
produceren als erom gevraagd wordt.

### `get()`

De `get()` methode kun je gebruiken om een waarde uit de dictionary te
halen zelfs als je niet weet of de key die je zoekt wel in de dictionary
zit. Je roept de `get()` methode aan met de key die je zoekt als
argument, en het geeft de corresponderende waarde terug als de key
bestaat, of de speciale waarde `None` als de key niet bestaat in de
dictionary. Als je in plaats van `None` een andere waarde terug wilt
krijgen als de key niet bestaat, dan kun je die waarde meegeven als het
tweede, optionele argument.

```python
fruitmand = {"appel":3,"banaan":5,"kers":50,"druif":0,"mango":2}

appel = fruitmand.get( "appel" )
if appel:
    print( "appel is in de mand" )
else:
    print( "geen appels in de mand")

aardbei = fruitmand.get( "aardbei" )
if aardbei:
    print( "aardbei is in de mand" )
else:
    print( "geen aardbei in de mand")

banaan = fruitmand.get( "banaan", 0 )
print( "aantal bananen in de mand:", banaan )

aardbei = fruitmand.get( "aardbei", 0 )
print( "aantal aarbeien in de mand:", aardbei )
```

Voer de code hierboven uit en bestudeer de uitkomst, omdat wat de code
demonstreert over de `get()` methode erg nuttig is. Stel je voor dat een
collectie van items hebt met corresponderende hoeveelheden,
bijvoorbeeld, de inhoud van een fruitmand waarbij de keys de namen van
fruit zijn, en de waardes de hoeveelheden. Als je in de `fruitmand`
dictionary zoekt met de `get()` methode en als tweede argument een nul,
kun je naar een willekeurig stuk fruit zoeken in de mand zonder dat je
eerst moet controleren of het bestaat in de mand, want als je naar een
fruitnaam vraagt die er niet als key in voorkomt, krijg je nul terug, en
dat is precies wat je wilt zien.

### Oefening

De code hieronder bevat een list met woorden. Bouw een dictionary die al
deze woorden als key heeft, en als waarde hoe vaak het woord voorkomt in
de list. Print daarna de woorden met hun hoeveelheden.

```python
woordlist = ["appel","doerian","banaan","doerian","appel","kers",
    "kers","mango","appel","appel","kers","doerian","banaan",
    "appel","appel","appel","appel","banaan","appel"]
```

De code hieronder bevat een string met woorden gescheiden door komma's.
Bouw een dictionary die al deze woorden als key heeft, en als waarde hoe
vaak het woord voorkomt in de list. Print daarna de woorden met hun
hoeveelheden.

```python
tekst = "appel,doerian,banaan,doerian,appel,kers,kers,mango," + \
    "appel,appel,kers,doerian,banaan,appel,appel,appel," + \
    "appel,banaan,appel"
```

De code hieronder bevat een kleine dictionary die vertalingen bevat van
Engelse woorden naar Nederlandse. Schrijf een programma dat met behulp
van deze dictionary een woord-voor-woord vertaling maakt van de tekst
eronder. Een woord dat niet in de dictionary voorkomt, vertaal je niet.
De dictionary gebruikt alleen kleine letters, en je kunt de hele tekst
naar kleine letters omzetten voordat je de vertaling maakt. Het is
aardig als je interpunctie in stand houdt in de vertaling, maar je mag
die ook weglaten (het is best veel werk om de interpunctie intact te
houden en het heeft niks van doen met dictionaries, dus het is niet
belangrijk – het is ook veel gemakkelijker om dit te doen als je eenmaal
geleerd hebt om te gaan met reguliere expressies, in hoofdstuk
26).
Ik besef heel goed dat de vertaling uitermate slecht is, maar daar gaat
het niet om.

```python
engels_nederlands = { "last":"laatst", "week":"week", "the":"de",
    "royal":"koninklijk", "festival":"feest", "hall":"hal",
    "saw":"zaag", "first":"eerst", "performance":"optreden",
    "of":"van", "a":"een", "new":"nieuw", "symphony":"symphonie",
    "by":"bij", "one":"een", "world":"wereld", "leading":
    "leidend", "modern":"modern", "composer":"componist",
    "composers":"componisten", "two":"twee", "shed":"schuur",
    "sheds":"schuren" }

zin = "Last week The Royal Festival Hall saw the first \
performance of a new symphony by one of the world's leading \
modern composers, Arthur \"Two-Sheds\" Jackson."
```
