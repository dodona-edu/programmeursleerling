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
