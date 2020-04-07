In de IDLE shell kun je commando's typen op de
"IDLE prompt" (`>>>`). Geef het commando `print(7/4)`. Je ziet dat de
uitkomst $1.75$ is. Geef daarna het commando $7/4$ (dus zonder `print`).
Zie nu dat het antwoord ook $1.75$ is.

De reden dat je in het tweede geval ook het antwoord ziet, is dat de
IDLE shell altijd de uitkomst van een commando laat zien. De uitkomst
van $7/4$ is $1.75$, en dus laat IDLE $1.75$ zien. De uitkomst van een
`print` commando is niks, dus de shell laat niks zien – echter, het
`print` commando zelf drukt de uitkomst af van wat er zich tussen de
haakjes bevindt, en dat is het resultaat van wat je krijgt als je $7$
deelt door $4$, dus $1.75$. Daarom zie je in beide gevallen $1.75$, maar
de eerste is het resultaat van het gebruik van het `print` commando,
terwijl het tweede het resultaat is van de shell die laat zien wat de
evaluatie van een berekening is.

Schrijf nu een Python programma (dus in een bestand met de extensie
`.py`) dat alleen het commando $7/4$ bevat. Voordat je dit programma
uitvoert, bedenk wat je verwacht dat er gebeurt als je het uitvoert. Zal
de shell $1.75$ laten zien? Of laat de shell niks zien? Of krijg je een
foutmelding?

Controleer of je verwachting uitkomt.
