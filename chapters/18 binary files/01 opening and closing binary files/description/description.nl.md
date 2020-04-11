Het afhandelen van binaire bestanden lijkt veel op het afhandelen van
tekstbestanden. Je moet het bestand openen met `open()` om de inhoud te
kunnen benaderen, je sluit het af met `close()` als je klaar bent, en je
kunt lezen en schrijven met respectievelijk `read()` en `write()`.

Als je een binair bestand opent, moet je aan Python aangeven dat je dit
bestand wilt behandelen in "binaire modus." Je doet dit door de letter
`"b"` aan het modus argument toe te voegen. Bijvoorbeeld, om een bestand
te openen in "binair lezen" modus, gebruik je `"rb"` als modus. Je kunt
ook een binair bestand openen voor zowel lezen als schrijven; dat geef
je aan met de modus `"r+"`, dus lezen en schrijven in binaire modus is
`"r+b"` (hoewel je eventueel ook een tekstbestand kunt openen in lezen
plus schrijven modus, via `"r+"`, gaf ik dat niet aan in hoofdstuk
<a href="#ch:textfiles" data-reference-type="ref" data-reference="ch:textfiles">17</a>,
omdat dat zelden zinvol is). Net als bij tekstbestanden, kun je een
binair bestand openen in "alleen schrijven" modus met `"wb"`; het
bestand wordt dan leeggemaakt. `"w+b"` opent een bestand voor zowel
lezen als schrijven, maar maakt in tegenstelling tot `"r+b"` het bestand
ook leeg om mee te beginnen.

Als je een bestand opent voor zowel lezen als schrijven, en de pointer
staat niet aan het einde van het bestand als je begint met schrijven,
dan ben je data aan het *over*schrijven.

Je kunt ieder bestand openen in binaire modus, ook al is het een
tekstbestand. Als je echter een tekstbestand opent in binaire modus, dan
behandel je het bestand ook als een binair bestand, wat inhoudt dat
Python geen automatische conversie van "newline" tekens doet.

Het sluiten van een binair bestand verschilt niet van het sluiten van
een tekstbestand.

```python
fp = open( "pc_rose.txt", "rb" )
fp.close()
```

{:class="callout callout-info"}
> #### Opmerking
> De code hierboven geeft geen uitvoer – als hij wel uitvoer geeft, dan
> betreft het een runtime error, die hoogstwaarschijnlijk inhoudt dat
> "pc\_rose.txt" niet beschikbaar is.
