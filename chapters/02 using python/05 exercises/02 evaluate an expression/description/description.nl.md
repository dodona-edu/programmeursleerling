In een interactieve Python sessie kun je commando's typen op de prompt
(`>>>`). Op Dodona krijg je zo'n sessie door onder de editor op **Naar
sandbox** te klikken; op je eigen computer krijg je er een door IDLE te
starten. Geef het commando `print(7/4)`. Je ziet dat de
uitkomst $$1.75$$ is. Geef daarna het commando $$7/4$$ (dus zonder `print`).
Zie nu dat het antwoord ook $$1.75$$ is.

```console?lang=python&prompt=>>>
>>> print(7/4)
1.75
>>> 7/4
1.75
```

De reden dat je in het tweede geval ook het antwoord ziet, is dat een
interactieve sessie altijd de uitkomst van een commando laat zien. De
uitkomst van $$7/4$$ is $$1.75$$, en dus laat de sessie $$1.75$$ zien. De
uitkomst van een `print` commando is niks, dus de sessie laat niks zien
– echter, het `print` commando zelf drukt de uitkomst af van wat er zich
tussen de haakjes bevindt, en dat is het resultaat van wat je krijgt als
je $$7$$ deelt door $$4$$, dus $$1.75$$. Daarom zie je in beide gevallen
$$1.75$$, maar de eerste is het resultaat van het gebruik van het `print`
commando, terwijl het tweede het resultaat is van de sessie die laat
zien wat de evaluatie van een berekening is.

Schrijf nu een Python programma dat alleen het commando $$7/4$$ bevat, en
dien het in. Bedenk voordat je dat doet wat je verwacht dat er gebeurt.
Zal $$1.75$$ getoond worden? Of wordt er niks getoond? Of krijg je een
foutmelding?

Controleer of je verwachting uitkomt.
