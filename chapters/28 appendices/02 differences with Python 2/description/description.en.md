This appendix contains an overview of the differences between Python 2
and Python 3, as far as they relate to the contents of this book and as
far as I am aware of them. You can ignore this appendix if you are only
going to use Python 3.

### Operators

The division operator (/) in Python 2 works differently from the one in
Python 3. In Python 3, it is automatically assumed that if you use
division, you need floating-point numbers, so the division will assume
that all numbers involved are floats, and will always result in a float.
In Python 2, it is assumed that the division will be of the type that is
"most detailed" for the numbers involved, i.e., if you divide two
numbers and at least one is a float, it will be a floating-point
division and the result is a float, but if you divide two integers, it
will be an integer division and the result will be an integer (if the
resulting number would mathematically have decimals, then the decimals
are simply removed). The way Python 2 works is similar to what most
programming languages do, but the way Python 3 works is more intuitive
and leads to fewer errors.

### Reserved words

In Python 3, `print` and `exec` are no longer reserved words (or
keywords), as they are now functions. However, `True`, `False`, and
`None` are now keywords, as is the word `nonlocal`.

### Basic functions

A small difference between Python 2 and Python 3 is that when using the
`type()` function, where Python 3 displays the word `class`, Python 2
displays the word `type`. The reason is that in Python 3, all types are
actually implemented as classes.

The `format()` function was implemented in later versions of Python 2,
but did not exist in the earlier versions. Instead, it supported a style
of formatting, using "percentage-codes," similar to what is used in
languages such as C++. This was directly implemented in the `print()`
function, and remained part of the `print()` function even after the
introduction of `format()` (for compatibility reasons). Consequently,
most Python 2 programs, even the ones written using the most recent
version of Python 2, use this older-style formatting. These older
approaches are no longer supported in Python 3. By the way, the
parentheses after the `print()` function are not necessary in Python 2,
but obligatory in Python 3.

In Python 3, the `range()` function is an iterator (see Chapter
<a href="#ch:iteratorsandgenerators" data-reference-type="ref" data-reference="ch:iteratorsandgenerators">24</a>).
This entails that it needs very little memory space: it only retains the
last number generated, the step size, and the limit that it should
reach. In Python 2 `range()` is implemented differently: it produces all
the numbers of the range in memory at once. A statement like
`range(1000000000)` in Python 2 requires so much memory that it may very
well crash the program. In Python 3, such issues do not exist. In Python
2 it is therefore recommended not to use `range()` for more than 10,000
numbers or so, while in Python 3 no restrictions exist.

In Python 2, the string manipulation methods were part of the `string`
module, and were generally called by importing the module and then
writing `string.<method>()`. Such calls are no longer supported by
Python 3.

### Data structures

In Python 2, sorting a mixed list does not give a runtime error. The
`sort()` function also supports an argument `cmp=<function>`, that
allows you to specify a function that does the comparison between two
elements. This function is no longer supported in Python 3, but you can
use the key parameter for the same purpose. In the Python module
`functools` a function `cmp_to_key()` is found that turns the
old-style `cmp` specification into the new-style `key` specification.

In Python 2, the dictionary methods `keys()`, `values()`, and `items()`
return lists instead of iterators. Python 2 also supports a method
`has_key()` that you can use to check if a certain key is in a
dictionary, but this method has been removed from Python 3.

Python 2 does not support sets natively. You have to import the `sets`
module to use them. Moreover, to create a set you use the `Set()`
method, not the `set()` function. To create a set with elements in them,
in Python 2 the only way is to give the elements as a list argument to
the `Set()` method.

The structure of exceptions has changed a bit between Python 2 and
Python 3. In particular, the exception `IOError` has been made an alias
for the `OSError` exception, as it was quite hard to distinguish which
each of them tried to capture.

### Unicode

Python 2 was not yet supporting Unicode natively, while Python 3 does.
Python 3 strings are Unicode strings. You will not notice the difference
as long as strings are ASCII, but Python 2 strings might get into
troubles when Unicode characters are inserted into the strings. Python 3
also supports Unicode characters in identifiers such as variable names,
while Python 2 does not. It is not recommended that you do use non-ASCII
characters in identifiers, though.

Python 2 does not have byte strings. There is no need for them in Python
2, as it does not support Unicode. In Python 2, if you want to write a
byte with ordinal value zero, you just write `chr(0)`. The `read()` and
`write()` methods for binary files use regular strings in Python 2. This
is not allowed in Python 3.

In Python 2, the `pickle` module worked on text files. This is no longer
possible in Python 3, as Python 3 supports Unicode. Pickle files written
with Python 2 cannot be loaded in Python 3 and vice versa.

### Iterators

Python 3 is much more based on iterators and generators than Python 2,
which has all kinds of advantages, mainly as far as speed and memory
usage is concerned. Consequently, there are quite a few differences
between Python 2 and 3 in this respect. I have not inventoried all of
them, but here are a few that struck me:

Iterators in Python 2 have a `next()` method. They no longer have it in
Python 3, where it is called `__next__()`.

In Python 2 `zip()` produces a list rather than an iterable.

The `itertools` module has some differences too. For instance, in Python
2 it has a function `izip()` that produces an iterable, but since in
Python 3 `zip()` does that already, the function `izip()` has been
removed from `itertools`.

### Modules

Besides `pickle` and `itertools`, `urllib` has been changed considerably
between Python 2 and Python 3.

The `statistics` module does not exist for Python 2.
