The `glob` module provides a function `glob()` to produce lists of files
based on a wildcard search pattern that is provided as argument. The
wildcard search uses Unix conventions, most of which also hold on other
systems. They are as follows:

-   A question mark (`?`) in a file name indicates any character

-   A Kleene star (`*`) in a file name indicates any sequence of
    characters

-   A sequence of characters between square brackets (`[]`) indicates
    any of these characters; a dash may be used to indicate a sequence
    that runs from the character to the left of the dash to the
    character to the right of the dash

For instance, the wildcard search `"A[0-9]?B.*"` looks for all files
that start with the letter A, followed by a digit, followed by any
character, followed by a B, with any extension. It depends on the
operating system whether this is a case-sensitive or case-insensitive
search.

Do not confuse a wildcard search pattern with a regular expression.
While they have some superficial resemblance (such as an asterisk
indicating "a series of any characters" in both of them), they are
nothing alike. Wildcard searches only support the patterns listed above
(some of which have a different meaning for regular expressions), and
are only used for `glob` and when directly communicating with the system
via the command prompt.

```python
from glob import glob

glist = glob( "*.pdf" )
for name in glist:
    print( name )
```

The `glob` module also contains a function `iglob()`, which has the same
functionality as `glob()`, but produces an iterator instead of a list.

Use `glob()` to list all Python files in the current directory.

## `statistics`

The statistics module gives you access to various common statistical
functions. All of these functions get as argument a sequence or iterator
of numbers (integers or floats).

-   `mean()` calculates the mean (or average) of a sequence of numbers

-   `median()` calculates the median of a sequence of numbers, i.e., the
    "middle" number

-   `mode()` calculates the mode of a sequence of numbers, i.e., the
    number that occurs most often

-   `stdev()` calculates the standard deviation of a sequence of numbers

-   `variance()` calculates the variance of a sequence of numbers

There are a few more functions in the `statistics` module, but these are
the most-used ones. For more advanced statistical calculations, there
are other modules available, which I do not discuss in this book.

These functions may raise a `StatisticsError`. This is particularly
relevant in the case of the `mode()` function, as it is generated when
no unique mode can be found.

```python
from statistics import mean, median, mode, stdev, variance, \
    StatisticsError

data = [ 4, 5, 1, 1, 2, 2, 2, 3, 3, 3 ]

print( "mean:", mean( data ) )
print( "median:", median( data ) )
try:
    print( "mode:", mode( data ) )
except StatisticsError as e:
    print( e )
print( "st.dev.: {:.3f}".format( stdev( data ) ) )
print( "variance: {:.3f}".format( variance( data ) ) )
```

Note that for a sequence with an even number of numbers, the median is
the average of the two "middle" numbers. There are different ways of
calculating the median in case of an even number of numbers; if you want
to use a different one, examine other functions in the `statistics`
module.

As for the mode, in the literature you find multiple definitions of what
the mode is supposed to be. The general definition is "the most common
number," but what if there are multiple of those? What if each number is
unique? The version of the mode that the `statistics` module supports
does not seem to be the most common one.
