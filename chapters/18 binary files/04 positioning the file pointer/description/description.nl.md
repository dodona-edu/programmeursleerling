Het bestand "pc\_binarytest.tmp" bevat een aantal geheime woorden, die
je niet kunt herkennen als je de inhoud van het bestand toont. Ik
gebruik ze als illustratie bij het positioneren van de pointer.

De pointer heeft in een bestand aan waar je begint met lezen of
schrijven. Je kunt de pointer verplaatsen middels de `seek()` methode.
`seek()` krijgt twee integer argumenten, waarvan de tweede optioneel is.
Het eerste argument is de relatieve byte positie. De tweede geeft de
positie aan ten opzichte waarvan het eerste argument relatief is.

Het tweede argument is 0, 1, of 2. 0 betekent "relatief ten opzichte van
het begin van het bestand." 1 betekent "relatief ten opzichte van de
huidige positie van de pointer." 2 betekent "relatief ten opzichte van
het einde van het bestand." Als je geen tweede argument opgeeft, wordt
aangenomen dat het 0 is. In de `os` module zijn er constanten voor dit
argument opgenomen: `os.SEEK_SET` is 0, `os.SEEK_CUR` is 1, en
`os.SEEK_END` is 2.

Het eerste argument geeft aan hoeveel bytes je verwijderd moet zijn van
de positie aangegeven door het tweede argument. Als het tweede argument
0 is, moet dit een positief getal zijn; als het 2 is, moet het een
negatief getal zijn; als het 1 is, mag het negatief of positief zijn,
afhankelijk van of je de pointer meer naar het begin of meer naar het
einde wilt bewegen. Bijvoorbeeld, `fp.seek(5)` is gelijk aan
`fp.seek(5,0)`, en beweegt de pointer naar een positie 5 bytes
verwijderd vanaf het begin van het bestand, op de zesde byte (de eerste
byte die gelezen zal gaan worden als je de `read()` methode aanroept).

Als je wilt weten waar de pointer gepositioneerd is, kun je de `tell()`
methode gebruiken. Zowel `seek()` als `tell()` werken ook voor
tekstbestanden, maar zijn dan niet erg nuttig.

De geheime boodschap begint op positie 50, en is 23 tekens lang. De
codering is zo gemaakt dat als je 128 aftrekt van de byte waardes, je de
getallen krijgt die je met de `ord()` functie in de juiste letters kunt
omzetten. Dus zo krijg je de boodschap te lezen:

```python
fp = open( "pc_binarytest.tmp", "rb" )
print( "1. Huidige positie van de pointer is", fp.tell() )
fp.seek( 50 )
print( "2. Huidige positie van de pointer is", fp.tell() )
buffer = fp.read( 23 )
print( "3. Huidige positie van de pointer is", fp.tell() )
fp.close()

print( buffer )
s = ""
for c in buffer:
    s += chr( c-128 )
print( "De geheime boodschap is:", s )
```

De `seek()` methode is vooral nuttig als je een bestand opent in "lezen
plus schrijven" modus (`"r+b"`). Je kunt ermee door het bestand bewegen
en lezen wat je moet lezen, en (over)schrijven waar dat nodig is.

Open "pc\_binarytest.tmp" in binaire "lezen plus schrijven" modus, en
overschrijf de gecodeerde boodschap met de vertaling. Als je het bestand
weer gesloten hebt, open het dan in tekst modus, lees de inhoud, en toon
die. Als je het correct hebt gedaan, zie je twee leesbare regels. Als je
het bestand per ongeluk kapot maakt, kun je het altijd opnieuw creëren.
