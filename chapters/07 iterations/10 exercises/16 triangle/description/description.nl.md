Beschouw de driehoek die hier beneden is
weergegeven. Deze driehoek bevat een kolonie Driehoekkruipers, en een
Verslinder van Driehoekkruipers. De Verslinder zit in punt D. Alle
Driehoekkuipers worden geboren in punt A. Een Driehoekkruiper die bij
punt D aankomt, wordt opgegeten.

![driehoek](media/triangle.png "driehoek"){:width="30%"}

Iedere dag kruipt iedere Driehoekkruiper over een van de lijnen in de
driehoek naar een willekeurig bepaald punt, maar niet naar het punt waar
hij de dag ervoor was. Deze beweging kost één dag. Bijvoorbeeld, een
Driehoekkruiper die net geboren is in punt A, zal op de eerste dag van
zijn leven kruipen naar B, C, of D. Als hij naar B gaat, zal hij de
volgende dag naar C of D gaan, maar niet terug naar A. Als hij naar C
gaat, zal hij de volgende dag naar B of D gaan, maar niet terug naar A.
Als hij naar D gaat, wordt hij opgegeten.

De waarschijnlijkheid dat een Driehoekkruiper op de eerste dag
onmiddellijk naar D gaat is $$1/3$$, en dan leeft hij dus maar één dag. In
principe kan een Driehoekkruiper iedere willekeurige leeftijd bereiken,
hoe hoog ook, door in cirkels te bewegen van A naar B naar C en terug
naar A (of tegen de klok in, van A naar C naar B en terug naar A). Maar
omdat hij iedere dag na de eerste per toeval kiest voor een volgend
punt, is iedere dag na de eerste de waarschijnlijkheid dat hij wordt
opgegeten $$1/2$$.

### Opgave

Bereken bij benadering de gemiddelde leeftijd waarop een Driehoekkruiper 
overlijdt. Doe dit door de simulatie van 100.000 Driehoekkruipers, waarbij je 
alle dagen dat ze leven optelt, en het totaal deelt door 100.000.

{:class="callout callout-info"}
> #### Tip
> Er zijn twee manieren waarop je dit programma kunt aanpakken: ofwel je simuleert het gedrag van één Driehoekkruiper en herhaalt dat 100.000 keer, ofwel je start met een populatie van 100.000 Driehoekkruipers in punt A, en verdeelt die over variabelen die bijhouden hoeveel Driehoekkruipers in ieder punt zitten op iedere dag, waarbij je ook bijhoudt van welk punt ze komen (overblijvende Driehoekkruipers worden aan een toevallig naburig punt toebedeeld). De eerste methode is kort en eenvoudig maar traag, de tweede is lang en complex maar snel. Je mag zelf kiezen welke methode je wilt gebruiken.

{:class="callout callout-info"}
> #### Tip
> Begin niet met 100.000 Driehoekkruipers voor je eerste pogingen. Start met 1000 (of misschien met slechts 1), en probeer het pas met 100.000 als je weet dat je programma min of meer klaar is. Testen gaat veel sneller met minder Driehoekkruipers. 1000 Driehoekkruipers kunnen worden gesimuleerd in minder dan een seconde, dus als je programma meer tijd nodig heeft, heb je waarschijnlijk een eindeloze loop gemaakt.

{:class="callout callout-info"}
> #### Tip
> Ik zal niet te specifiek zijn, maar het antwoord is ergens tussen de 1 en 5 dagen. Als je iets buiten dat bereik krijgt, is het zeker fout. Je kunt het juiste antwoord wiskundig bepalen voordat je de opgave maakt, maar dat kan behoorlijk lastig zijn.  

### Invoer

Geen invoer.

### Uitvoer

De de gemiddelde leeftijd waarop een Driehoekkruiper overlijdt, uitgedrukt als een gebroken getal met twee decimalen.
