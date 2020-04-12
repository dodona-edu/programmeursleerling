Een **complex getal** is een getal van de vorm
$$a +bi$$, waarbij $$a$$ en $$b$$ constanten zijn, en $$i$$ een speciale
waarde, die gedefinieerd is als de wortel uit -1. Natuurlijk kun je niet
echt de wortel uit -1 berekenen, dat zou een runtime error geven; in
complexe berekeningen laat je altijd de $$i$$ staan. Bijvoorbeeld, het
complexe getal $$3 + 2i$$ kan niet verder gesimplificeerd worden.

Het optellen van complexe getallen $$a +bi$$ en $$c + di$$ is gedefinieerd als 

$$(a + c) + (b + d)i$$

### Opgave

We stellen een complexe getal voor als een `tuple` met twee numerieke waardes. Schrijf een functie `som` die de optelling van twee complexe getallen implementeert.[^16]

### Voorbeeld

```console?lang=python&prompt=>>>
>>> som((3, 4), (7, 2))
(10, 6)
```

[^16]: Python heeft een apart data type `complex` dat complexe getallen
    representeert, dus er is eigenlijk geen noodzaak om complexe
    getallen als tuples te beschrijven, maar met als doel te oefenen met
    tuples werkt de opgave best.
