Een "first-in-first-out" (FIFO) structuur, ook wel
"queue" geheten, is een list waarbij steeds nieuwe elementen aan het
einde worden toegevoegd, terwijl elementen vanaf het begin van de list
verwijderd en verwerkt worden. Schrijf een programma dat een queue
verwerkt. Het programma bestaat uit een loop. In de loop wordt de
gebruiker om input gevraagd. Als de gebruiker alleen op de `Enter` toets
drukt, eindigt het programma. Als de gebruiker iets anders intoetst,
behalve als het een enkel vraagteken (`?`) is, voegt het programma
hetgeen de gebruiker heeft ingevoerd als nieuw element aan het einde van
de queue toe. Als de gebruik een enkel vraagteken ingeeft, "popt" het
programma het eerste element van de queue en toont het. Houd er rekening
mee dat de gebruiker een vraagteken kan ingeven terwijl de queue leeg
is.

### Opgave

Stel een queue voor als een lijst (`list`) van strings (`str`), en schrijf de volgende drie functies.

- Schrijf een functie `push` waaraan een queue en een element moeten doorgegeven worden. De functie moet het gegeven element achteraan de gegeven queue toevoegen, en mag niets teruggeven.

- Schrijf een functie `pop` waaraan een queue moet doorgegeven worden. De functie moet het eerste element uit de gegeven queue verwijderen en teruggeven. Als de gegeven queue leeg is, dan moet de functie de queue ongewijzigd laten en `None` teruggeven.

- Schrijf een functie `verwerk` waaraan een lijst (`list`) van strings (`str`) moet doorgegeven worden, die staan voor de opeenvolgende regels die de gebruiker ingeeft. Vertrekkend van een lege queue moet de functie die regels één voor één verwerken: een lege regel beëindigt de verwerking, een enkel vraagteken (`?`) popt het eerste element van de queue en drukt het af, en elke andere regel wordt achteraan de queue toegevoegd. Als de gebruiker een vraagteken ingeeft terwijl de queue leeg is, dan moet de functie in de plaats daarvan de boodschap `De queue is leeg.` afdrukken.

### Voorbeeld

```console?lang=python&prompt=>>>
>>> queue = ['appel', 'peer']
>>> push(queue, 'vijg')
>>> queue
['appel', 'peer', 'vijg']
>>> pop(queue)
'appel'
>>> queue
['peer', 'vijg']
>>> verwerk(['appel', 'peer', '?', 'vijg', '?', '?', '?', '', 'pruim'])
appel
peer
vijg
De queue is leeg.
```
