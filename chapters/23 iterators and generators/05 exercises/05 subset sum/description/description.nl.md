Het "subset som" probleem
stelt de vraag of een bepaalde verzameling van integers een
deelverzameling van integers bevat die, als ze worden opgeteld, nul als
antwoord geven. Bijvoorbeeld, als de verzameling is opgeslagen als een
list, dan is het antwoord bij de list `[1, 4, -3, -5, 7]` "ja,"
aangezien $1 + 4 - 5 = 0$. Echter, voor de list `[1, 4, -3, 7]` is het
antwoord "nee," aangezien er geen deelverzameling van de integers is die
optellen tot nul. Schrijf een programma dat het subset som probleem
oplost voor een list met integers. Als er een oplossing is, druk die af;
als er geen oplossing is, geef dat dan aan.

Dit is een herhaling van één van de opgaves uit hoofdstuk
13
(Lists). In dat hoofdstuk zei ik dat je deze opgave het beste recursief
kunt aanpakken. Echter, door de `itertools` module te gebruiken, kun je
hem nu oplossen zonder recursie (ik vermoed dat recursie nog steeds
plaatsvindt in de `itertools` module, maar jij hoeft je er niet druk om
te maken).

### Opgave

"Druk een oplossing af" is moeilijk automatisch te controleren, aangezien
een list meerdere correcte oplossingen kan hebben. Schrijf daarom een
**generatorfunctie** `nulsom_deelverzamelingen` waaraan één argument moet
doorgegeven worden: een list met verschillende (unieke) integers. De
functie moet elke niet-lege deelverzameling van de list waarvan de
elementen optellen tot nul `yield`en, als een `tuple` met de elementen in
dezelfde relatieve volgorde als in de invoerlist. De lege deelverzameling
wordt nooit ge-yield, ook al telt die triviaal op tot nul (het is geen
oplossing voor het oorspronkelijke probleem). De volgorde waarin de
verschillende deelverzamelingen geproduceerd worden, maakt niet uit.

### Voorbeeld

```console?lang=python&prompt=>>>
>>> sorted(nulsom_deelverzamelingen([1, 4, -3, -5, 7]))
[(1, -3, -5, 7), (1, 4, -5)]

>>> sorted(nulsom_deelverzamelingen([1, 4, -3, 7]))
[]
```
