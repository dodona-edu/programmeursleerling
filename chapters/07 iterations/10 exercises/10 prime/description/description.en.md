Een priemgetal is een positief geheel getal dat deelbaar is door precies twee
verschillende getallen, namelijk 1 en het priemgetal zelf. Het laagste en enige
even priemgetal is 2. De eerste 10 priemgetallen zijn 

> 2, 3, 5, 7, 11, 13, 17, 19, 23, 29

### Input

Een getal $$n \in \mathbb{N}_0$$.

### Uitvoer

Een zin die aangeeft of $$n$$ een priemgetal is.

{:class="callout callout-info"}
> #### Tip
> Test in een loop alle mogelijke delers van het getal. In deze loop kun je concluderen dat een getal geen priemgetal is zodra je een deler (anders dan 1 of het getal zelf) hebt gevonden. Je kunt echter alleen na afloop van de loop constateren dat het getal een priemgetal is, want dan heb je pas alle mogelijke delers getest.

### Voorbeeld

#### Input:

```
11
```

#### Uitvoer:

```
11 is een priemgetal
```

### Voorbeeld

#### Input:

```
12
```

#### Uitvoer:

```
11 is geen priemgetal
```
