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
>>> csv2json('data.csv', 'data.json')
>>> print(open('data.json', 'r').read(), end='')
[["ID", "CATEGORY", "NAME", "STOCK", "UNITPRICE"], ["1", "Fruit", "apple", "1000", "0.87"], ["2", "Fruit", "banana", "2500", "0.34"], ["3", "Fruit", "cherry", "11225", "0.07"], ["4", "Fruit", "durian", "0", "5.52"], ["5", "Cheese", "Roquefort", "46", "12.23"], ["6", "Cheese", "Blue Stilton", "1", "19.88"], ["7", "Cheese", "Gouda", "7", "11.99"], ["8", "Fruit", "orange", "355", "0.77"], ["9", "Fruit", "mango", "24", "1.56"], ["10", "Cheese", "Cheddar", "333", "13.15"]]
"""

def csv2json(csv, json):

    from csv import reader
    from json import dump

    # import data from CSV fie
    data = []
    with open(csv, 'r') as csv:
        csv = reader(csv)
        for record in csv:
            data.append(record)

    # export data in JSON format
    with open(json, 'w') as json:
        dump(data, json)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
