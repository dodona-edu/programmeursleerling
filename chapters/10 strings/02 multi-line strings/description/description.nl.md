In Python kunnen strings meerdere regels beslaan. Dat kan nuttig zijn
wanneer je een erg lange string in je programma hebt, of als je de
output van de string op een specifieke manier wilt formatteren. Dit kan
op twee manieren bereikt worden:

-   Met enkele of dubbele aanhalingstekens, en een indicatie dat de
    string doorloopt op de volgende regel door een backslash aan het
    einde van de regel te zetten.

-   Met drievoudige enkele of dubbele aanhalingstekens.

Ik demonstreer eerst hoe het werkt met enkele of dubbele
aanhalingstekens om de string:

```python
langestring = "Ik heb mijn buik vol van te worden behandeld \
als een schaap. Wat is de zin van op vakantie gaan als je \
gewoon maar een toerist bent die wordt rondgereden in een bus \
omringd door zweterige uilskuikens uit Den Haag en Rotterdam \
met hun honkbalpetjes en trainingspakken en radio's en \
De Telegraaf, klagend over de koffie - 'Oh, ze zetten geen \
lekker bakje hier, toch, niet zoals thuis' - en dan stoppen \
bij Mallorcaanse eettentjes waar ze friet en kroket verkopen \
en Heineken en calamaris met salade en ze zitten in hun \
katoenen overgooiers Nivea zonnebrand te spuiten over hun \
pafferige rauwe opgezwollen uitpuilende blubberbuiken 'omdat \
ze op de eerste dag wat teveel zon hebben gehad.'"
print( langestring )
```

Als je deze code uitvoert, zie je dat Python de string als een geheel
interpreteert. De backslash (`\`) die aangeeft dat de string verder
gaat op de volgende regel is algemener bruikbaar dan alleen voor
strings: je kunt hem achter ieder Python statement zetten om aan te
geven dat het statement verder gaat op de volgende regel. Dat kan nuttig
zijn bij bijvoorbeeld lange berekeningen.

De aanbevolen manier om strings over meerdere regels te spreiden in
Python is echter het gebruik van drievoudige aanhalingstekens. Ik heb in
een eerder hoofdstuk aangegeven dat je die gebruikt om lang commentaar
in de code op te nemen, maar feitelijk komt het erop neer dat je dan een
lange string midden in je programma zet. Zo'n string doet niks, tenzij
je hem aan een variabele toekent. Hier is een voorbeeld van een string
met drievoudige dubbele aanhalingstekens:

```python
langestring = """En je wordt onderworpen aan een eindeloze stroom
Hotel Miramars en Bellevues en Continentaals met hun moderne luxe
internationale studio's en Heineken van de tap en zwembaden vol 
vette Duitse zakenlui die denken dat ze acrobaten zijn en 
pyramides vormen en de kinderen bang maken en voordringen in de 
rij en als je niet aan tafel zit om klokslag zeven dan mis je je 
kop Knorr Romige Tomatensoep, het eerste item op het menu van de 
Internationale Cuisine, en iedere donderdagavond is er een
amateuristisch theater in de bar, met een kleine verwijfde 
Spanjool met smalle heupjes en een opblazen taart met haar haar
platgeboterd en een enorm achterwerk die Flamenco voor 
Buitenlanders presenteren."""
print( langestring )
```

Het opvallende verschil tussen deze twee voorbeelden is dat in het
eerste voorbeeld de string beschouwd werd als een lange, doorlopende
serie tekens, terwijl in het tweede voorbeeld de verschillende regels op
meerdere regels geprint wordt. De reden dat dat gebeurt in het tweede
voorbeeld is dat er een onzichtbaar teken staat aan het einde van iedere
regel, dat aangeeft dat Python naar een nieuwe regel moet gaan voordat
verder geprint wordt. Dit is een zogeheten "newline" teken, en je kunt
het expliciet in een string opnemen, door gebruik te maken van de code
`"\n"`. Deze code moet je niet lezen als twee tekens, de backslash en de
`"n"`, maar als een enkel "newline" teken. Je kunt met dit teken ervoor
zorgen dat de output over meerdere regels geprint wordt. Dat kan zelfs
als je de backslash aan het einde van een regel zet om aan te geven dat
de string over meerdere regels verspreid is, als in het eerste
voorbeeld. Bijvoorbeeld:

```python
langestring = "En een paar nasale secretaresses uit Middelburg\n\
met flubberende witte benen en buikloop die flirten met harige\n\
krombenige Spaanse obers genaamd Manuel en eens per week is er\n\
een excursie naar de plaatselijke Romeinse bouwval waar je\n\
cola kunt kopen en gesmolten ijsjes en natuurlijk Heineken en\n\
op een avond bezoek je het zogenaamde typische restaurant met\n\
rustieke uitstraling en plaatselijke atmosfeer en je zit naast\n\
een groepje toeristen uit Amstelveen die maar blijven zingen\n\
'Torremolinos, torremolinos' en klagen over het eten - 'Het is\n\
erg vettig hier, vind je niet?' - en je wordt in een hoek\n\
gedreven door een dronken groentenboer uit Hilversum met zijn\n\
instant fototoestel en plastic sandalen en het Algemeen\n\
Dagblad van afgelopen dinsdag en hij zaagt maar door en door\n\
en door over hoe meneer Jansen dit land moet besturen en\n\
hoeveel talen Frits Bolkestein wel niet spreekt en dan kotst\n\
hij zijn avondeten uit over de cocktails."
print( langestring )
```

Dit betekent dat als je niet die automatische "newlines" wilt hebben in
een string die meerdere regels beslaat, je de eerste aanpak moet
gebruiken, met de backslash aan het einde van iedere regel. Als je wel
meerdere regels wilt, dan is de tweede aanpak waarschijnlijk het beste
leesbaar.
