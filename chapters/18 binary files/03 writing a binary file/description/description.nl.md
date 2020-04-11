Je kunt in een binair bestand schrijven middels de `write()` methode.
Het verschil met schrijven naar een tekstbestand is dat je een byte
string als argument moet meegeven in plaats van een reguliere string. De
volgende code creëert een binair bestand en schrijft er een tekst in.

```python
from os.path import getsize

NAAM = "pc_binarytest.tmp"

fp = open( NAAM, "wb" )
fp.write( b"And now for something completely different...\x0A\
\x00\x00\x00\x00\xD4\xE8\xE5\xA0\xD3\xF0\xE1\xEE\xE9\xF3\xE8\xA0\
\xC9\xEE\xF1\xF5\xE9\xF3\xE9\xF4\xE9\xEF\xEE\x00\x00\x00" )
fp.close()

print( getsize( NAAM ), "bytes geschreven" )
```

Voer deze code uit om het binaire bestand te bouwen. De code hieronder
opent het in tekst modus (dat kun je doen omdat Python nergens aan kan
zien dat het een binair bestand is), leest de inhoud, en toont die. Je
ziet dan wat leesbare tekst en een serie onleesbare tekens.

```python
NAAM = "pc_binarytest.tmp"

fp = open( NAAM, encoding="latin-1" )
while True:
    buffer = fp.readline()
    if buffer == "":
        break
    print( buffer )
fp.close()
```

Wijzig bovenstaande code zodat je het bestand opent in binaire modus en
de inhoud toont.
