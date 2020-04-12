Het schrijven in een tekstbestand lijkt veel op het lezen uit een
tekstbestand. Je opent het bestand, schrijft erin, en sluit het weer.

### Openen voor schrijven

Om een bestand te openen voor schrijven, en voor schrijven alleen, geef
je de waarde `"w"` mee als tweede argument aan de `open()` functie. Als
het bestand nog niet bestaat, wordt het gecreëerd. Bestaat het wel, dan
wordt het leeggemaakt.

Ik herhaal: **als je een bestand opent voor schrijven en het bestand
bestaat al, dan wordt de inhoud van het bestand zonder pardon
weggegooid!** Je zult geen waarschuwing krijgen die zegt "weet je het
zeker?" Het bestand wordt gewoon leeggemaakt. Dus je moet heel erg
voorzichtig zijn met het openen van een bestand voor schrijven.
Gewoonlijk vraag ik studenten om hun programma's zo te schrijven dat
eerst gecontroleerd wordt of een bestand bestaat alvorens het voor
schrijven wordt geopend, en als het bestaat, een foutmelding te geven.
Functies om te controleren of een bestand bestaat volgen later in dit
hoofdstuk.

### Schrijven met `write()`

Om iets te schrijven naar een tekstbestand, gebruik je de `write()`
methode met als argument een string die je wilt schrijven naar het
bestand. De code hieronder vraagt je om een paar strings in te geven, en
schrijft ze dan naar een bestand. Het programma stopt met het vragen om
strings als je een lege string ingeeft. Aan het einde opent het
programma het geschreven bestand, leest de inhoud, en toont die op het
scherm. Voer deze code uit, geef op zijn minst twee strings in, en zie
wat er gebeurt.

```python
fp = open( "pc_writetest.tmp", "w" )
while True:
    tekst = input( "Geef een regel tekst: " )
    if tekst == "":
        break
    fp.write( tekst )
fp.close()

fp = open( "pc_writetest.tmp" )
buffer = fp.read()
fp.close()

print( buffer )
```

Als je hebt gedaan wat ik vroeg, zie je dat alle tekst die je hebt
ingegeven in het bestand staat, maar dat alles op één lange regel staat.
Er staan geen newline tekens in het bestand. De reden is dat je newline
tekens expliciet moet schrijven als je ze in het bestand wilt hebben.
Als je input van het toetsenbord leest via de `input()` functie, stop je
weliswaar met input verstrekken door op `Enter` te drukken, maar dat
heeft dan niet als resultaat dat er een newline teken in de ingegeven
string staat. Dus je moet dat newline teken zelf toevoegen als je die
nieuwe regels wilt zien.

Pas de code hierboven aan zodat er een newline teken in het bestand komt
te staan na iedere ingegeven regel.

### Schrijven met `writelines()`

Je kunt een list van strings in één keer naar een bestand schrijven, via
de `writelines()` methode die de list als argument krijgt. Als je
newline tekens tussen de strings wilt, moet je die expliciet opnemen aan
het einde van iedere string in de list. `writelines()` is de tegenhanger
van `readlines()`; als je de list die `readlines()` retourneert als
argument voor `writelines()` gebruikt, zal de inhoud van het
uitvoerbestand exact gelijk zijn aan de inhoud van het invoerbestand.

Er is geen `writeline()` methode. `writeline()` zou precies hetzelfde
zijn als `write()`, dus hij is overbodig.

### Oefening

Schrijf een programma dat de inhoud van "pc_rose.txt" leest, en exact
dezelfde inhoud schrijft in een bestand "pc_writetest.tmp." Open dan
het bestand "pc_writetest.tmp" en toon de inhoud. Je kunt dit programma
gemakkelijk bouwen door wat van de hierboven gegeven code bij elkaar te
plakken.

Schrijf een programma dat de inhoud van "pc_rose.txt" leest, iedere
regel achterstevoren zet, en dan de geïnverteerde regels wegschrijft
naar het bestand "pc_writetest.tmp." Open daarna "pc_writetest.tmp" en
toon de inhoud.
