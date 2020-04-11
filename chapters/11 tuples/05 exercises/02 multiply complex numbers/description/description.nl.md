Een **complex getal** is een getal van de vorm
$$a +bi$$, waarbij $$a$$ en $$b$$ constanten zijn, en $$i$$ een speciale
waarde, die gedefinieerd is als de wortel uit -1. Natuurlijk kun je niet
echt de wortel uit -1 berekenen, dat zou een runtime error geven; in
complexe berekeningen laat je altijd de $$i$$ staan. Bijvoorbeeld, het
complexe getal $$3 + 2i$$ kan niet verder gesimplificeerd worden.

Het product van de complexe getallen $$a +bi$$ en $$c + di$$ is gedefinieerd als 

$$(a\times c - b\times d) + (a\times d + b\times c)i$$

### Opgave

We stellen een complexe getal voor als een `tuple` met twee numerieke waardes. Schrijf een functie `product` die de vermenigvuldiging van twee complexe getallen implementeert.

### Voorbeeld

```console?lang=python&prompt=>>>
>>> product((3, 4), (7, 2))
(13, 34)
```
