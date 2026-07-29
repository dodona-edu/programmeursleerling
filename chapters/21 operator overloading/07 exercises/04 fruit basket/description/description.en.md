Implement a `FruitBasket`
class. The `FruitBasket` contains fruit items, and it may contain a
certain number of each item type. Keep it simple: store the fruit items
as a dictionary, with the name of the fruit as key, and the quantity as
value. For this exercise there is no need to limit what keys can be,
anything can be the name of a fruit. Implement the `__add__()` method to
add a piece of fruit to the basket (and it might be a good idea to also
implement `__iadd()__`), and implement the `__sub__()` method to remove
a piece of fruit from the basket (and `__isub__()` is a good candidate
too). Implement the `__contains__()` method to check if a certain kind
of fruit is in the basket. Also implement `__getitem__()` to check how
much of a piece of fruit there is, `__setitem__()` to add a whole bunch
of a piece of fruit at once, and `__len__()` to check how many different
pieces of fruit there are in the basket. Note that when nothing more of
a piece of fruit remains in the basket, you have to remove the key.

### Assignment

Define a class `FruitBasket` that can be used to represent a basket of fruit. One optional argument may be passed when creating a new fruit basket (`FruitBasket`): a dictionary (`dict`) that maps the name of a fruit (`str`) onto the number of pieces (`int`) of that fruit in the basket. If no argument is passed, an empty basket must be created.

Fruit baskets (`FruitBasket`) must at least support the following operations:

- The builtin function `len` must return the number of different kinds of fruit (`int`) in the basket.

- The operator `in` (`fruit in basket`) must return whether the basket holds at least one piece (`bool`) of the given fruit.

- Indexing a basket (`basket[fruit]`) must return the number of pieces (`int`) of the given fruit in the basket, or `0` if the basket does not hold that fruit at all.

- Assigning to an index (`basket[fruit] = n`) must set the number of pieces of the given fruit in the basket to $$n$$. If $$n \leq 0$$, the fruit must be taken out of the basket.

- The operator `+` (`basket + fruit`) must return a new fruit basket (`FruitBasket`) that holds one piece more of the given fruit. The basket the operator was applied to must not change. The operator `+=` (`basket += fruit`) must put one piece more of the given fruit in the basket itself.

- The operator `-` (`basket - fruit`) must return a new fruit basket (`FruitBasket`) that holds one piece less of the given fruit. The basket the operator was applied to must not change. The operator `-=` (`basket -= fruit`) must take one piece of the given fruit out of the basket itself. Taking away the last piece of a fruit must take that fruit out of the basket, and taking away a fruit that is not in the basket must change nothing.

- If a fruit basket is passed to the builtin functions `repr` or `str`, a string (`str`) must be returned that reads as a Python expression that creates the same basket, with the fruits listed in alphabetical order.

### Example

```console?lang=python&prompt=>>>
>>> basket = FruitBasket({'mango': 2})
>>> basket
FruitBasket({'mango': 2})
>>> len(basket)
1
>>> basket['mango']
2
>>> basket['kiwi']
0
>>> 'kiwi' in basket
False
>>> basket['kiwi'] = 3
>>> basket + 'kiwi'
FruitBasket({'kiwi': 4, 'mango': 2})
>>> basket
FruitBasket({'kiwi': 3, 'mango': 2})
>>> basket -= 'mango'
>>> basket -= 'mango'
>>> basket
FruitBasket({'kiwi': 3})
>>> basket - 'papaya'
FruitBasket({'kiwi': 3})
>>> len(basket)
1
```
