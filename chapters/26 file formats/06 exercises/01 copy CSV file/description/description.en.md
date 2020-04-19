Write a function `copy_csv` that takes the location of two text files (`str`). The first file must be a CSV file. The function must copy the content of that CSV file to the second text file, with spaces as delimiters and information fields enclosed in single quotes wherever that is needed.

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
>>> copy_csv('data.csv', 'copy.csv')
>>> print(open('copy.csv', 'r').read(), end='')
ID CATEGORY NAME STOCK UNITPRICE
1 Fruit apple 1000 0.87
2 Fruit banana 2500 0.34
3 Fruit cherry 11225 0.07
4 Fruit durian 0 5.52
5 Cheese Roquefort 46 12.23
6 Cheese 'Blue Stilton' 1 19.88
7 Cheese Gouda 7 11.99
8 Fruit orange 355 0.77
9 Fruit mango 24 1.56
10 Cheese Cheddar 333 13.15
```
