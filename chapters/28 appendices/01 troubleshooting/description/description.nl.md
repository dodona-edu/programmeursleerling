### Ik krijg een ImportError als ik code probeer uit te voeren

Controleer de naam van de module die je probeert te importeren. Als het
één van de standaard Python modules is, heb je waarschijnlijk een
spelfout gemaakt. Of je hebt `.py` achter de naam gezet – dat moet je
niet doen. Als de fout optreedt bij `pcinput` of `pcmaze`, dan heb je
ofwel deze modules niet gebouwd of gedownload (zie appendix
31
of
32
om dit op te lossen), of je hebt ze geplaatst op een locatie waar Python
ze niet kan vinden. Zorg dat je ze kopieert naar dezelfde plaats als
waar je je Python programma's zet.

### Ik krijg een FileNotFoundError: [Errno 2]

Je probeert een bestand te openen dat Python niet kan vinden. Wellicht
ben je vergeten het volledige pad te vermelden in de bestandsnaam, of je
denkt dat het bestand in de huidige directory staat terwijl dat niet zo
is. Of misschien probeert je code één van de standaard tekstbestanden te
openen die ik gebruik voor het boek, en je hebt die nog niet. Als dat
het geval is, zie dan appendix
33
om ze te krijgen.

### Ik krijg een SyntaxError maar ik heb geen idee wat ik fout heb gedaan

Als er meerdere syntax errors worden gerapporteerd, moet je proberen de
fout die het eerst gerapporteerd wordt, als eerste op te lossen.
Volgende fouten zijn vaak het gevolg van de eerste. Python rapporteert
bij de fout de regel waarop de fout wordt aangetroffen. Controleer die
regel. Bekijk ook de regel erboven: het is niet ongebruikelijk dat je
een fout hebt gemaakt op een bepaalde regel, maar Python ziet de fout
pas als het met de volgende regel bezig is. Syntax kleuren kunnen ook
een indicatie geven waar je de fout hebt gemaakt. Gebruikelijke syntax
fouten van beginnende programmeurs zijn het vergeten van een dubbele
punt (`:`) na een `if`, `while`, of `for` statement, het maken van
spelfouten in variabele namen, en fouten met tabulatie (inspringen).

### Ik krijg een SyntaxError die een "Non-UTF-8 code" rapporteert

Je hebt een teken in je programma gebruikt dat niet door Python verwerkt
kan worden. Bijvoorbeeld, misschien heb je je eigen naam in de code
gezet (misschien zelfs alleen maar in een commentaar-regel), en je naam
wordt gespeld met een speciaal teken dat niet op het toetsenbord staat.
Beperk je tot de tekens die op een US toetsenbord zitten. Het is niet zo
dat je geen speciale tekens mag gebruiken, maar de regels om dat te doen
worden in de latere hoofdstukken van het boek uitgelegd.

### Ik krijg een vreemde fout zelfs als ik de voorbeeld code uitvoer

Zorg ervoor dat je Python 3.4 of een later versie gebruikt. Ik heb de
code geschreven met Python 3.4, en heb vernomen dat sommige constructies
niet goed werken in eerdere versies van Python.

### Ik voer mijn programma uit maar het doet niks

Misschien staat er een eindeloze loop in je programma, dus het programma
werkt wel, maar komt nooit toe bij het punt dat uitvoer geproduceerd
wordt. Controleer je loops. Soms is het nuttig om een `print()`
statement op te nemen bij het begin van je programma, zodat je kunt zien
dat het programma daadwerkelijk is opgestart. `print()` statements in de
code kunnen je ook helpen om te ontdekken waar het vastloopt.

### Ik heb een functie (of class) gedefinieerd in mijn programma, maar het lijkt erop dat Python hem niet kan benaderen

Zorg dat je de aanroep van de class of functie correct gespeld hebt.
Bedenk dat Python onderscheid maakt tussen hoofd- en kleine letters! Als
de spelling correct is, wees er dan zeker van dat je niet een variabele
hebt gecreëerd met dezelfde naam als de functie (of class). Als je dat
hebt gedaan, interfereer je met de mogelijkheden van Python om je
functie (of class) te benaderen.

### Ik staar al uren naar mijn programma en ik kan het niet aan het werk krijgen

Soms is het goed om te pauzeren. Leg het programma weg, ga naar huis,
speel een spelletje, doe fitness, neem een douche, wat je maar wilt.
Neem het programma morgen weer op. Vraag het aan een willekeurige
programmeur: soms lopen ze vast bij het ontwikkelen van een programma en
kunnen een probleem niet oplossen, terwijl de oplossing onmiddellijk
duidelijk is als ze de volgende dag op het werk arriveren. Wat kan
helpen is om iemand anders bij je computer uit te nodigen en je probleem
aan deze andere persoon uit te leggen. Vaak gebeurt het dat je, terwijl
je het probleem uitlegt, plotseling ziet waar je een fout hebt gemaakt.
Wat je echter zeker *niet* moet doen, is verder gaan met schrijven aan
je programma zonder het probleem op te lossen. Daarmee maak je er alleen
maar een grotere chaos van. Een veel beter idee is het programma te
kopiëren en dan regels te verwijderen of code te simplificeren totdat je
programma weer iets doet dat werkt. Dat geeft je tenminste een idee waar
je je fout moet zoeken.
