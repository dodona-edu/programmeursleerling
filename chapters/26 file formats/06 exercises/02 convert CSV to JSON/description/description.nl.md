Schrijf een functie `csv2json` waaraan twee locaties van tekstbestanden (`str`) moeten doorgegeven worden. Het eerste bestand moet een CSV-bestand zijn. De functie moet de inhoud van dat CSV-bestand inlezen als een lijst van lijsten, en in JSON-formaat uitschrijven naar het tweede tekstbestand.

### Voorbeeld

In onderstaande interactieve sessie gaan we ervan uit dat het CSV-bestand [`data.csv`](media/data/data.csv){:target="_blank"} zich in de huidige directory bevindt.

```console?lang=python&prompt=>>>
>>> print(open('data.csv', 'r').read(), end='')
ID,CATEGORY,NAME,STOCK,UNITPRICE
1,Fruit,apple,1000,0.87
2,Fruit,banana,2500,0.34
3,Fruit,cherry,11225,0.07
4,Fruit,durian,0,5.52
5,Cheese,Roquefort,46,12.23
6,Cheese,Blue Stilton,1,19.88
7,Cheese,Gouda,7,11.99
8,Fruit,orange,355,0.77
9,Fruit,mango,24,1.56
10,Cheese,Cheddar,333,13.15
>>> csv2json('data.csv', 'data.json')
>>> print(open('data.json', 'r').read(), end='')
[["ID", "CATEGORY", "NAME", "STOCK", "UNITPRICE"], ["1", "Fruit", "apple", "1000", "0.87"], ["2", "Fruit", "banana", "2500", "0.34"], ["3", "Fruit", "cherry", "11225", "0.07"], ["4", "Fruit", "durian", "0", "5.52"], ["5", "Cheese", "Roquefort", "46", "12.23"], ["6", "Cheese", "Blue Stilton", "1", "19.88"], ["7", "Cheese", "Gouda", "7", "11.99"], ["8", "Fruit", "orange", "355", "0.77"], ["9", "Fruit", "mango", "24", "1.56"], ["10", "Cheese", "Cheddar", "333", "13.15"]]
```
