Een binair bestand kent geen "regels." De enige manier om informatie uit
een binair bestand te krijgen is de `read()` methode gebruiken. Als je
`read()` zonder argument gebruikt, wordt het hele bestand gelezen
(beginnend bij de pointer). Als je de methode echter een integer
meegeeft als argument, dan geeft die integer het aantal bytes aan dat
gelezen wordt (beginnend bij de pointer, en niet verder lezend dan het
einde van het bestand).

Voor het geval de term nieuw is: een "byte" is een 8-bits teken, dat wil
zeggen, een getal tussen nul en 255, opgeslagen in de kleinste
geheugeneenheid die door computers ondersteund wordt. De reguliere
tekens die je op het toetsenbord vindt worden alle opgeslagen in een
enkele byte, en de tekens in een string zijn ook ieder één byte, maar
beperkt tot een kleinere reeks getallen.

### Byte strings

En hier treden we dan de obscure krochten van de Python taal binnen. Als
je leest uit een binair bestand, dan retourneert de `read()` methode
niet een reguliere string zoals je gewend bent bij het lezen uit
tekstbestanden – het retourneert een "byte string." Er zijn subtiele
verschillen tussen strings en byte strings. Om die te demonstreren, moet
ik eerst vertellen dat je kunt aangeven dat een string een byte string
is door een letter `b` voor de string te plaatsen. Dus `"Hello, world`"!
is een string, terwijl `b"Hello, world`"! een byte string is.

![binair bestand](media/BinaryFile.png "binair bestand"){:width="50%"}

```python
hw1 = "Hello, world!"
hw2 = b"Hello, world!"

print( hw1 )
print( hw2 )
```

Het verschil tussen een string en een byte string is dat een byte string
tekens kan bevatten die een string niet kan bevatten. Als je even
terugdenkt aan de ASCII tabel, herinner je je wellicht dat ieder teken
een getal met zich geassocieerd heeft. Je zag, bijvoorbeeld, dat "A"
nummer 65 heeft, en de spatie nummer 32. De spatie was het laagste teken
van de ASCII tabel dat ik liet zien, en je vraagt je je dus wellicht af
wat er aan de hand is met de nummers 0 tot en met 31. Het antwoord is:
dat zijn controle-tekens, en geen legale tekens die je in een string
kunt zetten (op een paar uitzonderingen na). Je kunt proberen ze in een
string op te nemen als een speciaal teken: als je `\x`, gevolgd door een
hexadecimale code van twee hexadecimale cijfers, opneemt, representeert
dat het teken met dat hexadecimale getal als nummer. Bijvoorbeeld, de
hexadecimale code voor een spatie is `\x20`. Met andere woorden:
`"Hello, world!\"` is hetzelfde als `"Hello,\\x20world!\"` (ik heb dit
allemaal eerder besproken in hoofdstuk
11).

```python
hw1 = "Hello,\x20world!"
print( hw1 )
```

Maar wat gebeurt er als je op deze manier een illegaal teken in een
string probeert op te nemen? Dan wordt zo'n teken gewoon genegeerd:

```python
print( "Hello,\x00\x01\x02world!" )
```

Het probleem is dat zulke tekens kunnen voorkomen in binaire bestanden,
dus je moet ze uit binaire bestanden kunnen lezen. Omdat byte strings
deze tekens wel kunnen bevatten, resulteert het lezen uit binaire
bestanden in byte strings.

```python
print( b"Hello,\x00\x01\x02world!" )
```

Je kunt de tekens in een byte string benaderen via indices, net zoals je
kunt met reguliere strings. Het verschil is dat als je een teken via een
index uit een string haalt, je een letter krijgt, terwijl het halen van
een teken via een index uit een binaire string een nummer oplevert. De
nummers zijn codes voor de letters, die je ook krijgt als je de `ord()`
functie op zo'n letter loslaat.

```python
hw1 = "Hello, world!"
hw2 = b"Hello, world!"

for c in hw1:
    print( c, end=" " )
print()
for c in hw1:
    print( ord( c ), end=" " )
print()
for c in hw2:
    print( c, end=" " )
```

Omdat bytes getallen zijn tussen 0 en 255, kan het voorkomen dat je een
getal naar een byte string met lengte 1 wilt omzetten, of een list van
getallen naar een byte string met een grotere lengte. Je kunt dat doen
door een `bytes` cast op een list van zulke getallen. Let op: als je een
enkel teken om wilt zetten van een getal naar een byte string via deze
methode, dan moet je dat teken ook in een list zetten, al heeft die list
dan maar één element. Vergeet dus niet om vierkante haken om dat ene
getal te zetten, want anders is het resultaat niet wat je zou
verwachten.

```python
bs = bytes( [72,101,108,108,111,44,32,119,111,114,108,100,33] )
print( bs )
bch = bytes( [72] )
print( bch )
fout = bytes( 72 )
print( fout )
```

Kun je een byte string omzetten naar een reguliere string. Je zou
misschien denken dat een string cast het doet, maar dat werkt helaas
niet:

```python
hw1 = b"Hello, world!"
hw2 = str( hw1 )
print( hw2 )
```

De reden dat het niet werkt, is dat als een string gegeven is als byte
string, er een codering gebruikt wordt om de string op te slaan, volgens
de Unicode standaard (die ik bediscussieerde in hoofdstuk
17).
Je moet de byte string "decoderen" volgens een zeker coderingsschema,
meestal `"utf-8"`, omdat die het meest gebruikte Unicode formaat
vastlegt. Decoderen doe je middels de `decode()` methode, met het
coderingsschema als argument. Je kunt op een soortgelijke manier een
string omzetten naar een byte string middels de `encode()` methode.

```python
hw1 = b"Hello, world!"
hw2 = hw1.decode( "utf-8" )
print( hw2 )
hw3 = hw2.encode( "utf-8" )
print( hw3 )
```

Over het algemeen is er geen reden om tekstbestanden in binaire modus te
lezen, tenminste niet als je de tekst wilt benaderen, en dus hoef je je
bij tekstbestanden je meestal geen zorgen te maken over codering en
decodering. Een uitzondering moet gemaakt worden voor tekstbestanden die
Unicode tekens bevatten. Een dergelijk bestand kun je niet behandelen
als tekstbestand, en moet je dus openen in binaire modus.

### Demonstratie binair lezen

Om te demonstreren hoe binair lezen werkt, open ik het bestand
"pc_rose.txt" in binaire modus en lees tien keer tien bytes.

```python
fp = open( "pc_rose.txt", "rb" )
for i in range( 10 ):
    buffer = fp.read( 10 )
    print( buffer )
fp.close()
```

Als je deze code uitvoert, zie je de tien byte strings getoond. Het valt
je wellicht op dat controle tekens ook getoond worden, zoals `\r` en
`\n`. De `\r` zou je niet zien als je het bestand opent als
tekstbestand, omdat Python dit teken, samen met het opvolgende teken
`\n`, omzet naar een enkele `\n`. Bovendien zou je in een reguliere
string ook het teken `\n` niet zien, omdat het een "newline" teken is
dat Python zegt dat naar de volgende regel gegaan moet worden.

Als je in plaats van een tekstbestand een echt binair bestand opent en
leest, zul je waarschijnlijk weinig betekenis kunnen ontdekken in de
tekens die je ziet.
