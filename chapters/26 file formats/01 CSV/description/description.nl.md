CSV staat voor "Comma-Separated Values," en is het meest gebruikte
bestandsformaat voor het importeren en exporteren van data in en vanuit
spreadsheets en databases. Het formaat stelt dat iedere regel in het CSV
bestand één record (een complete entiteit) bevat, waarbij de velden van
het record in een specifieke volgorde opgenomen zijn, van elkaar
gescheiden zijn door komma's. De eerste regel van het bestand mag een
lijst van de namen van de velden bevatten.

De code hieronder laadt en toont de inhoud van een typisch CSV bestand.
Appendix
<a href="#ch:testtextfiles" data-reference-type="ref" data-reference="ch:testtextfiles">33</a>
legt uit hoe je dit CSV bestand kunt krijgen (als je het niet al
gedownload hebt).

```python
fp = open( "pc_inventory.csv" )
print( fp.read().strip() )
fp.close()
```

Helaas is het CSV formaat niet gestandaardiseerd, en verschillende
applicaties gebruiken licht verschillende versies van CSV bestanden. Er
is wel een standaard die vrij veel gebruikt wordt, en deze standaard is
geïmplementeerd in de Python `csv` module. De module ondersteunt ook
diverse "dialecten" van het CSV formaat om verschillende soorten
bestanden te kunnen lezen en schrijven.

Het kan gebeuren dat je een excentriek CSV formaat moet gebruiken dat
niet door de module ondersteund wordt. Je kunt dan proberen met
reguliere expressies je eigen versie van het CSV formaat te
ondersteunen, of aan de module je eigen dialect toevoegen. Geen van
beide biedt een aantrekkelijk perspectief.

### CSV `reader()`

De `csv` module bevat een `reader()` functie die toegang geeft tot een
CSV bestand. De `reader()` functie krijgt een handle als argument, en
retourneert een iterator die je de mogelijkheid geeft regels uit het
bestand te halen als een list waarbij ieder veld van een record een
element van de list is. Je moet het bestand open laten zolang je het
wilt benaderen met `reader()`.

```python
from csv import reader

fp = open( "pc_inventory.csv", newline='' )
csvreader = reader( fp )
for regel in csvreader:
    print( regel )
fp.close()
```

De Python documentatie geeft de aanbeveling om, als je `reader()`
gebruikt op een bestand (en dat is wat je meestal doet), een
`newline=''` argument op te nemen bij het openen van het bestand (dat
deed ik in de code hierboven). Dit is noodzakelijk als er tekstvelden in
het CSV bestand staan die zelf newline tekens bevatten.

`reader()` zelf kan ook argumenten krijgen. De meest gebruikte zijn
`delimiter=<teken>`, die aangeeft welk `<teken>` tussen twee velden
staat (default is de komma), en `quotechar=<teken>`, die aangeeft welk
`<teken>` gebruikt wordt om strings mee te omsluiten (default is het
dubbele aanhalingsteken).

### CSV `writer()`

Het schrijven van een CSV bestand is slechts een beetje moeilijker dan
het lezen. Je creëert een handle voor een CSV bestand dat je wilt
schrijven door het te openen in `"w"` modus, en je geeft de handle mee
aan de `writer()` functie van de `csv` module. Het object dat
geretourneerd wordt door `writer()` heeft een methode `writerow()` die
je kunt aanroepen met een list met velden, die dan in het uitvoerbestand
worden weggeschreven in CSV formaat.

De aanroep van `writer()` kan dezelfde argumenten krijgen als
`reader()`, inclusief een `delimiter` en een `quotechar`. Daarnaast kun
je ook nog een `quoting=<quotemethode>` argument opgeven, waarbij
`<quotemethode>` één van de volgende waardes heeft:

-   `csv.QUOTE_ALL`, die ervoor zorgt dat elk veld tussen `quotechar`s
    geplaatst wordt

-   `csv.QUOTE_MINIMAL`, die ervoor zorgt dat alleen velden door
    `quotechar`s omsloten worden als dat absoluut noodzakelijk is (dit
    is de default)

-   `csv.QUOTE_NONNUMERIC`, die ervoor zorgt dat alle velden die geen
    integers of floats zijn omsloten worden door `quotechar`s

-   `csv.QUOTE_NONE`, die ervoor zorgt dat geen enkel veld door
    `quotechar`s omsloten wordt

Het omsluiten van een veld met `quotechar`s is alleen nodig als de
string buitengewone tekens bevat, zoals newline tekens, of tekens die
ook als `delimiter` worden gebruikt.

```python
from csv import writer

fp = open( "pc_writetest.csv", "w", newline='' )
csvwriter = writer( fp )
csvwriter.writerow( ["FILM", "SCORE"] )
csvwriter.writerow( ["Monty Python and the Holy Grail", 8] )
csvwriter.writerow( ["Monty Python's Life of Brian", 8.5] )
csvwriter.writerow( ["Monty Python's Meaning of Life", 7] )
fp.close()
```

Nadat je de code hierboven hebt gebruikt om het bestand
"pc_writetest.csv" te creëren, open je het bestand en gebruikt
`reader()` om de inhoud ervan te tonen.
