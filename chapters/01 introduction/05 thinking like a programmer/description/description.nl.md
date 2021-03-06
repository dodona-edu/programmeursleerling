Dit boek heeft niet alleen als doel om je Python te leren, maar ook om
je te leren denken als een programmeur, omdat denken als een programmeur
noodzakelijk is om te begrijpen waarvoor je computers kunt gebruiken en
hoe je ze moet gebruiken. Maar wat betekent het om te "denken als een
programmeur"? Ik zal die vraag beantwoorden door hem te illustreren met
een taak:

Stel je voor dat je een stapel kaarten hebt, en op iedere kaart staat
een verschillend getal geschreven. Je moet deze kaarten sorteren van
laag naar hoog, met het laagste getal bovenop. De meeste mensen kunnen
die taak uitvoeren. Voor de meeste mensen geldt ook dat als je ze vraagt
*hoe* ze de taak uitvoeren, ze je vragend aan zullen kijken en zeggen:
"Eh…, ik sorteer ze van laag naar hoog… wat bedoel je met hoe ik dat
doe?" Anderen zullen zeggen: "Ik zoek eerst de hoogste kaart en die leg
ik onderop. Dan zoek ik de op-een-na-hoogste en die leg ik erbovenop.
Enzovoorts." Dit legt min of meer uit hoe ze het doen, maar als je dan
vraagt: "Maar hoe vind je de hoogste kaart?" zullen ze je ook vragend
aankijken.

Het probleem is dat als je een computer moet uitleggen hoe een stapel
kaarten gesorteerd moet worden, je niet kunt veronderstellen dat de
computer iets kan met vage uitspraken, zelfs als die uitspraken voor
mensen duidelijk zijn. Je kunt niet tegen de computer zeggen: "Zoek de
hoogste kaart," want zelfs als de computer Nederlands zou begrijpen, dan
zou hij nog vragen hoe hij de hoogste kaart moet vinden. Je moet heel
expliciet zijn over de handelingen die moeten worden uitgevoerd. Je moet
iets zeggen als: "Neem de bovenste kaart in je linkerhand. Doe dan het
volgende totdat de stapel leeg is: Neem de bovenste kaart in je
rechterhand. Als het getal op de kaart in je rechterhand hoger is dan
het getal op de kaart in je linkerhand, dan stop je de kaart in je
linkerhand in de aflegstapel en stopt de kaart in je rechterhand in je
linkerhand. Anders stop je de kaart in je rechterhand in de aflegstapel.
Als de stapel leeg is en je rechterhand ook leeg is, is de kaart in je
linkerhand de hoogste kaart."

Natuurlijk heeft een computer geen handen en begrijpt hij ook geen
Nederlands. Maar een computer begrijpt wel computertaal. Computertalen
hebben een zeer precieze syntax[^1] en een zeer precieze semantiek,[^2]
wat betekent dat een programma een ondubbelzinnige manier is om te
beschrijven hoe een taak uitgevoerd moet worden. Dus om een computer een
taak uit te laten voeren, moet je met behulp van een computertaal de
computer stap voor stap uitleggen hoe de taak uitgevoerd moet worden.
Slechts dan kan de computer de taak uitvoeren.

Omdat het vaak lastig is om alle stappen te overzien die een computer
moet zetten om een taak uit te voeren, moet je de taak verdelen in
kleinere subtaken, die je misschien ook weer moet opdelen in subtaken,
totdat de subtaken zo klein zijn dat je gemakkelijk de stappen kunt zien
die je nodig hebt om zulke subtaken uit te voeren. Je kunt dan ieder van
de subtaken implementeren, en ze samenvoegen om een programma voor de
grote taak te vormen.

Denken als een programmeur betekent dat je een taak kunt beschouwen
vanuit het perspectief dat een computerprogramma geschreven moet worden
om de taak op te lossen, dat je in staat bent een logische opdeling van
een taak in subtaken te maken, en dat je kunt herkennen wanneer de
subtaken klein genoeg zijn dat je ze kunt implementeren. Dit is een
vaardigheid die de meeste mensen kunnen leren, maar die veel oefening
vereist omdat er een denkproces voor nodig is dat anders is dan waar de
meeste mensen aan gewend zijn.

Door te leren programmeren in Python, beginnend met kleine programma's
die groeien in complexiteit, breng je jezelf langzaamaan ook de
denkprocessen bij die een programmeur van nature beheerst.

[^1]: De syntax zijn de regels die beschrijven wat correct-gevormde
    zinnen in een taal zijn.

[^2]: De semantiek beschrijft de manier waarop syntactisch
    correct-gevormde zinnen geïnterpreteerd moeten worden.
