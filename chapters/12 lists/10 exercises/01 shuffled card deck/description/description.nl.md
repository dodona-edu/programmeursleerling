Een **standaard kaartspel** bestaat uit 52 verschillende kaarten die onderverdeeld worden in vier kleuren van elk 13 kaarten: 13 klaveren (**♣**), 13 ruiten (**♦**{:style="color:red;"}), 13 harten (**♥**{:style="color:red;"}) en 13 schoppen (**♠**). Klaveren en schoppen zijn zwart, ruiten en harten zijn rood, maar het zijn niet deze fysieke kleuren, maar de soorten die met de term **kleur** aangeduid worden. Van elke kleur zijn er telkens kaarten met een **rang** van 2 tot en met 10, een boer, een vrouw, een heer en een aas. Daarnaast bevat een spel soms twee of drie jokers, maar die laten we hier even buiten beschouwing.

### Opgave

We stellen elk van de 52 kaarten van een standaard kaartspel voor als een string (`str`) die bestaat uit de **rang** van de kaart, gevolgd door de **kleur** van de kaart:

- rangen: `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9`, `10`, `J` (boer), `Q` (vrouw), `K` (heer) en `A` (aas)

- kleuren: `C` (klaveren; **♣**), `D` (ruiten; **♦**{:style="color:red;"}), `H` (harten; **♥**{:style="color:red;"}) en `S` (schoppen; **♠**)

Zo stelt `AS` bijvoorbeeld schoppenaas voor, `10H` hartentien en `KC` klaverenheer.

Schrijf een functie `kaartspel` waaraan geen argumenten moeten doorgegeven worden. De functie moet een lijst (`list`) teruggeven met de voorstellingen van de 52 kaarten van het kaartspel die willekeurig door elkaar geschud werden.

### Voorbeeld

```console?lang=python&prompt=>>>
>>> kaartspel()
['5H', '6D', '9H', 'QD', '9S', '4C', '5C', '8S', '5S', 'KC', '6C', '2C', '6S', 'KS', '7D', '3H', '3D', 'QS', '7H', '7S', 'AC', '2S', 'AS', 'AD', '9D', '8H', '4S', '7C', '3C', '8C', 'AH', 'KD', '10D', 'JH', '8D', '4H', '10C', 'JC', 'JS', 'QC', '6H', '3S', '5D', '4D', 'JD', '2H', '10S', '10H', 'KH', '9C', 'QH', '2D']
```
