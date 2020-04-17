Als je data wilt halen uit HTML
pagina's, zoek je vaak naar de delen waarin je geïnteresseerd bent
middels "mark-ups." Stel dat je een pagina hebt met data van personen,
die een ID en een naam hebben. De ID is een negen-cijferig getal,
omsloten door een code `<id>` ervoor, en een code `</id>` erna. De naam
van de persoon volgt onmiddellijk na de ID, en wordt gemarkeerd door de
code `<naam>` ervoor, en de code `</naam>` erna. Gebruik een reguliere
expressie om alle IDs met bijbehorende namen uit de tekst hieronder te
halen en te tonen. Er zijn er vijf.

```python
import re

tekst = "<html><head><title>Lijst van personen met ids</title>\
</head><body>\
<p><id>123123123</id><naam>Groucho Marx</naam>\
<p><id>123123124</id><naam>Harpo Marx</naam>\
<p><id>123123125</id><naam>Chico Marx</naam>\
<randomcrap>Etaoin<id>Shrdlu</id>qwerty</naam></randomcrap>\
<nocrap><p><id>123123126</id><naam>Zeppo Marx</naam></nocrap>\
<address>Chicago</address>\
<morerandomcrap><id>999999999</id>geennaamtezien!\
</morerandomcrap>\
<p><id>123123127</id><naam>Gummo Marx</naam>\
<note>Zoek hem op via <a href=\"http://www.google.com\">\
Google.</a></note>\
</body></html>"
```
