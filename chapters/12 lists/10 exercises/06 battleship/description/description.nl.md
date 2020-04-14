Maak een programma dat een vereenvoudigde
versie van het spel "Zeeslagje" speelt. De computer creëert (in het
geheugen) een matrix van 3 rijen hoog en 4 kolommen breed. De rijen zijn
genummerd 1, 2, en 3, en de kolommen hebben de letters A, B, C, en D. De
computer verstopt in drie van de cellen een "oorlogsschip." Ieder schip
is precies één cel groot. De schepen mogen elkaar noch horizontaal, noch
verticaal raken. Laat het programma de schepen per toeval plaatsen, dus
niet volgens een vastgestelde configuratie.

De computer vraagt de speler te "schieten" op cellen in de matrix. De
speler doet dat door een kolom letter en rij cijfer in te geven
(bijvoorbeeld, `"D3"`). Als de cel waarop de speler schiet niks bevat,
zegt de computer "Mis!" Als de cel een schip bevat, zegt de computer
"Raak!' en verwijdert het schip (dus als de speler nog eens zou schieten
op dezelfde cel dan is het automatisch een mis). Als de speler erin
geslaagd is alle drie de schepen tot zinken te brengen, laat de computer
zien hoeveel schoten er nodig waren, en het programma eindigt.

Om te helpen bij het debuggen van het spel, laat je de computer bij de
start de matrix tonen waarbij je kunt zien welke cellen een schip
bevatten.

Hint: Als je dit een lastige oefening vindt, start dan met een bord
waarbij je de schepen al vooraf geplaatst hebt. Als de rest van de code
werkt (en dit is niet erg moeilijk na de vorige opgave), voeg dan een
functie toe waarbij de schepen per toeval geplaatst worden, zonder dat
je controleert of ze elkaar raken. Als dat eenmaal werkt, voeg je code
toe die ervoor zorgt dat de schepen elkaar niet kunnen raken.
