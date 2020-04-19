"""
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
>>> kopieer_csv('data.csv', 'kopie.csv')
>>> print(open('kopie.csv', 'r').read(), end='')
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
"""

def kopieer_csv(bronbestand, doelbestand):

    from csv import reader, writer

    with open(bronbestand, 'r') as bron:
        bron_csv = reader(bron)
        with open(doelbestand, 'w', newline='') as doel:
            doel_csv = writer(doel, delimiter=' ', quotechar="'")
            for record in bron_csv:
                doel_csv.writerow(record)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
