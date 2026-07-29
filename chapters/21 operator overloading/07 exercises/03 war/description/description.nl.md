Gebruik de class definities die je
hiervoor hebt gecreëerd, en maak twee trekstapels. De eerste bevat de
Ruiten 2, de Harten Heer, en de Klaveren 7 (in deze volgorde). De tweede
bevat de Harten 4, de Harten 3, en de Schoppen 8 (in deze volgorde).
Laat de twee stapels het spel "Oorlogje" spelen. Dit gaat als volgt:
Trek de bovenste kaart van iedere stapel. De hoogste kaart van de twee
wordt onderop de stapel waar hij vandaan kwam gelegd, en vervolgens
wordt ook de andere kaart onderop die stapel gelegd. Het spel gaat door
totdat slechts één stapel over is.

Hint: Met deze opzet duurt het spel 13 rondes, en de eerste stapel wint
(dat moet wel, want de eerste stapel bevat een kaart die nooit door een
kaart van de tweede stapel verslagen kan worden). Zie je wat een saai
spel "Oorlogje" is? Waarom kinderen dit zouden willen spelen – met zelfs
een volledige stok kaarten – is me een raadsel.

Merk op dat normaal het spel "Oorlogje" gespeeld wordt met speciale
regels die optreden als twee kaarten met dezelfde waarde getrokken
worden, maar in dit geval hebben alle kaarten een verschillende waarde
dus die situatie kan niet optreden. Je hoeft dus ook geen rekening
daarmee te houden, maar als je dat toch wilt doen, mag het wel.

### Opgave

Definieer opnieuw de klassen `Kaart` en `Trekstapel` van de vorige opgaven (je oplossing wordt op zichzelf beoordeeld, en kan dus niets importeren uit een andere opgave). Een kaart (`Kaart`) wordt aangemaakt op basis van een kleur (`'Harten'`, `'Schoppen'`, `'Klaveren'` of `'Ruiten'`) en een waarde (`2` tot en met `10`, `'Boer'`, `'Vrouw'`, `'Heer'` of `'Aas'`), `repr` leest als een Python expressie waarmee dezelfde kaart aangemaakt wordt, `str` beschrijft de kaart in de vorm `Aas van Harten`, en de vergelijkingsoperatoren vergelijken twee kaarten enkel op hun waarde. Een trekstapel (`Trekstapel`) wordt aangemaakt op basis van een lijst (`list`) van kaarten, ondersteunt `len` en indexering (index 0 is de bovenste kaart), heeft een methode `voegtoe` die een kaart onderaan de stapel legt en een methode `trek` die de bovenste kaart van de stapel verwijdert en teruggeeft (of `None` als de stapel leeg is), en `repr` en `str` lezen als een Python expressie waarmee dezelfde trekstapel aangemaakt wordt.

Schrijf een functie `oorlogje` waaraan twee trekstapels (`Trekstapel`) moeten doorgegeven worden, die het spel "Oorlogje" spelen. Iedere ronde wordt van beide stapels de bovenste kaart getrokken. De hoogste van deze twee kaarten wordt onderop de stapel gelegd waar hij vandaan kwam, en vervolgens wordt ook de andere kaart onderop diezelfde stapel gelegd. Het spel eindigt zodra één van beide stapels geen kaarten meer heeft. De functie moet de trekstapel (`Trekstapel`) teruggeven die het spel gewonnen heeft, dat wil zeggen: de stapel die nog kaarten heeft.

Merk op dat de functie beide trekstapels wijzigt die eraan doorgegeven worden. Je mag ervan uitgaan dat de twee stapels nooit twee kaarten met dezelfde waarde bevatten, waardoor een ronde altijd een winnaar heeft, en dat het spel altijd eindigt.

### Voorbeeld

```console?lang=python&prompt=>>>
>>> stapel_1 = Trekstapel([Kaart('Ruiten', 2), Kaart('Harten', 'Heer'), Kaart('Klaveren', 7)])
>>> stapel_2 = Trekstapel([Kaart('Harten', 4), Kaart('Harten', 3), Kaart('Schoppen', 8)])
>>> winnaar = oorlogje(stapel_1, stapel_2)
>>> winnaar is stapel_1
True
>>> winnaar
Trekstapel([Kaart('Schoppen', 8), Kaart('Harten', 3), Kaart('Harten', 'Heer'), Kaart('Harten', 4), Kaart('Klaveren', 7), Kaart('Ruiten', 2)])
>>> len(stapel_1)
6
>>> len(stapel_2)
0
```
