Write a function `csv2json` that takes the location of two text files (`str`). The first file must be a CSV file. The function must import the data from that CSV file as a list of lists, and export it to the second text file in JSON format.

### Example

In the following interactive session we assume the CSV file [`data.csv`](media/data/data.csv){:target="_blank"} to be located in the current directory.

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
