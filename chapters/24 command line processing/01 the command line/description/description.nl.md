Hoofdstuk
16
legde uit hoe je de "command prompt" of "command shell" van de computer
kunt benaderen. Als je dat niet meer weet, neem dat hoofdstuk nog eens
door. Het hoofdstuk gaf ook aan dat je Python programma's kunt starten
op de command prompt via het commando:

```console?lang=bash&prompt=$
$ python <programmanaam>.py
```

Dit werkt zolang je systeem weet waar het Python kan vinden en het
programma zich in de huidige directory bevindt. Als het programma niet
in de huidige directory staat, werkt het nog steeds, als je de
programmanaam maar specificeert inclusief het volledige pad.

### Batch verwerking

Stel je voor dat je een programma hebt geschreven dat de gebruiker
vraagt om een bestandsnaam en misschien een aantal extra parameters.
Daarna verwerkt je programma het genoemde bestand, gebruik makend van de
parameters. Ik vraag je vervolgens het programma te draaien voor alle
bestanden in een bepaalde directory. Deze directory bevat meer dan
tienduizend bestanden. Wat doe je?

Je kunt je programma aanpassen zodat het niet meer vraagt om een
bestand, maar om de naam van een directory, en dan alle bestanden in die
directory verwerkt. Daarbij vraagt het dan niet de gebruiker om
parameters, maar parameters die op één of andere manier van de
bestandnaam worden afgeleid, of iets dergelijks. Er moet tenslotte een
manier zijn om de parameters te achterhalen, dus je kunt je programma zo
schrijven dat het dat zelf doet. Dit lost het probleem op. Maar dan
vraag ik je om het programma uit te voeren voor een groot aantal
directories. Wat doe je?

Je kunt je programma verder aanpassen zodat het een list bevat van alle
directories die je moet verwerken, en ze dan één voor één afwerken. En
ieder keer dat ik je vraag een extra directory te verwerken, pas je
gewoon het programma aan. Het maakt niet uit wat ik vraag, je kunt
altijd het programma verder aanpassen. Hoewel je wellicht een beetje
geïrriteerd raakt van al mijn wijzigingsverzoeken.

Er bestaat een alternatieve manier om dit soort problemen af te
handelen, en dat is via batch verwerking. Alle command shells
ondersteunen het uitvoeren van "batchbestanden," die bestaan uit een
lijst van commando's die je aan het besturingssysteem geeft. Onder
Windows hebben dit soort bestanden de extensie `.bat`, terwijl bij de
Mac en Linux ze een willekeurige naam kunnen hebben. Je kunt echter
verschillende command shells installeren die andere conventies gebruiken
– je kunt zelfs de Python shell voor dit doel gebruiken en Python zelf
gebruiken om batchbestanden te schrijven.

Het batchbestand bevat commando's die gebruik maken van het eerste
programma dat ik hierboven beschreef, dat slechts één bestand bewerkt,
en roept dat programma aan voor ieder te verwerken bestand. Het probleem
is dat het programma zo geschreven was dat het gebruikersinvoer nodig
heeft, en je gaat natuurlijk niet iedere keer invoer geven als het
batchbestand het programma opnieuw aanroept. De oplossing is het
programma zo aan te passen dat het command line argumenten kan
gebruiken.

### Command line argumenten

Op de command line kun je een Python programma starten met een aantal
argumenten. Je schrijft dan:

```console?lang=bash&prompt=$
$ python <programmanaam>.py <argument_1> <argument_2> … <argument_n>
```

De argumenten zijn van elkaar gescheiden door middel van spaties en
mogen van alles zijn. Als je een argument hebt dat zelf een spatie
bevat, moet je het tussen dubbele aanhalingstekens zetten. Dat doet
natuurlijk onmiddellijk de vraag rijzen wat je moet doen als het
argument een dubbel aanhalingsteken bevat, en helaas is het antwoord
"dat hangt af van de command shell die je gebruikt." Meestal moet je het
dubbele aanhalingsteken vooraf laten gaan door een backslash, of je moet
een dubbel dubbel aanhalingsteken schrijven.

Natuurlijk zal je programma de argumenten niet automatisch verwerken. Je
moet het programma uitbreiden met code die de argumenten "binnenhaalt."

### `sys.argv`

Je krijgt toegang tot de command line argumenten die aan het programma
worden meegegeven via een voorgedefinieerde list, die beschikbaar is als
je de `sys` module importeert. De list heet `sys.argv`. Het is een list
van strings, waarbij iedere string één van de command line argumenten
is.

`sys.argv` bevat altijd minimaal één argument, namelijk de complete naam
van het Python bestand dat je uitvoert, inclusief het pad. Om te weten
hoeveel command line argumenten er zijn, kun je, zoals gewoonlijk, de
`len()` functie gebruiken.

Als je programmeert in een editor die je ook gebruikt om je programma's
te testen, kun je over het algemeen geen command-line argumenten
specificeren. Dus als je hiermee wilt experimenteren, moet je je
programma's daadwerkelijk testen in de command shell. Dat is een heel
gedoe, zeker tijdens het ontwikkelen van een programma. Ik kan je echter
vertellen hoe je je programma's zodanig kunt opzetten dat het afhandelen
van command-line argumenten optioneel is.
