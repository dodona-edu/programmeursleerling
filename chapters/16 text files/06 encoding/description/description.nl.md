Tekstfiles hebben een zogeheten "encoding" (letterlijk betekent dit
"versleuteling," maar die term wordt nooit gebruikt). Dit is een systeem
dat voorschrijft hoe de tekens in een bestand geïnterpreteerd moeten
worden. Encoding kan verschillend zijn tussen besturingssystemen. Je
kunt de standaard manier van encoding voor een besturingssysteem zien
door de functie `sys.getfilesystemencoding()` aan te roepen.

```python
from sys import getfilesystemencoding

print( getfilesystemencoding() )
```

Als je een tekstbestand leest dat een andere manier van encoding
gebruikt dan je bestandssysteem prefereert, kun je een
`UnicodeDecodeError` krijgen. Of je deze fout krijgt voor een bepaald
bestand, hangt af van je besturingssysteem. Een vervelende consequentie
daarvan is, dat als je code hebt geschreven die een bestand leest en die
fatsoenlijk werkt, en je die code naar een ander besturingssysteem
brengt, een bestand dat voorheen gelezen kon worden plotseling de code
laat stuklopen.[^20]

Een eenvoudige manier om dit probleem te omzeilen is een extra parameter
toevoegen aan het openen van een bestand, die aangeeft welk encoding
mechanisme je wilt gebruiken om het bestand te lezen. Je doet dit via
een parameter `encoding=<encodingnaam>`, waarbij `<encodingnaam>` een
string is die verschillende waardes kan hebben. Een paar typische
waardes voor deze parameter zijn:

-   `ascii`: 7-bits encoding, tekens met waardes in het bereik 00-7F

-   `latin-1`: 8-bits encoding, tekens met waardes in het bereik 00-FF

-   `mbcs`: 2-byte encoding, die momenteel vervangen wordt door UTF-8

-   `utf-8`: encoding met een variabel aantal bytes

Gewoonlijk worden tekstbestanden gecreëerd met `ascii` of `latin-1`
encoding. Omdat `ascii` een onderdeel is van `latin-1`, kun je bij het
openen van een tekstbestand altijd `latin-1` encoding gebruiken. Het is
mogelijk dat als er tekens in het bestand staan die vallen buiten de
`ascii` range, je andere tekens ziet dan waarmee het bestand
oorspronkelijk gebouwd is – dat is afhankelijk van het encoding
mechanisme van je bestandssysteem. Maar een `UnicodeDecodeError` zul je
niet krijgen. Dus als je de inhoud van een bestand probeert te lezen en
je krijgt een `UnicodeDecodeError`, kun je proberen het te openen via
`open( <``bestand``>, encoding="latin-1" )`. Over het algemeen lost dit
je probleem op.

Merk op dat `utf-8` een veel groter bereik aan tekens ondersteunt dan
`latin-1`, maar als je een tekstbestand dat gemaakt is met `latin-1`
encoding probeert te gebruiken met een bestandssysteem dat gebaseerd is
op `utf-8` encoding, kun je toch een `UnicodeDecodeError` krijgen. Dat
komt doordat `utf-8` geen tekens kent met waardes in het (hexadecimale)
bereik 80-FF.

Als je wilt zien welke speciale tekens door jouw bestandssysteem
ondersteund worden met waardes in het bereik 80-FF, kun je de code
hieronder uitvoeren. De numerieke waarde van een teken in de tabel kun
je afleiden door $16*rij+kolom$ te berekenen, waarbij `rij` en `kolom`
de hexadecimale nummering zijn van de rij en kolom. Met deze code laat
ik geen tekens zien in het bereik 80-9F, omdat die meestal niet ingevuld
zijn.

```python
for i in range(16):
    if i < 10:
        print( ' '+chr( ord( '0' )+i ), end='' )
    else:
        print( ' '+chr( ord( 'A' )+i-10 ), end='' )
print()
for i in range( 10, 16 ):
    print( chr( ord( 'A' )+i-10 ), end='' )
    for j in range( 16 ):
        c = i*16+j
        print( ' '+chr( c ), end='' )
    print()
```

Ik geef meer details over UTF-8 encoding in hoofdstuk
<a href="#ch:bitwiseoperators" data-reference-type="ref" data-reference="ch:bitwiseoperators">20</a>,
maar voor het manipuleren van tekstbestanden heb je voldoende aan de
bovenstaande informatie.

[^20]: Ik moet hier een opmerking maken over een fenomeen dat wat bizar
    kan overkomen als je het voor het eerst tegenkomt: Je kunt deze fout
    krijgen als je bestand tekens bevat met een encoding die niet door
    je besturingssysteem ondersteund wordt, zelfs als die tekens zich
    bevinden in regels in het bestand die je niet eens probeert in te
    lezen! Bijvoorbeeld, stel dat je zo'n speciaal teken hebt op regel
    10 in het bestand, en je probeert alleen de eerste 5 regels van het
    bestand te lezen voordat je het bestand weer sluit – je programma
    kan dan nog steeds de genoemde fout geven! Ik vermoed dat dit
    gerelateerd is aan het "bufferen" van data: als je Python vraagt een
    klein stukje data uit een bestand te lezen, dan leest Python toch
    grotere delen van het bestand, zodat het sneller is als je later
    meer van het bestand gaat lezen. Dus door slim te zijn, kan Python
    je met problemen opzadelen die je niet aan zag komen. Het is goed om
    je bewust te zijn van dit soort eigenschappen van Python.
