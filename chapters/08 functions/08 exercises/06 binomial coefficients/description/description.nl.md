Hoeveel kleurencombinaties zijn er mogelijk bij een keuze van drie kleuren uit de zeven kleuren van de regenboog? De volgorde van de kleuren is niet van belang. Dat zijn er

$$\binom{7}{3} = \frac{7!}{3!4!} = 35$$

Hoe komt men tot de waarde van deze coëfficiënt? Voor de eerste kleurkeuze zijn er 7 mogelijkheden, voor de tweede nog 6, en voor de derde nog 5. In totaal dus $$7 \times 6 \times 5 = \frac{7!}{4!} = 210$$ mogelijkheden.

Maar daarbij is rekening gehouden met de volgorde van de kleuren: eerst kan rood en dan geel gekozen zijn, maar ook eerst geel en dan rood. Om van deze volgorde af te zien, moet nog gedeeld worden door het aantal volgordes van de drie kleuren. Dat is

$$1 \times 2 \times 3 = 3! = 6$$

### Opgave

De **faculteit** van een natuurlijk getal $$n$$, genoteerd als $$n!$$, is het product van de getallen 1 tot en met $$n$$:

$$n! = \prod_{k=1}^{n}k = 1 \times 2 \times 3 \times \cdots \times n$$

Bijvoorbeeld als $$n = 5$$:

$$5! = 1 \times 2 \times 3 \times 4 \times 5 = 120$$

In overeenstemming met de definitie van het lege product is afgesproken dat

$$0! = 1$$

Een **binomiaalcoëfficient**, geschreven als

$$\binom{n}{k}$$

en uitgesproken als "$$n$$ boven $$k$$", is een grootheid uit de combinatoriek die aangeeft op hoeveel manieren men uit $$n$$ (verschillende) objecten er zonder terugleggen $$k$$ kan kiezen. Zo'n keuze heet een **combinatie**. Een binomiaalcoëfficient is gedefinieerd als het natuurlijk getal

$$\binom{n}{k} = \frac{n!}{k!(n-k)!}\ \ \ \text{voor }0 \leq k \leq n$$

en

$$\binom{n}{k} = 0\ \ \ \text{voor }k < 0\text{ of }k > n$$

Gevraagd wordt:

- Schrijf een functie `faculteit` waaraan een getal $$n \in \mathbb{N}$$ (`int`) moet doorgegeven worden. De functie moet $$n!$$ (`int`) teruggeven.

- Schrijf een functie `binomiaal` waaraan twee getallen $$n, k \in \mathbb{N}$$ (`int`) moeten doorgegeven worden. De functie moet $$\binom{n}{k}$$ teruggeven.

### Voorbeeld

```console?lang=python&prompt=>>>
>>> faculteit(5)
120

>>> binomiaal(7, 3)
35
```
