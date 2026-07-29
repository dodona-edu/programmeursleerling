Hoewel dit hoofdstuk over binaire
bestanden gaat, werden in de vorige twee opgaves geen binaire bestanden
gebruikt. Er valt gewoon niet veel te oefenen met binaire bestanden: de
problemen bij dit soort bestanden betreffen het behandelen van bytes, en
dat is wat de vorige twee opgaves deden. Maar om te completeren wat deze
twee opgaves begonnen, kun je nu een programma schrijven dat
tekstbestanden comprimeert en decomprimeert.

Schrijf een programma dat vraagt om een invoerbestand, dat moet bestaan,
en een uitvoerbestand, dat niet mag bestaan. Daarna vraagt het programma
of je wilt comprimeren of decomprimeren. Als je ervoor kiest om te
comprimeren, wordt het invoerbestand gecomprimeerd volgens de
bovengenoemde methode, en als uitvoerbestand weggeschreven. Als je
ervoor kiest om te decomprimeren, wordt het invoerbestand
gedecomprimeerd onder de aanname dat het eerder gecomprimeerd is middels
de bovengenoemde methode, en als uitvoerbestand weggeschreven. Dus je
zou het originele tekstbestand weer terug moeten kunnen krijgen door
eerst te comprimeren en dat te decomprimeren.

Je doet er goed aan eerst het hele bestand in het geheugen te lezen
voordat je gaat (de)comprimeren, zodat je niet in de problemen komt als
de byte string in een halve byte eindigt in plaats van in een hele byte
na compressie. Je doet er ook goed aan zowel het invoerbestand als het
uitvoerbestand als binaire bestanden te behandelen.

### Opgave

In plaats van een programma dat om zijn invoer vraagt, schrijf je twee functies waaraan telkens de locatie van een invoerbestand (`str`) en de locatie van een uitvoerbestand (`str`) moet doorgegeven worden.

- Schrijf een functie `comprimeer_bestand` die het gegeven invoerbestand in binaire modus inleest, zijn inhoud comprimeert met de methode uit de opgave *Compressie*, en het resultaat wegschrijft naar het gegeven uitvoerbestand.

- Schrijf een functie `decomprimeer_bestand` die het gegeven invoerbestand in binaire modus inleest, zijn inhoud decomprimeert met de methode uit de opgave *Decompressie*, en het resultaat wegschrijft naar het gegeven uitvoerbestand.

Beide functies lezen het volledige invoerbestand in het geheugen voor ze het (de)comprimeren, zodat het niet uitmaakt dat een gecomprimeerde byte string in een halve byte kan eindigen. Beide functies behandelen elke byte van het invoerbestand als het teken met die ordinale waarde, zodat elk bestand gecomprimeerd kan worden, en niet alleen tekstbestanden. Beide functies moeten een tuple (`tuple`) met twee elementen teruggeven: *i*) het aantal bytes dat uit het invoerbestand gelezen werd en *ii*) het aantal bytes dat naar het uitvoerbestand geschreven werd.

Beide functies moeten ook nagaan of het invoerbestand bestaat en of het uitvoerbestand nog niet bestaat. Als het invoerbestand niet bestaat, moet een `AssertionError` opgeworpen worden met de boodschap `invoerbestand bestaat niet`. Als het uitvoerbestand al bestaat, moet een `AssertionError` opgeworpen worden met de boodschap `uitvoerbestand bestaat al`.

Een bestand comprimeren en het resultaat weer decomprimeren, moet het originele bestand teruggeven.

### Voorbeeld

In onderstaande interactieve sessie gaan we ervan uit dat het tekstbestand [`data.txt`](media/data/data.txt){:target="_blank"} zich in de huidige directory bevindt, en dat de bestanden `data.cmp` en `data.new` nog niet bestaan.

```console?lang=python&prompt=>>>
>>> comprimeer_bestand('data.txt', 'data.cmp')
(13, 11)
>>> open('data.cmp', 'rb').read()
b'\x04\x81\xbb@,\xf0wI\xba\x02\x10'
>>> decomprimeer_bestand('data.cmp', 'data.new')
(11, 13)
>>> open('data.new', 'rb').read() == open('data.txt', 'rb').read()
True
>>> comprimeer_bestand('data.xxx', 'data.yyy')
Traceback (most recent call last):
AssertionError: invoerbestand bestaat niet
>>> comprimeer_bestand('data.txt', 'data.cmp')
Traceback (most recent call last):
AssertionError: uitvoerbestand bestaat al
```
