Hoe vaak komt elk letter in een tekst voor?

### Opgave

Schrijf een functie `letterfrequenties` waaraan de locaties van vier tekstbestanden (`str`) moeten doorgegeven worden. De functie moet voor elke letter van het alfabet de frequentie berekenen waarmee die letter in elk van eerste drie tekstbestanden voorkomt. Deze frequentie van een letter is gelijk aan het aantal keer dat een letter voorkomt in het bestand, gedeeld door het totaal aantal letters in het bestand. Daarbij wordt geen onderscheid gemaakt tussen hoofdletters en kleine letters.

De functie moet een CSV-bestand uitschrijven naar het vierde de tekstbestand. Dit CSV-bestand bevat voor elke letter uit het alfabet (in alfabetische volgorde) een record met vier velden: **i**) de letter (in kleine letters), **ii**) de frequentie de letter in het eerste tekstbestand, **iii**) de frequentie de letter in het tweede tekstbestand en **iv**) de frequentie de letter in het derde tekstbestand. Alle frequenties moeten uitgeschreven worden met vijf decimalen (afgerond).

### Voorbeeld

In onderstaande interactieve sessie gaan we ervan uit dat de tekstbestanden [`data_a.txt`](media/data/data_a.txt), [`data_b.txt`](media/data/data_b.txt) en [`data_c.txt`](media/data/data_c.txt) zich in de huidige directory bevinden.

```console?lang=python&prompt=>>>
>>> letterfrequenties('data_a.txt', 'data_b.txt', 'data_c.txt', 'data.csv')
>>> print(open('data.csv').read(), end='')
a,0.06081,0.08505,0.10141
b,0.00000,0.04527,0.01127
c,0.16216,0.02332,0.01972
d,0.10135,0.04527,0.01972
e,0.02027,0.11111,0.11268
f,0.01351,0.01372,0.02535
g,0.00000,0.02881,0.01408
h,0.10811,0.08368,0.07606
i,0.01351,0.05075,0.03944
j,0.00000,0.01235,0.00000
k,0.06081,0.01097,0.00282
l,0.04730,0.04115,0.03944
m,0.02027,0.03567,0.05070
n,0.00676,0.04938,0.07606
o,0.14865,0.07407,0.10423
p,0.00000,0.00412,0.00845
q,0.00000,0.00000,0.00000
r,0.00000,0.04664,0.05915
s,0.02703,0.05213,0.04225
t,0.00000,0.09191,0.11549
u,0.12838,0.02881,0.02254
v,0.00000,0.00823,0.00000
w,0.08108,0.03292,0.03380
x,0.00000,0.00137,0.00000
y,0.00000,0.02332,0.02535
z,0.00000,0.00000,0.00000
```

{:class="callout callout-info"}
> #### Opmerking
> Aangezien het resultaat een CSV-bestand is, kun je het ook
> openen in een spreadsheet programma. Een snelle controle om te zien of je 
> uitkomst correct is, is dat alle frequenties tussen nul en 1 moeten liggen, en 
> dat de frequenties voor de letter `e` het hoogste is voor alle bestanden, terwijl 
> ook de frequenties voor `a` en `n` behoorlijk hoog zijn. Als je langere bestanden 
> gebruikt die allemaal in dezelfde taal geschreven zijn, zullen de frequenties 
> meestal veel dichter bij elkaar liggen.
